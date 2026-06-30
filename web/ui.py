"""Form-submit routes that mutate state and redirect.

Separate from /api so the JSON API stays clean. Both call the same files+index
business logic underneath.
"""
from __future__ import annotations

from datetime import UTC, datetime
from typing import Optional

from fastapi import APIRouter, Depends, Form, HTTPException
from starlette.responses import RedirectResponse

from core import dag
from core.models import Claim, Course, Proof, Status
from storage import files, index

from api.deps import get_data_dir, get_db, get_db_path


router = APIRouter(prefix="/ui", tags=["ui"])


def _split_csv(s: Optional[str]) -> list[str]:
    if not s:
        return []
    return [x.strip() for x in s.split(",") if x.strip()]


def _redirect(path: str) -> RedirectResponse:
    return RedirectResponse(path, status_code=303)


# ────── Claims ──────

@router.post("/claims/new")
def claims_new(
    id: str = Form(...),
    statement: str = Form(...),
    kind: str = Form(...),
    status: str = Form("draft"),
    course: str = Form(""),
    topic: str = Form(""),
    notes: str = Form(""),
    data_dir=Depends(get_data_dir),
    db=Depends(get_db),
):
    try:
        claim = Claim(
            id=id, statement=statement, kind=kind, status=status,
            course=course or None, topic=topic or None, notes=notes or None,
        )
    except Exception as e:
        return _redirect(f"/claims/new?error={e}")
    if files.load_claim(data_dir, claim.id) is not None:
        return _redirect(f"/claims/new?error=Already+exists:{claim.id}")
    files.save_claim(claim, data_dir)
    index.upsert_claim(db, claim)
    index.touch_mtime(db, data_dir)
    return _redirect(f"/claims/{claim.id}")


@router.post("/claims/{claim_id}/update")
def claims_update(
    claim_id: str,
    statement: str = Form(...),
    kind: str = Form(...),
    status: str = Form("draft"),
    course: str = Form(""),
    topic: str = Form(""),
    notes: str = Form(""),
    data_dir=Depends(get_data_dir),
    db=Depends(get_db),
):
    existing = files.load_claim(data_dir, claim_id)
    if existing is None:
        raise HTTPException(404, f"Claim not found: {claim_id}")
    claim = Claim(
        id=claim_id, statement=statement, kind=kind, status=status,
        course=course or None, topic=topic or None, notes=notes or None,
        date_added=existing.date_added,
        date_canonized=existing.date_canonized,
        source=existing.source,
        relates_to=existing.relates_to,
        relation_kind=existing.relation_kind,
    )
    files.save_claim(claim, data_dir)
    index.upsert_claim(db, claim)
    index.touch_mtime(db, data_dir)
    return _redirect(f"/claims/{claim_id}")


@router.post("/claims/{claim_id}/delete")
def claims_delete(claim_id: str,
                  data_dir=Depends(get_data_dir),
                  db=Depends(get_db)):
    if files.load_claim(data_dir, claim_id) is None:
        raise HTTPException(404, f"Claim not found: {claim_id}")
    if index.get_citing_proofs(db, claim_id):
        return _redirect(f"/claims/{claim_id}?error=Cited+by+other+proofs")
    files.delete_claim(data_dir, claim_id)
    index.remove_claim(db, claim_id)
    index.touch_mtime(db, data_dir)
    return _redirect("/")


@router.post("/claims/{claim_id}/approve")
def claims_approve(claim_id: str,
                   data_dir=Depends(get_data_dir),
                   db=Depends(get_db)):
    claim = files.load_claim(data_dir, claim_id)
    if claim is None:
        raise HTTPException(404, f"Claim not found: {claim_id}")
    claim.status = Status.CANONICAL
    claim.date_canonized = datetime.now(UTC)
    files.save_claim(claim, data_dir)
    index.upsert_claim(db, claim)
    index.touch_mtime(db, data_dir)
    return _redirect(f"/claims/{claim_id}")


# ────── Proofs ──────

@router.post("/proofs/new")
def proofs_new(
    id: str = Form(...),
    claim_id: str = Form(...),
    body: str = Form(...),
    method: str = Form("informal"),
    status: str = Form("draft"),
    dependencies: str = Form(""),
    is_canonical: Optional[str] = Form(None),
    data_dir=Depends(get_data_dir),
    db=Depends(get_db),
):
    deps = _split_csv(dependencies)
    canonical = is_canonical == "true"
    try:
        proof = Proof(
            id=id, claim_id=claim_id, body=body, method=method,
            status=status, dependencies=deps, is_canonical=canonical,
        )
    except Exception as e:
        return _redirect(f"/proofs/new?claim_id={claim_id}&error={e}")
    if files.load_proof(data_dir, proof.id) is not None:
        return _redirect(f"/proofs/new?claim_id={claim_id}&error=Already+exists:{proof.id}")

    err = _validate_proof(proof, db)
    if err:
        return _redirect(f"/proofs/new?claim_id={claim_id}&error={err}")

    files.save_proof(proof, data_dir)
    index.upsert_proof(db, proof)
    if proof.is_canonical:
        _demote_other_canonicals(proof.claim_id, proof.id, data_dir, db)
    index.touch_mtime(db, data_dir)
    return _redirect(f"/claims/{proof.claim_id}")


