"""Claims CRUD + search + traceability."""
from __future__ import annotations

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from core import dag
from core.models import Claim, Status
from core.status import effective_status, EffectiveStatus
from storage import files, index

from .deps import get_data_dir, get_db


router = APIRouter(prefix="/api/claims", tags=["claims"])


@router.get("")
def search_claims(
    q: Optional[str] = None,
    course: Optional[list[str]] = Query(None),
    status: Optional[list[str]] = Query(None),
    kind: Optional[list[str]] = Query(None),
    topic: Optional[list[str]] = Query(None),
    source_ref: Optional[str] = None,
    limit: int = Query(100, le=500),
    db=Depends(get_db),
    data_dir=Depends(get_data_dir),
) -> list[dict]:
    ids = index.search_claim_ids(
        db, q=q,
        courses=course or [], statuses=status or [],
        kinds=kind or [], topics=topic or [],
        source_ref=source_ref, limit=limit,
    )
    # Return summary cards (not full files) for list view
    rows = db.execute(
        f"SELECT id, statement, kind, status, course, topic, source_ref FROM claims "
        f"WHERE id IN ({','.join('?' * len(ids))}) ORDER BY date_added DESC",
        ids,
    ).fetchall() if ids else []
    return [dict(r) for r in rows]


@router.get("/{claim_id}")
def get_claim(claim_id: str,
              data_dir=Depends(get_data_dir),
              db=Depends(get_db)) -> dict:
    claim = files.load_claim(data_dir, claim_id)
    if claim is None:
        raise HTTPException(404, f"Claim not found: {claim_id}")
    proof_ids = index.get_proof_ids_for(db, claim_id)
    canonical_id = index.get_canonical_proof_id(db, claim_id)
    citing = index.get_citing_proofs(db, claim_id)
    eff = effective_status(claim_id, index.get_status_map(db), index.get_dep_map(db))
    return {
        "claim": claim.model_dump(mode="json"),
        "proof_ids": proof_ids,
        "canonical_proof_id": canonical_id,
        "cited_by": [{"proof_id": pid, "claim_id": cid} for pid, cid in citing],
        "effective_status": eff.model_dump(mode="json"),
    }


@router.post("", status_code=201)
def create_claim(claim: Claim,
                 data_dir=Depends(get_data_dir),
                 db=Depends(get_db)) -> dict:
    if files.load_claim(data_dir, claim.id) is not None:
        raise HTTPException(409, f"Claim already exists: {claim.id}")
    files.save_claim(claim, data_dir)
    index.upsert_claim(db, claim)
    index.touch_mtime(db, data_dir)
    return claim.model_dump(mode="json")


@router.put("/{claim_id}")
def update_claim(claim_id: str, claim: Claim,
                 data_dir=Depends(get_data_dir),
                 db=Depends(get_db)) -> dict:
    if claim.id != claim_id:
        raise HTTPException(400, "ID mismatch between URL and body")
    if files.load_claim(data_dir, claim_id) is None:
        raise HTTPException(404, f"Claim not found: {claim_id}")
    files.save_claim(claim, data_dir)
    index.upsert_claim(db, claim)
    index.touch_mtime(db, data_dir)
    return claim.model_dump(mode="json")


@router.delete("/{claim_id}", status_code=204)
def delete_claim(claim_id: str,
                 data_dir=Depends(get_data_dir),
                 db=Depends(get_db)) -> None:
    if files.load_claim(data_dir, claim_id) is None:
        raise HTTPException(404, f"Claim not found: {claim_id}")
    citing = index.get_citing_proofs(db, claim_id)
    if citing:
        raise HTTPException(
            409,
            f"Cannot delete: cited by {len(citing)} proof(s). Remove those proofs/deps first.",
        )
    files.delete_claim(data_dir, claim_id)
    index.remove_claim(db, claim_id)
    index.touch_mtime(db, data_dir)


