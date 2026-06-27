"""Cowork ingest — accepts a batch of claims+proofs+courses extracted from
a lecture/textbook/etc. and stores them as drafts with shared provenance.

The DAG system does not know about Zoom, transcripts, or AI. A Cowork plugin
(separate component) does the extraction work and POSTs structured data here.
This keeps concerns separated: extraction strategy can evolve without touching
storage or the DAG model.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends

from core.models import IngestBatch, IngestReceipt, Status, ProofStatus
from storage import files, index

from .deps import get_data_dir, get_db


router = APIRouter(prefix="/api/cowork", tags=["cowork"])


@router.post("/ingest", response_model=IngestReceipt)
def ingest(batch: IngestBatch,
           data_dir=Depends(get_data_dir),
           db=Depends(get_db)) -> IngestReceipt:
    """Persist a batch. Every claim/proof gets shared source provenance and
    status=draft. The client (Cowork plugin) is responsible for shaping the
    batch — extracting from transcript, deduping against existing claims, etc.

    Returns a review URL the user can open to triage the drafts.
    """
    accepted_claims: list[str] = []
    accepted_proofs: list[str] = []
    rejected: list[dict] = []

    existing_ids = set(index.all_claim_ids(db))

    # Courses first (so claim.course references resolve)
    for c in batch.courses:
        try:
            if files.load_course(data_dir, c.id) is None:
                files.save_course(c, data_dir)
                index.upsert_course(db, c)
        except Exception as e:
            rejected.append({"id": c.id, "kind": "course", "reason": str(e)})

    # Claims
    for c in batch.claims:
        try:
            if c.source is None:
                c.source = batch.source
            c.status = Status.DRAFT
            if files.load_claim(data_dir, c.id) is not None:
                rejected.append({"id": c.id, "kind": "claim", "reason": "already exists"})
                continue
            files.save_claim(c, data_dir)
            index.upsert_claim(db, c)
            existing_ids.add(c.id)
            accepted_claims.append(c.id)
        except Exception as e:
            rejected.append({"id": c.id, "kind": "claim", "reason": str(e)})

    # Proofs (after claims so deps resolve)
    for p in batch.proofs:
        try:
            if p.source is None:
                p.source = batch.source
            p.status = ProofStatus.DRAFT
            if files.load_proof(data_dir, p.id) is not None:
                rejected.append({"id": p.id, "kind": "proof", "reason": "already exists"})
                continue
            if p.claim_id not in existing_ids:
                rejected.append({"id": p.id, "kind": "proof",
                                 "reason": f"target claim missing: {p.claim_id}"})
                continue
            unknown = [d for d in p.dependencies if d not in existing_ids]
            if unknown:
                rejected.append({"id": p.id, "kind": "proof",
                                 "reason": f"unknown dependencies: {unknown}"})
                continue
            files.save_proof(p, data_dir)
            index.upsert_proof(db, p)
            accepted_proofs.append(p.id)
        except Exception as e:
            rejected.append({"id": p.id, "kind": "proof", "reason": str(e)})

    index.touch_mtime(db, data_dir)

    review_url = f"/?status=draft&source_ref={batch.source.ref}"
    return IngestReceipt(
        accepted_claims=accepted_claims,
        accepted_proofs=accepted_proofs,
        rejected=rejected,
        review_url=review_url,
    )
