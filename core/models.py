"""Pydantic models — the keystone of the schema.

Everything that crosses a layer boundary (file, DB, API, template) speaks these types.
Adding a new verification method, source type, or status is a one-enum-entry change.
"""
from __future__ import annotations

from datetime import UTC, datetime
from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


CURRENT_SCHEMA_VERSION = 1


# ────── Enums ──────

class Kind(StrEnum):
    AXIOM = "axiom"
    THEOREM = "theorem"
    LEMMA = "lemma"
    DEFINITION = "definition"
    RELATION = "relation"


class Status(StrEnum):
    DRAFT = "draft"
    SELF_PROVED = "self_proved"
    AI_VERIFIED = "ai_verified"
    REVIEWED = "reviewed"
    CANONICAL = "canonical"
    FORMALLY_VERIFIED = "formally_verified"
    CONJECTURED = "conjectured"


class RelationKind(StrEnum):
    IMPLIES = "implies"
    EQUIVALENCE = "equivalence"
    CONTRADICTS = "contradicts"
    INDEPENDENT = "independent"


class ProofMethod(StrEnum):
    AXIOM = "axiom"
    INFORMAL = "informal"
    LEAN = "lean"
    AI_VERIFIED = "ai_verified"
    TRUTH_TABLE = "truth_table"
    SAT = "sat"
    OMEGA = "omega"
    GROEBNER = "groebner"
    DECISION_PROCEDURE = "decision_procedure"


class ProofStatus(StrEnum):
    DRAFT = "draft"
    REVIEWED = "reviewed"
    VERIFIED = "verified"


class SourceType(StrEnum):
    LECTURE = "lecture"
    TEXTBOOK = "textbook"
    MANUAL = "manual"
    CONJECTURE = "conjecture"
    DERIVED = "derived"


class ImportedBy(StrEnum):
    COWORK = "cowork"
    MANUAL = "manual"


# ────── Nested models ──────

def _now() -> datetime:
    return datetime.now(UTC)


def _validate_id(v: str) -> str:
    if not v or v.strip() != v or " " in v or any(c in v for c in "/\\:*?\"<>|"):
        raise ValueError(f"Invalid id: {v!r}")
    return v


class Relation(BaseModel):
    """One side of a relation-claim. Used when Claim.kind == RELATION."""
    role: str
    claim_id: str


class Source(BaseModel):
    """Provenance — where this claim/proof originated.

    The seam that makes ingest-from-anywhere (lectures, textbooks, Cowork, manual)
    a uniform operation. Add new SourceType values without schema migration.
    """
    model_config = ConfigDict(use_enum_values=True)

    type: SourceType
    ref: str
    imported_at: datetime = Field(default_factory=_now)
    imported_by: ImportedBy = ImportedBy.MANUAL
    confidence: Optional[float] = None
    raw_excerpt: Optional[str] = None


# ────── Top-level entities ──────

class Claim(BaseModel):
    """A unit of mathematical knowledge.

    Relations between claims (A ⇒ B, A ⇔ B, ...) are themselves Claims with
    kind=RELATION, relates_to=[Relation(...)], relation_kind=IMPLIES/EQUIVALENCE/...
    This preserves the "relations as claims" invariant from the design.
    """
    model_config = ConfigDict(use_enum_values=True)

    id: str
    statement: str
    kind: Kind
    status: Status = Status.DRAFT

    course: Optional[str] = None
    topic: Optional[str] = None
    notes: Optional[str] = None

    relates_to: Optional[list[Relation]] = None
    relation_kind: Optional[RelationKind] = None

    source: Optional[Source] = None

    date_added: datetime = Field(default_factory=_now)
    date_canonized: Optional[datetime] = None
    schema_version: int = CURRENT_SCHEMA_VERSION

    @field_validator("id")
    @classmethod
    def _check_id(cls, v: str) -> str:
        return _validate_id(v)


class Proof(BaseModel):
    """A proof of a claim. A claim may have multiple proofs;
    is_canonical=True marks the one used for cycle detection and status propagation.
    """
    model_config = ConfigDict(use_enum_values=True)

    id: str
    claim_id: str
    body: str
    method: ProofMethod = ProofMethod.INFORMAL
    status: ProofStatus = ProofStatus.DRAFT
    dependencies: list[str] = Field(default_factory=list)
    is_canonical: bool = False
    notes: Optional[str] = None
    source: Optional[Source] = None

    date_added: datetime = Field(default_factory=_now)
    schema_version: int = CURRENT_SCHEMA_VERSION

    @field_validator("id")
    @classmethod
    def _check_id(cls, v: str) -> str:
        return _validate_id(v)


class Course(BaseModel):
    """A course context. Determines what claims are available to cite within this course."""
    id: str
    name: str
    prerequisites: list[str] = Field(default_factory=list)
    notation: Optional[dict] = None
    allowed_claims: Optional[list[str]] = None
    schema_version: int = CURRENT_SCHEMA_VERSION

    @field_validator("id")
    @classmethod
    def _check_id(cls, v: str) -> str:
        return _validate_id(v)


# ────── Verification ──────

class Verdict(BaseModel):
    success: bool
    verifier: str
    notes: Optional[str] = None
    verified_at: datetime = Field(default_factory=_now)


# ────── Batch ingestion (Cowork & other importers) ──────

class IngestBatch(BaseModel):
    """A batch of related claims/proofs/courses from one source.

    Cowork's lecture plugin sends one of these per session. The DAG system
    persists everything in draft status with the shared source provenance.
    """
    source: Source
    claims: list[Claim] = Field(default_factory=list)
    proofs: list[Proof] = Field(default_factory=list)
    courses: list[Course] = Field(default_factory=list)


class IngestReceipt(BaseModel):
    accepted_claims: list[str]
    accepted_proofs: list[str]
    rejected: list[dict]
    review_url: str