@router.post("/proofs/{proof_id}/update")
def proofs_update(
    proof_id: str,
    claim_id: str = Form(...),
    body: str = Form(...),
    method: str = Form("informal"),
    status: str = Form("draft"),
    dependencies: str = Form(""),
    is_canonical: Optional[str] = Form(None),
    data_dir=Depends(get_data_dir),
    db=Depends(get_db),
):
    existing = files.load_proof(data_dir, proof_id)
    if existing is None:
        raise HTTPException(404, f"Proof not found: {proof_id}")
    deps = _split_csv(dependencies)
    canonical = is_canonical == "true"
    proof = Proof(
        id=proof_id, claim_id=claim_id, body=body, method=method,
        status=status, dependencies=deps, is_canonical=canonical,
        date_added=existing.date_added, source=existing.source,
    )
    err = _validate_proof(proof, db)
    if err:
        return _redirect(f"/proofs/{proof_id}/edit?error={err}")
    files.save_proof(proof, data_dir)
    index.upsert_proof(db, proof)
    if proof.is_canonical:
        _demote_other_canonicals(proof.claim_id, proof.id, data_dir, db)
    index.touch_mtime(db, data_dir)
    return _redirect(f"/claims/{proof.claim_id}")


@router.post("/proofs/{proof_id}/delete")
def proofs_delete(proof_id: str,
                  data_dir=Depends(get_data_dir),
                  db=Depends(get_db)):
    proof = files.load_proof(data_dir, proof_id)
    if proof is None:
        raise HTTPException(404, f"Proof not found: {proof_id}")
    claim_id = proof.claim_id
    files.delete_proof(data_dir, proof_id)
    index.remove_proof(db, proof_id)
    index.touch_mtime(db, data_dir)
    return _redirect(f"/claims/{claim_id}")


# ────── Maintenance ──────

@router.post("/rebuild_index")
def rebuild_index_action(
    next: str = Form("/"),
    data_dir=Depends(get_data_dir),
    db_path=Depends(get_db_path),
):
    """Force-rebuild the SQLite index from the file store. Safe to call any time.

    Useful when claim/proof MD files were edited outside the app (direct edit,
    git pull, etc.) and the index might be stale.
    """
    index.rebuild_index(data_dir, db_path)
    return _redirect(next)


def _validate_proof(proof: Proof, db) -> Optional[str]:
    if not db.execute("SELECT 1 FROM claims WHERE id = ?", (proof.claim_id,)).fetchone():
        return f"Target claim does not exist: {proof.claim_id}"
    all_ids = set(index.all_claim_ids(db))
    missing = [d for d in proof.dependencies if d not in all_ids]
    if missing:
        return f"Unknown dependency claims: {missing}"
    if proof.is_canonical:
        dep_map = index.get_dep_map(db)
        dep_map = {k: v for k, v in dep_map.items() if k != proof.claim_id}
        if dag.has_cycle(proof.claim_id, proof.dependencies, dep_map):
            return f"Would create a cycle: {proof.claim_id} cannot transitively depend on itself"
    return None


def _demote_other_canonicals(claim_id: str, except_proof_id: str, data_dir, db) -> None:
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


# ────── Courses ──────

@router.post("/courses/new")
def courses_new(
    id: str = Form(...),
    name: str = Form(...),
    prerequisites: str = Form(""),
    data_dir=Depends(get_data_dir),
    db=Depends(get_db),
):
    try:
        course = Course(id=id, name=name, prerequisites=_split_csv(prerequisites))
    except Exception as e:
        return _redirect(f"/courses/new?error={e}")
    if files.load_course(data_dir, course.id) is not None:
        return _redirect(f"/courses/new?error=Already+exists:{course.id}")
    files.save_course(course, data_dir)
    index.upsert_course(db, course)
    index.touch_mtime(db, data_dir)
    return _redirect("/courses")


@router.post("/courses/{course_id}/update")
def courses_update(
    course_id: str,
    name: str = Form(...),
    prerequisites: str = Form(""),
    data_dir=Depends(get_data_dir),
    db=Depends(get_db),
):
    existing = files.load_course(data_dir, course_id)
    if existing is None:
        raise HTTPException(404, f"Course not found: {course_id}")
    course = Course(id=course_id, name=name,
                    prerequisites=_split_csv(prerequisites),
                    notation=existing.notation,
                    allowed_claims=existing.allowed_claims)
    files.save_course(course, data_dir)
    index.upsert_course(db, course)
    index.touch_mtime(db, data_dir)
    return _redirect("/courses")


@router.post("/courses/{course_id}/delete")
def courses_delete(course_id: str,
                   data_dir=Depends(get_data_dir),
                   db=Depends(get_db)):
    if files.load_course(data_dir, course_id) is None:
        raise HTTPException(404, f"Course not found: {course_id}")
    files.delete_course(data_dir, course_id)
    db.execute("DELETE FROM course_prereqs WHERE course_id = ?", (course_id,))
    db.execute("DELETE FROM courses WHERE id = ?", (course_id,))
    db.commit()
    index.touch_mtime(db, data_dir)
    return _redirect("/courses")
