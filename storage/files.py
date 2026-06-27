"""File-based storage. Markdown+YAML is the source of truth.

CRITICAL: every read/write opens with ``encoding='utf-8'`` explicit.
PowerShell Get/Set-Content uses CP1255 on Hebrew systems and silently corrupts
Hebrew characters in mixed files — never let those tools touch these files.
"""
from __future__ import annotations

from pathlib import Path

import frontmatter
import yaml

from core.models import Claim, Course, Proof


CLAIMS_DIR = "claims"
PROOFS_DIR = "proofs"
COURSES_DIR = "courses"
SCHEMA_FILE = "SCHEMA_VERSION"


# ────── Path helpers ──────

def claim_path(data_dir: Path, claim_id: str) -> Path:
    return data_dir / CLAIMS_DIR / f"{claim_id}.md"


def proof_path(data_dir: Path, proof_id: str) -> Path:
    return data_dir / PROOFS_DIR / f"{proof_id}.md"


def course_path(data_dir: Path, course_id: str) -> Path:
    return data_dir / COURSES_DIR / f"{course_id}.yaml"


# ────── Serialization ──────

def _format_post(metadata: dict, content: str) -> str:
    """Produce a Markdown file with YAML frontmatter, allowing unicode (Hebrew)."""
    yaml_text = yaml.safe_dump(
        metadata,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    ).rstrip()
    return f"---\n{yaml_text}\n---\n\n{content.rstrip()}\n"


# ────── Load ──────

def _load_claim_file(path: Path) -> Claim:
    text = path.read_text(encoding="utf-8")
    post = frontmatter.loads(text)
    data = dict(post.metadata)
    data["statement"] = post.content.strip()
    return Claim.model_validate(data)


def _load_proof_file(path: Path) -> Proof:
    text = path.read_text(encoding="utf-8")
    post = frontmatter.loads(text)
    data = dict(post.metadata)
    data["body"] = post.content.strip()
    return Proof.model_validate(data)


def _load_course_file(path: Path) -> Course:
    text = path.read_text(encoding="utf-8")
    data = yaml.safe_load(text)
    return Course.model_validate(data)


def load_claim(data_dir: Path, claim_id: str) -> Claim | None:
    p = claim_path(data_dir, claim_id)
    return _load_claim_file(p) if p.exists() else None


def load_proof(data_dir: Path, proof_id: str) -> Proof | None:
    p = proof_path(data_dir, proof_id)
    return _load_proof_file(p) if p.exists() else None


def load_course(data_dir: Path, course_id: str) -> Course | None:
    p = course_path(data_dir, course_id)
    return _load_course_file(p) if p.exists() else None


# ────── Save ──────

def save_claim(claim: Claim, data_dir: Path) -> Path:
    p = claim_path(data_dir, claim.id)
    p.parent.mkdir(parents=True, exist_ok=True)
    meta = claim.model_dump(mode="json", exclude={"statement"}, exclude_none=True)
    p.write_text(_format_post(meta, claim.statement), encoding="utf-8")
    return p


def save_proof(proof: Proof, data_dir: Path) -> Path:
    p = proof_path(data_dir, proof.id)
    p.parent.mkdir(parents=True, exist_ok=True)
    meta = proof.model_dump(mode="json", exclude={"body"}, exclude_none=True)
    p.write_text(_format_post(meta, proof.body), encoding="utf-8")
    return p


def save_course(course: Course, data_dir: Path) -> Path:
    p = course_path(data_dir, course.id)
    p.parent.mkdir(parents=True, exist_ok=True)
    data = course.model_dump(mode="json", exclude_none=True)
    text = yaml.safe_dump(data, allow_unicode=True, sort_keys=False, default_flow_style=False)
    p.write_text(text, encoding="utf-8")
    return p


# ────── Delete ──────

def delete_claim(data_dir: Path, claim_id: str) -> bool:
    p = claim_path(data_dir, claim_id)
    if p.exists():
        p.unlink()
        return True
    return False


def delete_proof(data_dir: Path, proof_id: str) -> bool:
    p = proof_path(data_dir, proof_id)
    if p.exists():
        p.unlink()
        return True
    return False


def delete_course(data_dir: Path, course_id: str) -> bool:
    p = course_path(data_dir, course_id)
    if p.exists():
        p.unlink()
        return True
    return False


# ────── Scan ──────

def scan_data_dir(data_dir: Path) -> tuple[list[Claim], list[Proof], list[Course]]:
    claims = [_load_claim_file(p) for p in sorted((data_dir / CLAIMS_DIR).glob("*.md"))]
    proofs = [_load_proof_file(p) for p in sorted((data_dir / PROOFS_DIR).glob("*.md"))]
    courses = [_load_course_file(p) for p in sorted((data_dir / COURSES_DIR).glob("*.yaml"))]
    return claims, proofs, courses


def latest_mtime(data_dir: Path) -> float:
    """Most recent mtime under data_dir; used to decide if SQLite index is stale."""
    mts: list[float] = []
    for ext in ("*.md", "*.yaml"):
        mts.extend(p.stat().st_mtime for p in data_dir.rglob(ext))
    return max(mts) if mts else 0.0


def read_schema_version(data_dir: Path) -> int:
    p = data_dir / SCHEMA_FILE
    if not p.exists():
        return 0
    return int(p.read_text(encoding="utf-8").strip())
