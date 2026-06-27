"""HTML page routes — full-page renders. Forms POST to ui.py routes."""
from __future__ import annotations

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Request
from starlette.responses import HTMLResponse

from core import dag
from core.status import effective_status
from core.topic_groups import TOPIC_GROUPS, topic_groups_with_other, topic_to_group
from storage import files, index

from api.deps import get_data_dir, get_db
from web.filters import claim_name, clean_latex_for_label


def _build_name_map(db, ids):
    """Map claim_id → display name (the **name:** prefix cleaned of LaTeX,
    or the id as fallback). Used in plain-text surfaces (tree, dep lists)."""
    ids = [i for i in set(ids) if i]
    if not ids:
        return {}
    placeholder = ",".join("?" * len(ids))
    rows = db.execute(
        f"SELECT id, statement FROM claims WHERE id IN ({placeholder})",
        ids,
    ).fetchall()
    return {row[0]: (clean_latex_for_label(claim_name(row[1])) or row[0]) for row in rows}


def _collect_tree_ids(node):
    """Walk a traceability tree, return all IDs referenced."""
    ids = {node["id"]}
    for child in node.get("children", []):
        ids.update(_collect_tree_ids(child))
    return ids


router = APIRouter(tags=["views"])


def _templates(request: Request):
    return request.app.state.templates


def _color_for_status(s: str) -> str:
    if s in ("canonical", "formally_verified"):
        return "green"
    if s == "conjectured":
        return "red"
    return "amber"


PAGE_SIZE_OPTIONS = [25, 50, 100, 250, 500]
MAX_PAGE_SIZE = 2000


