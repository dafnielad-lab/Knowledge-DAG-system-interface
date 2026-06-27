"""Courses CRUD + 'available claims' query for context filtering."""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException

from core import context
from core.models import Course
from storage import files, index

from .deps import get_data_dir, get_db


router = APIRouter(prefix="/api/courses", tags=["courses"])


@router.get("")
def list_courses(db=Depends(get_db)) -> list[dict]:
    return [dict(r) for r in db.execute("SELECT id, name FROM courses ORDER BY id").fetchall()]


@router.get("/{course_id}")
def get_course(course_id: str,
               data_dir=Depends(get_data_dir)) -> dict:
    course = files.load_course(data_dir, course_id)
    if course is None:
        raise HTTPException(404, f"Course not found: {course_id}")
    return course.model_dump(mode="json")


@router.post("", status_code=201)
def create_course(course: Course,
                  data_dir=Depends(get_data_dir),
                  db=Depends(get_db)) -> dict:
    if files.load_course(data_dir, course.id) is not None:
        raise HTTPException(409, f"Course already exists: {course.id}")
    files.save_course(course, data_dir)
    index.upsert_course(db, course)
    index.touch_mtime(db, data_dir)
    return course.model_dump(mode="json")


@router.put("/{course_id}")
def update_course(course_id: str, course: Course,
                  data_dir=Depends(get_data_dir),
                  db=Depends(get_db)) -> dict:
    if course.id != course_id:
        raise HTTPException(400, "ID mismatch between URL and body")
    if files.load_course(data_dir, course_id) is None:
        raise HTTPException(404, f"Course not found: {course_id}")
    files.save_course(course, data_dir)
    index.upsert_course(db, course)
    index.touch_mtime(db, data_dir)
    return course.model_dump(mode="json")


@router.delete("/{course_id}", status_code=204)
def delete_course(course_id: str,
                  data_dir=Depends(get_data_dir),
                  db=Depends(get_db)) -> None:
    if files.load_course(data_dir, course_id) is None:
        raise HTTPException(404, f"Course not found: {course_id}")
    files.delete_course(data_dir, course_id)
    db.execute("DELETE FROM course_prereqs WHERE course_id = ?", (course_id,))
    db.execute("DELETE FROM courses WHERE id = ?", (course_id,))
    db.commit()
    index.touch_mtime(db, data_dir)


@router.get("/{course_id}/available")
def get_available_claims(course_id: str,
                         data_dir=Depends(get_data_dir),
                         db=Depends(get_db)) -> dict:
    """Returns the set of claim ids citable inside the given course's context."""
    all_courses = [files.load_course(data_dir, cid) for cid in index.all_course_ids(db)]
    course_map = {c.id: c for c in all_courses if c}
    if course_id not in course_map:
        raise HTTPException(404, f"Course not found: {course_id}")
    claim_to_course = index.get_claim_to_course(db)
    allowed = context.allowed_claims(course_id, course_map, claim_to_course)
    return {"course_id": course_id, "allowed_claim_ids": sorted(allowed)}