@router.post("/{claim_id}/approve")
def approve_claim(claim_id: str,
                  data_dir=Depends(get_data_dir),
                  db=Depends(get_db)) -> dict:
    """Promote claim from draft/reviewed/etc. to canonical."""
    claim = files.load_claim(data_dir, claim_id)
    if claim is None:
        raise HTTPException(404, f"Claim not found: {claim_id}")
    claim.status = Status.CANONICAL
    from datetime import UTC, datetime
    claim.date_canonized = datetime.now(UTC)
    files.save_claim(claim, data_dir)
    index.upsert_claim(db, claim)
    index.touch_mtime(db, data_dir)
    return claim.model_dump(mode="json")


@router.get("/{claim_id}/traceability")
def get_traceability(claim_id: str, db=Depends(get_db)) -> dict:
    if not db.execute("SELECT 1 FROM claims WHERE id = ?", (claim_id,)).fetchone():
        raise HTTPException(404, f"Claim not found: {claim_id}")
    return dag.traceability(claim_id, index.get_dep_map(db))


@router.get("/{claim_id}/dependents")
def get_dependents(claim_id: str, db=Depends(get_db)) -> dict:
    if not db.execute("SELECT 1 FROM claims WHERE id = ?", (claim_id,)).fetchone():
        raise HTTPException(404, f"Claim not found: {claim_id}")
    return {"claim_id": claim_id, "dependents": sorted(dag.dependents(claim_id, index.get_dep_map(db)))}


@router.get("/dag/full")
def get_full_dag(
    course: Optional[list[str]] = Query(None),
    kind: Optional[list[str]] = Query(None),
    topic: Optional[list[str]] = Query(None),
    db=Depends(get_db),
) -> dict:
    """Return all claims (optionally filtered) + every edge between them.

    Used for the standalone /dag visualization. Returns:
        {"nodes": [{id, kind, status, name, course}], "edges": [{source, target}]}
    """
    courses = course or []
    kinds = kind or []
    topics = topic or []
    ids = index.search_claim_ids(
        db, courses=courses, kinds=kinds, topics=topics, limit=10000, offset=0,
    )
    if not ids:
        return {"nodes": [], "edges": []}
    claim_set = set(ids)
    placeholder = ",".join("?" * len(ids))
    rows = db.execute(
        f"SELECT id, kind, status, course, statement FROM claims "
        f"WHERE id IN ({placeholder})",
        ids,
    ).fetchall()
    from web.filters import claim_name, clean_latex_for_label
    nodes = [{
        "id": r["id"],
        "kind": r["kind"],
        "status": r["status"],
        "course": r["course"],
        "name": clean_latex_for_label(claim_name(r["statement"])) or r["id"],
    } for r in rows]
    dep_map = index.get_dep_map(db)
    edges = [
        {"source": src, "target": tgt}
        for src, deps in dep_map.items() if src in claim_set
        for tgt in deps if tgt in claim_set
    ]
    return {"nodes": nodes, "edges": edges}


@router.get("/{claim_id}/neighborhood")
def get_neighborhood(
    claim_id: str,
    depth_down: int = 2,
    depth_up: int = 2,
    db=Depends(get_db),
) -> dict:
    """Return a focused subgraph around ``claim_id`` for visualization.

    Format suitable for Cytoscape.js / D3:
      {"nodes": [{id, kind, status, name, is_focus}], "edges": [{source, target}]}
    """
    if not db.execute("SELECT 1 FROM claims WHERE id = ?", (claim_id,)).fetchone():
        raise HTTPException(404, f"Claim not found: {claim_id}")
    dep_map = index.get_dep_map(db)
    ids, edges = dag.neighborhood(claim_id, dep_map,
                                  depth_down=depth_down, depth_up=depth_up)
    placeholder = ",".join("?" * len(ids))
    rows = db.execute(
        f"SELECT id, kind, status, statement FROM claims WHERE id IN ({placeholder})",
        list(ids),
    ).fetchall()
    from web.filters import claim_name, clean_latex_for_label
    nodes = [{
        "id": r["id"],
        "kind": r["kind"],
        "status": r["status"],
        "name": clean_latex_for_label(claim_name(r["statement"])) or r["id"],
        "is_focus": r["id"] == claim_id,
    } for r in rows]
    return {
        "nodes": nodes,
        "edges": [{"source": s, "target": t} for s, t in edges],
        "focus": claim_id,
    }
