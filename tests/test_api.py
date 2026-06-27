"""End-to-end API tests via TestClient — exercises the full stack:
files <-> SQLite index <-> FastAPI <-> Pydantic.
"""
from fastapi.testclient import TestClient


def _create_claim(client, id_, kind="axiom", statement="x", **extra):
    return client.post("/api/claims", json={
        "id": id_, "kind": kind, "statement": statement, **extra,
    })


def test_create_and_get_claim(client: TestClient):
    r = _create_claim(client, "ax_test", statement="Every set is a set.")
    assert r.status_code == 201, r.text
    r = client.get("/api/claims/ax_test")
    assert r.status_code == 200
    data = r.json()
    assert data["claim"]["id"] == "ax_test"
    assert data["claim"]["kind"] == "axiom"
    assert data["proof_ids"] == []


def test_duplicate_claim_rejected(client: TestClient):
    assert _create_claim(client, "ax_dup").status_code == 201
    assert _create_claim(client, "ax_dup").status_code == 409


def test_proof_with_cycle_rejected(client: TestClient):
    # Build: a (axiom), b (theorem depending on a)
    assert _create_claim(client, "ax_a").status_code == 201
    assert _create_claim(client, "thm_b", kind="theorem").status_code == 201

    # Proof of b citing a → fine
    r = client.post("/api/proofs", json={
        "id": "prf_b", "claim_id": "thm_b", "body": "From a.",
        "dependencies": ["ax_a"], "is_canonical": True,
    })
    assert r.status_code == 201, r.text

    # Now: proof of a citing b → cycle (a→b→a)
    r = client.post("/api/proofs", json={
        "id": "prf_a", "claim_id": "ax_a", "body": "From b.",
        "dependencies": ["thm_b"], "is_canonical": True,
    })
    assert r.status_code == 400
    assert "cycle" in r.text.lower()


def test_cannot_delete_cited_claim(client: TestClient):
    _create_claim(client, "ax_x")
    _create_claim(client, "thm_y", kind="theorem")
    client.post("/api/proofs", json={
        "id": "prf_y", "claim_id": "thm_y", "body": "...",
        "dependencies": ["ax_x"], "is_canonical": True,
    })
    r = client.delete("/api/claims/ax_x")
    assert r.status_code == 409


def test_traceability(client: TestClient):
    _create_claim(client, "ax_1")
    _create_claim(client, "ax_2")
    _create_claim(client, "lem_3", kind="lemma")
    _create_claim(client, "thm_4", kind="theorem")
    client.post("/api/proofs", json={
        "id": "prf_lem", "claim_id": "lem_3", "body": "from axioms",
        "dependencies": ["ax_1", "ax_2"], "is_canonical": True,
    })
    client.post("/api/proofs", json={
        "id": "prf_thm", "claim_id": "thm_4", "body": "from lemma",
        "dependencies": ["lem_3"], "is_canonical": True,
    })
    r = client.get("/api/claims/thm_4/traceability")
    assert r.status_code == 200
    tree = r.json()
    assert tree["id"] == "thm_4"
    # Walks: thm_4 → lem_3 → ax_1, ax_2
    assert len(tree["children"]) == 1
    assert tree["children"][0]["id"] == "lem_3"
    leaf_ids = {c["id"] for c in tree["children"][0]["children"]}
    assert leaf_ids == {"ax_1", "ax_2"}


def test_cowork_ingest(client: TestClient):
    batch = {
        "source": {
            "type": "lecture",
            "ref": "lecture_2026_06_27_logic",
            "imported_by": "cowork",
        },
        "claims": [
            {"id": "ax_lec1", "kind": "axiom", "statement": "P or not P"},
            {"id": "thm_lec1", "kind": "theorem", "statement": "(P→Q)→(¬Q→¬P)"},
        ],
        "proofs": [
            {"id": "prf_lec1", "claim_id": "thm_lec1",
             "body": "Contrapositive.", "dependencies": ["ax_lec1"]},
        ],
        "courses": [],
    }
    r = client.post("/api/cowork/ingest", json=batch)
    assert r.status_code == 200, r.text
    receipt = r.json()
    assert set(receipt["accepted_claims"]) == {"ax_lec1", "thm_lec1"}
    assert receipt["accepted_proofs"] == ["prf_lec1"]
    assert receipt["rejected"] == []
    assert "lecture_2026_06_27_logic" in receipt["review_url"]

    # Verify provenance was attached + status is draft
    r = client.get("/api/claims/thm_lec1")
    data = r.json()
    assert data["claim"]["status"] == "draft"
    assert data["claim"]["source"]["ref"] == "lecture_2026_06_27_logic"
    assert data["claim"]["source"]["imported_by"] == "cowork"

    # Filter by source_ref → drafts review queue
    r = client.get("/api/claims?source_ref=lecture_2026_06_27_logic&status=draft")
    assert r.status_code == 200
    found_ids = {c["id"] for c in r.json()}
    assert found_ids == {"ax_lec1", "thm_lec1"}


def test_approve_promotes_to_canonical(client: TestClient):
    _create_claim(client, "thm_to_approve", kind="theorem")
    r = client.post("/api/claims/thm_to_approve/approve")
    assert r.status_code == 200
    assert r.json()["status"] == "canonical"
    assert r.json()["date_canonized"] is not None


def test_search_hebrew(client: TestClient):
    _create_claim(client, "thm_heb", kind="theorem",
                  statement="פונקציה רציפה בכל קטע סגור היא חסומה")
    r = client.get("/api/claims?q=רציפה")
    assert r.status_code == 200
    ids = {c["id"] for c in r.json()}
    assert "thm_heb" in ids


def test_index_view_renders(client: TestClient):
    """The HTML index page should render (status 200, contains brand)."""
    r = client.get("/")
    assert r.status_code == 200
    assert "Knowledge" in r.text
    assert 'dir="rtl"' in r.text
