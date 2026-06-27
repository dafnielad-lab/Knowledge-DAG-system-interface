"""Proofs CRUD with cycle detection on canonical proofs."""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException

from core import dag
from core.models import Proof
from storage import files, index

from .deps import get_data_dir, get_db


router = APIRouter(prefix="/api/proofs", tags=["proofs"])


def _validate_proof(proof: Proof, db, data_dir) -> None:
    """Shared validation: claim exists, all deps exist, no cycle if canonical."""
    if not db.execute("SELECT 1 FROM claims WHERE id = ?", (proof.claim_id,)).fetchone():
        raise HTTPException(400, f"Target claim does not exist: {proof.claim_id}")
    all_ids = set(index.all_claim_ids(db))
    missing = [d for d in proof.dependencies if d not in all_ids]
    if missing:
        raise HTTPException(400, f"Unknown dependency claims: {missing}")
    if proof.is_canonical:
        dep_map = index.get_dep_map(db)
        # Exclude this proof's old canonical entry (if any) before checking
        if proof.claim_id in dep_map:
            dep_map = {k: v for k, v in dep_map.items() if k != proof.claim_id}
        if dag.has_cycle(proof.claim_id, proof.dependencies, dep_map):
            raise HTTPException(400,
                f"Would create a cycle: {proof.claim_id} cannot transitively depend on itself")


def _demote_other_canonicals(claim_id: str, except_proof_id: str, data_dir, db) -> None:
    """Mark all other canonical proofs for this claim as non-canonical (file + index)."""
    rows = db.execute(
        "SELECT id FROM proofs WHERE claim_id = ? AND is_canonical = 1 AND id != ?",
        (claim_id, except_proof_id),
    ).fetchall()
    for row in rows:
        other = files.load_proof(data_dir, row[0])
        if other is not None:
            other.is_canonical = False
            files.save_proof(other, data_dir)
            index.upsert_proof(db, other)


@router.get("/{proof_id}")
def get_proof(proof_id: str,
              data_dir=Depends(get_data_dir),
              db=Depends(get_db)) -> dict:
    proof = files.load_proof(data_dir, proof_id)
    if proof is None:
        raise HTTPException(404, f"Proof not found: {proof_id}")
    return proof.model_dump(mode="json")


@router.post("", status_code=201)
def create_proof(proof: Proof,
                 data_dir=Depends(get_data_dir),
                 db=Depends(get_db)) -> dict:
    if files.load_proof(data_dir, proof.id) is not None:
        raise HTTPException(409, f"Proof already exists: {proof.id}")
    _validate_proof(proof, db, data_dir)
    files.save_proof(proof, data_dir)
    index.upsert_proof(db, proof)
    if proof.is_canonical:
        _demote_other_canonicals(proof.claim_id, proof.id, data_dir, db)
    index.touch_mtime(db, data_dir)
    return proof.model_dump(mode="json")


@router.put("/{proof_id}")
def update_proof(proof_id: str, proof: Proof,
                 data_dir=Depends(get_data_dir),
                 db=Depends(get_db)) -> dict:
    if proof.id != proof_id:
        raise HTTPException(400, "ID mismatch between URL and body")
    if files.load_proof(data_dir, proof_id) is None:
        raise HTTPException(404, f"Proof not found: {proof_id}")
    _validate_proof(proof, db, data_dir)
    files.save_proof(proof, data_dir)
    index.upsert_proof(db, proof)
    if proof.is_canonical:
        _demote_other_canonicals(proof.claim_id, proof.id, data_dir, db)
    index.touch_mtime(db, data_dir)
    return proof.model_dump(mode="json")


@router.delete("/{proof_id}", status_code=204)
def delete_proof(proof_id: str,
                 data_dir=Depends(get_data_dir),
                 db=Depends(get_db)) -> None:
    if files.load_proof(data_dir, proof_id) is None:
        raise HTTPException(404, f"Proof not found: {proof_id}")
    files.delete_proof(data_dir, proof_id)
    index.remove_proof(db, proof_id)
    index.touch_mtime(db, data_dir)