@router.get("/", response_class=HTMLResponse)
def index_page(
    request: Request,
    q: Optional[str] = None,
    course: Optional[list[str]] = Query(None),
    status: Optional[list[str]] = Query(None),
    kind: Optional[list[str]] = Query(None),
    topic: Optional[list[str]] = Query(None),
    source_ref: Optional[str] = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(100, ge=1, le=MAX_PAGE_SIZE),
    data_dir=Depends(get_data_dir),
    db=Depends(get_db),
):
    courses_sel = course or []
    statuses_sel = status or []
    kinds_sel = kind or []
    topics_sel = topic or []
    source_ref_v = source_ref or None

    filtered_count = index.count_claims(
        db, q=q or None,
        courses=courses_sel, statuses=statuses_sel,
        kinds=kinds_sel, topics=topics_sel,
        source_ref=source_ref_v,
    )
    total_in_db = db.execute("SELECT COUNT(*) FROM claims").fetchone()[0]

    total_pages = max(1, (filtered_count + page_size - 1) // page_size)
    if page > total_pages:
        page = total_pages
    offset = (page - 1) * page_size

    ids = index.search_claim_ids(
        db, q=q or None,
        courses=courses_sel, statuses=statuses_sel,
        kinds=kinds_sel, topics=topics_sel,
        source_ref=source_ref_v,
        limit=page_size, offset=offset,
    )
    if ids:
        placeholder = ",".join("?" * len(ids))
        rows = db.execute(
            f"SELECT id, statement, kind, status, course, topic, source_ref "
            f"FROM claims WHERE id IN ({placeholder}) ORDER BY date_added DESC",
            ids,
        ).fetchall()
        claims = [dict(r) | {"color": _color_for_status(r["status"])} for r in rows]
    else:
        claims = []

    course_rows = [dict(r) for r in db.execute("SELECT id, name FROM courses ORDER BY name").fetchall()]
    topics = index.all_topics(db)
    topic_groups = topic_groups_with_other(topics)
    topic_to_group_map = topic_to_group()
    has_filter = bool(q or courses_sel or statuses_sel or kinds_sel or topics_sel or source_ref_v)
    showing_from = offset + 1 if claims else 0
    showing_to = offset + len(claims)

    return _templates(request).TemplateResponse(
        request=request,
        name="index.html",
        context={
            "claims": claims,
            "total_in_db": total_in_db,
            "filtered_count": filtered_count,
            "has_filter": has_filter,
            "page": page,
            "page_size": page_size,
            "total_pages": total_pages,
            "showing_from": showing_from,
            "showing_to": showing_to,
            "page_size_options": PAGE_SIZE_OPTIONS,
            "courses": course_rows,
            "topics": topics,
            "topic_groups": topic_groups,
            "topic_to_group": topic_to_group_map,
            "q": q,
            "filters": {
                "course": courses_sel, "status": statuses_sel,
                "kind": kinds_sel, "topic": topics_sel,
                "source_ref": source_ref_v,
            },
        },
    )


@router.get("/claims/new", response_class=HTMLResponse)
def claim_new_form(request: Request):
    return _templates(request).TemplateResponse(
        request=request, name="claim_edit.html",
        context={"mode": "new", "claim": None})


@router.get("/claims/{claim_id}/edit", response_class=HTMLResponse)
def claim_edit_form(claim_id: str, request: Request,
                    data_dir=Depends(get_data_dir)):
    claim = files.load_claim(data_dir, claim_id)
    if claim is None:
        raise HTTPException(404, f"Claim not found: {claim_id}")
    return _templates(request).TemplateResponse(
        request=request, name="claim_edit.html",
        context={"mode": "edit", "claim": claim.model_dump(mode="json")})


@router.get("/claims/{claim_id}", response_class=HTMLResponse)
def claim_view(claim_id: str, request: Request,
               data_dir=Depends(get_data_dir),
               db=Depends(get_db)):
    claim = files.load_claim(data_dir, claim_id)
    if claim is None:
        raise HTTPException(404, f"Claim not found: {claim_id}")
    proof_ids = index.get_proof_ids_for(db, claim_id)
    proofs = [files.load_proof(data_dir, pid) for pid in proof_ids]
    proofs = [p.model_dump(mode="json") for p in proofs if p is not None]
    citing = index.get_citing_proofs(db, claim_id)
    dep_map = index.get_dep_map(db)
    eff = effective_status(claim_id, index.get_status_map(db), dep_map)
    trace_ancestors = dag.traceability(claim_id, dep_map)
    trace_descendants = dag.traceability_dependents(claim_id, dep_map)

    # Collect every claim id referenced on this page so we can label
    # tree/dep/citing entries by their Hebrew name instead of the bare id.
    referenced_ids = set(_collect_tree_ids(trace_ancestors))
    referenced_ids.update(_collect_tree_ids(trace_descendants))
    for p in proofs:
        referenced_ids.update(p.get("dependencies", []))
    for _, cid in citing:
        referenced_ids.add(cid)
    name_map = _build_name_map(db, referenced_ids)

    return _templates(request).TemplateResponse(
        request=request,
        name="claim_view.html",
        context={
            "claim": claim.model_dump(mode="json"),
            "proof_ids": proof_ids,
            "proofs": proofs,
            "cited_by": [{"proof_id": pid, "claim_id": cid} for pid, cid in citing],
            "effective": eff.model_dump(mode="json") | {"color": eff.color},
            "traceability": trace_ancestors,
            "traceability_descendants": trace_descendants,
            "name_map": name_map,
        },
    )


@router.get("/proofs/new", response_class=HTMLResponse)
def proof_new_form(request: Request, claim_id: Optional[str] = None):
    return _templates(request).TemplateResponse(
        request=request, name="proof_edit.html",
        context={"mode": "new", "proof": None, "claim_id": claim_id})


@router.get("/proofs/{proof_id}/edit", response_class=HTMLResponse)
def proof_edit_form(proof_id: str, request: Request,
                    data_dir=Depends(get_data_dir)):
    proof = files.load_proof(data_dir, proof_id)
    if proof is None:
        raise HTTPException(404, f"Proof not found: {proof_id}")
    return _templates(request).TemplateResponse(
        request=request, name="proof_edit.html",
        context={"mode": "edit", "proof": proof.model_dump(mode="json")})


@router.get("/dag", response_class=HTMLResponse)
def dag_full_view(request: Request,
                  db=Depends(get_db)):
    course_rows = [dict(r) for r in db.execute("SELECT id, name FROM courses ORDER BY name").fetchall()]
    topics = index.all_topics(db)
    return _templates(request).TemplateResponse(
        request=request,
        name="dag_view.html",
        context={"courses": course_rows, "topics": topics,
                 "topic_groups": topic_groups_with_other(topics)},
    )


@router.get("/courses", response_class=HTMLResponse)
def courses_index(request: Request,
                  data_dir=Depends(get_data_dir),
                  db=Depends(get_db)):
    courses = [files.load_course(data_dir, cid) for cid in index.all_course_ids(db)]
    courses = [c.model_dump(mode="json") for c in courses if c is not None]
    return _templates(request).TemplateResponse(
        request=request, name="courses.html",
        context={"courses": courses})


@router.get("/courses/new", response_class=HTMLResponse)
def course_new_form(request: Request):
    return _templates(request).TemplateResponse(
        request=request, name="course_edit.html",
        context={"mode": "new", "course": None})


@router.get("/courses/{course_id}", response_class=HTMLResponse)
@router.get("/courses/{course_id}/edit", response_class=HTMLResponse)
def course_edit_form(course_id: str, request: Request,
                     data_dir=Depends(get_data_dir)):
    course = files.load_course(data_dir, course_id)
    if course is None:
        raise HTTPException(404, f"Course not found: {course_id}")
    return _templates(request).TemplateResponse(
        request=request, name="course_edit.html",
        context={"mode": "edit", "course": course.model_dump(mode="json")})
