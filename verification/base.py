"""Verifier plugin protocol — the seam for future verification methods.

Adding Lean / AI / SAT / omega / groebner / truth_table verification is a matter
of dropping a new file in this directory that implements ``Verifier`` and
registering it in ``REGISTRY``. The rest of the system never changes.
"""
from __future__ import annotations

from typing import Protocol, runtime_checkable

from core.models import Proof, ProofMethod, Verdict


@runtime_checkable
class Verifier(Protocol):
    """A verification strategy. Stateless; one instance can verify many proofs."""

    name: str
    method: ProofMethod

    def can_verify(self, proof: Proof) -> bool:
        """Does this verifier handle the given proof's method?"""
        ...

    def verify(self, proof: Proof) -> Verdict:
        """Return a Verdict. Does not raise on logical failure — sets success=False."""
        ...


REGISTRY: dict[str, Verifier] = {}


def register(verifier: Verifier) -> None:
    REGISTRY[verifier.name] = verifier


def verifier_for(method: ProofMethod | str) -> Verifier | None:
    """Find the first registered verifier whose ``method`` matches."""
    target = method.value if hasattr(method, "value") else method
    for v in REGISTRY.values():
        if v.method == target or (hasattr(v.method, "value") and v.method.value == target):
            return v
    return None
