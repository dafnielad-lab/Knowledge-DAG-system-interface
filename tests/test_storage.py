"""Storage roundtrip tests including Hebrew + LaTeX preservation."""
from pathlib import Path

from core.models import Claim, Course, Proof, Source
from storage import files, index


def test_claim_roundtrip_hebrew_latex(tmp_data_dir: Path):
    c = Claim(
        id="thm_test",
        statement=r"לכל $\epsilon > 0$ קיים $\delta > 0$ כך ש: $|x - x_0| < \delta$",
        kind="theorem",
        course="calc_1",
        topic="רציפות",
        source=Source(type="manual", ref="manual_test"),
    )
    files.save_claim(c, tmp_data_dir)
    loaded = files.load_claim(tmp_data_dir, "thm_test")
    assert loaded is not None
    assert loaded.statement == c.statement
    assert loaded.topic == "רציפות"
    assert loaded.source.ref == "manual_test"


def test_proof_roundtrip(tmp_data_dir: Path):
    p = Proof(
        id="prf_test",
        claim_id="thm_test",
        body=r"הוכחה: לפי האקסיומה $\forall x \in \mathbb{R}$ ...",
        method="informal",
        dependencies=["ax_one", "ax_two"],
        is_canonical=True,
    )
    files.save_proof(p, tmp_data_dir)
    loaded = files.load_proof(tmp_data_dir, "prf_test")
    assert loaded is not None
    assert loaded.body == p.body
    assert loaded.dependencies == ["ax_one", "ax_two"]
    assert loaded.is_canonical


def test_course_roundtrip(tmp_data_dir: Path):
    c = Course(id="logic_1", name="לוגיקה 1", prerequisites=["math_intro"])
    files.save_course(c, tmp_data_dir)
    loaded = files.load_course(tmp_data_dir, "logic_1")
    assert loaded is not None
    assert loaded.name == "לוגיקה 1"
    assert loaded.prerequisites == ["math_intro"]


def test_index_search_finds_hebrew_and_english(tmp_data_dir: Path, tmp_db_path: Path):
    c1 = Claim(id="thm_continuity", statement="A function f is continuous at x0 if...",
               kind="theorem", topic="continuity")
    c2 = Claim(id="thm_retzifut", statement="פונקציה f רציפה ב-$x_0$ אם...",
               kind="theorem", topic="רציפות")
    files.save_claim(c1, tmp_data_dir)
    files.save_claim(c2, tmp_data_dir)

    index.rebuild_index(tmp_data_dir, tmp_db_path)
    conn = index.open_db(tmp_db_path)
    try:
        assert index.search_claim_ids(conn, q="continuous") == ["thm_continuity"]
        # Hebrew search
        results = index.search_claim_ids(conn, q="פונקציה")
        assert "thm_retzifut" in results
    finally:
        conn.close()
