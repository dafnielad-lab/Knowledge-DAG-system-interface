"""Course-context filtering — which claims/proofs are citable inside a given course.

The Open University specifies prerequisites per course; this module computes
the citable set automatically from that graph. A course's ``allowed_claims``
field can override the computed set.
"""
from __future__ import annotations

from .models import Course, Proof


def transitive_courses(course_id: str, course_map: dict[str, Course]) -> set[str]:
    """All courses in the prerequisite closure of ``course_id``, including itself."""
    visited: set[str] = set()
    stack: list[str] = [course_id]
    while stack:
        cur = stack.pop()
        if cur in visited:
            continue
        visited.add(cur)
        course = course_map.get(cur)
        if course:
            stack.extend(course.prerequisites)
    return visited


def allowed_claims(
    course_id: str,
    course_map: dict[str, Course],
    claim_to_course: dict[str, str | None],
) -> set[str]:
    """Set of claim ids that may be cited within ``course_id``."""
    course = course_map.get(course_id)
    if course is None:
        return set()
    if course.allowed_claims is not None:
        return set(course.allowed_claims)
    in_scope = transitive_courses(course_id, course_map)
    return {cid for cid, c in claim_to_course.items() if c in in_scope}


def proof_allowed(proof: Proof, allowed: set[str]) -> bool:
    """Is this proof usable in a context where ``allowed`` is the citable set?

    A proof is allowed iff every claim it cites is in the allowed set.
    """
    return all(dep in allowed for dep in proof.dependencies)
