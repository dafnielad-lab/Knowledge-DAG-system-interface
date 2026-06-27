"""Effective-status computation — propagate dependency statuses through the DAG.

The stored ``status`` on a Claim is local. The *effective* status accounts for the
transitive closure of canonical-proof dependencies. The rules from the design doc:

  • If any transitive dependency is ``conjectured`` → effective is "proved modulo X"
  • Otherwise → effective equals the stored status

This is rendered as: green (canonical/formally_verified), amber (anything modulo
a conjecture or in early review), red (conjectured itself).
"""
from __future__ import annotations

from pydantic import BaseModel, Field

from .dag import DepMap, transitive_closure
from .models import Status


class EffectiveStatus(BaseModel):
    base: Status
    modulo: list[str] = Field(default_factory=list)

    @property
    def is_modulo(self) -> bool:
        return bool(self.modulo) and self.base != Status.CONJECTURED

    @property
    def color(self) -> str:
        """For UI hint — caller maps to actual colors."""
        if self.base == Status.CONJECTURED:
            return "red"
        if self.is_modulo:
            return "amber"
        if self.base in (Status.CANONICAL, Status.FORMALLY_VERIFIED):
            return "green"
        return "amber"


def effective_status(
    claim_id: str,
    status_map: dict[str, Status],
    dep_map: DepMap,
) -> EffectiveStatus:
    """Compute the effective status of a claim considering transitive dependencies."""
    base = status_map.get(claim_id, Status.DRAFT)
    if base == Status.CONJECTURED:
        return EffectiveStatus(base=base, modulo=[])
    closure = transitive_closure(claim_id, dep_map)
    conjectures = sorted(
        cid for cid in closure if status_map.get(cid) == Status.CONJECTURED
    )
    return EffectiveStatus(base=base, modulo=conjectures)
