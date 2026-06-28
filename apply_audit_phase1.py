"""Apply the workflow-generated audit-fix plan to the file store.

Reads the workflow's JSON output (new_claims + proof_patches + cycle_fixes),
then writes claims/overwrites proofs accordingly. Idempotent w.r.t. content —
re-running over the same input is safe (claims that already match are no-ops
at the filesystem level).

Run from the project root:
    python apply_audit_phase1.py path/to/workflow_output.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from core.models import Claim, Proof
from storage import files


DATA = ROOT / "data"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def apply(output_path: Path) -> None:
    payload = json.loads(output_path.read_text(encoding="utf-8"))
    result = payload["result"]

    # ── 1. New claims ──
    n_claim_created = 0
    n_claim_skipped = 0
    n_proof_for_new_claim = 0

    for c in result["new_claims"]:
        cid = c["id"]
        existing = files.load_claim(DATA, cid)
        kind = c.get("kind") or ("axiom" if c.get("is_axiom") else "theorem")

        claim_obj = Claim(
            id=cid,
            kind=kind,
            status="canonical",
            course=c["course"],
            topic=c["topic"],
            statement=c["statement"],
            date_added=now_iso() if existing is None else (existing.date_added or now_iso()),
        )
        files.save_claim(claim_obj, DATA)
        if existing is None:
            n_claim_created += 1
        else:
            n_claim_skipped += 1

        # Proof for the new claim (axioms don't need one)
        if not c.get("is_axiom") and c.get("proof_body"):
            pid = f"prf_{cid[len('thm_'):] if cid.startswith('thm_') else cid[len('def_'):] if cid.startswith('def_') else cid}"
            proof_obj = Proof(
                id=pid,
                claim_id=cid,
                method="informal",
                status="reviewed",
                is_canonical=True,
                dependencies=c.get("proof_dependencies", []),
                body=c["proof_body"],
            )
            files.save_proof(proof_obj, DATA)
            n_proof_for_new_claim += 1

    # ── 2. Proof patches (overwrites) ──
    n_patches_applied = 0
    for p in result["proof_patches"]:
        proof_obj = Proof(
            id=p["proof_id"],
            claim_id=p["claim_id"],
            method="informal",
            status="reviewed",
            is_canonical=True,
            dependencies=p["dependencies"],
            body=p["body"],
        )
        files.save_proof(proof_obj, DATA)
        n_patches_applied += 1

    # ── 3. Cycle fixes (more proof overwrites) ──
    n_cycles_applied = 0
    for cf in result.get("cycle_fixes", []):
        if cf.get("unable"):
            continue
        proof_obj = Proof(
            id=cf["proof_id"],
            claim_id=cf["claim_id"],
            method="informal",
            status="reviewed",
            is_canonical=True,
            dependencies=cf["dependencies"],
            body=cf["body"],
        )
        files.save_proof(proof_obj, DATA)
        n_cycles_applied += 1

    print(f"Claims created: {n_claim_created} (skipped {n_claim_skipped} existing)")
    print(f"Proofs for new claims: {n_proof_for_new_claim}")
    print(f"Proof patches applied: {n_patches_applied}")
    print(f"Cycle fix proofs applied: {n_cycles_applied}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    apply(Path(sys.argv[1]))
