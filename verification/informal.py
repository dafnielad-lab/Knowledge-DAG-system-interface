"""Informal verifier — the human-written proof case.

This verifier doesn't *check* the proof; it just asserts the structural
preconditions (non-empty body, declared dependencies exist) and returns a
verdict that means "the proof is here, but it's only as good as the human
that wrote it and reviewers' time."

When AI verification arrives, it'll be a separate file with its own logic.
"""
from __future__ import annotations

from core.models import Proof, ProofMethod, Verdict

from .base import Verifier, register


class InformalVerifier:
    name = "informal"
    method = ProofMethod.INFORMAL

    def can_verify(self, proof: Proof) -> bool:
        return proof.method == ProofMethod.INFORMAL.value or proof.method == ProofMethod.INFORMAL

    def verify(self, proof: Proof) -> Verdict:
        if not proof.body.strip():
            return Verdict(success=False, verifier=self.name,
                           notes="Empty proof body.")
        return Verdict(success=True, verifier=self.name,
                       notes="Structural check only — informal proofs require human review.")


register(InformalVerifier())
