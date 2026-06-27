"""SQLite cache built from the file-based source of truth.

The index is fully rebuildable from files — if it gets corrupted or schema
changes, delete it and it'll be recreated on startup.

Queries return IDs; callers reload full objects from files. This keeps the
schema thin and avoids drift between SQLite and file representations.

FTS5 uses unicode61 tokenizer, which handles Hebrew and English in the same
index without configuration.
"""
from __future__ import annotations

import sqlite3
from pathlib import Path

from core.models import Claim, Course, Proof

from . import files


SCHEMA = """
CREATE TABLE IF NOT EXISTS meta (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS claims (
    id TEXT PRIMARY KEY,
    statement TEXT NOT NULL,
    kind TEXT NOT NULL,
    status TEXT NOT NULL,
    course TEXT,
    topic TEXT,
    notes TEXT,
    relation_kind TEXT,
    source_type TEXT,
    source_ref TEXT,
    source_imported_by TEXT,
    date_added TEXT,
    date_canonized TEXT
);

CREATE INDEX IF NOT EXISTS idx_claims_course ON claims(course);
CREATE INDEX IF NOT EXISTS idx_claims_status ON claims(status);
CREATE INDEX IF NOT EXISTS idx_claims_kind ON claims(kind);
CREATE INDEX IF NOT EXISTS idx_claims_source_ref ON claims(source_ref);

CREATE TABLE IF NOT EXISTS proofs (
    id TEXT PRIMARY KEY,
    claim_id TEXT NOT NULL,
    body TEXT NOT NULL,
    method TEXT NOT NULL,
    status TEXT NOT NULL,
    is_canonical INTEGER NOT NULL,
    source_type TEXT,
    source_ref TEXT,
    date_added TEXT
);

CREATE INDEX IF NOT EXISTS idx_proofs_claim ON proofs(claim_id);
CREATE INDEX IF NOT EXISTS idx_proofs_canonical ON proofs(is_canonical);

CREATE TABLE IF NOT EXISTS proof_deps (
    proof_id TEXT NOT NULL,
    dep_claim_id TEXT NOT NULL,
    PRIMARY KEY(proof_id, dep_claim_id)
);

CREATE INDEX IF NOT EXISTS idx_pdeps_dep ON proof_deps(dep_claim_id);

CREATE TABLE IF NOT EXISTS courses (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS course_prereqs (
    course_id TEXT NOT NULL,
    prereq_id TEXT NOT NULL,
    PRIMARY KEY(course_id, prereq_id)
);

CREATE VIRTUAL TABLE IF NOT EXISTS claims_fts USING fts5(
    id UNINDEXED,
    statement,
    notes,
    topic,
    tokenize='unicode61 remove_diacritics 2'
);
"""


def open_db(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    return conn


# ────── Rebuild lifecycle ──────

def rebuild_if_stale(data_dir: Path, db_path: Path) -> bool:
    """Returns True if a rebuild occurred."""
    if db_path.exists():
        try:
            conn = open_db(db_path)
            try:
                row = conn.execute("SELECT value FROM meta WHERE key='schema_version'").fetchone()
                stored_v = int(row[0]) if row else -1
                row = conn.execute("SELECT value FROM meta WHERE key='data_mtime'").fetchone()
                stored_mtime = float(row[0]) if row else 0.0
            finally:
                conn.close()
            on_disk_v = files.read_schema_version(data_dir)
            on_disk_mtime = files.latest_mtime(data_dir)
            if stored_v == on_disk_v and stored_mtime >= on_disk_mtime:
                return False
        except sqlite3.DatabaseError:
            pass  # fall through to rebuild
    rebuild_index(data_dir, db_path)
    return True


def rebuild_index(data_dir: Path, db_path: Path) -> None:
    if db_path.exists():
        db_path.unlink()
    conn = open_db(db_path)
    try:
        conn.executescript(SCHEMA)
        claims, proofs, courses = files.scan_data_dir(data_dir)
        for c in claims:
            _insert_claim(conn, c)
        for p in proofs:
            _insert_proof(conn, p)
        for course in courses:
            _insert_course(conn, course)
        conn.execute("INSERT INTO meta(key, value) VALUES ('schema_version', ?)",
                     (str(files.read_schema_version(data_dir)),))
        conn.execute("INSERT INTO meta(key, value) VALUES ('data_mtime', ?)",
                     (str(files.latest_mtime(data_dir)),))
        conn.commit()
    finally:
        conn.close()


def touch_mtime(conn: sqlite3.Connection, data_dir: Path) -> None:
    """After file changes, update the stored mtime so we don't trigger a needless rebuild."""
    conn.execute(
        "INSERT OR REPLACE INTO meta(key, value) VALUES ('data_mtime', ?)",
        (str(files.latest_mtime(data_dir)),),
    )
    conn.commit()


# ────── Incremental upsert ──────

def upsert_claim(conn: sqlite3.Connection, c: Claim) -> None:
    conn.execute("DELETE FROM claims WHERE id = ?", (c.id,))
    conn.execute("DELETE FROM claims_fts WHERE id = ?", (c.id,))
    _insert_claim(conn, c)
    conn.commit()


def upsert_proof(conn: sqlite3.Connection, p: Proof) -> None:
    conn.execute("DELETE FROM proof_deps WHERE proof_id = ?", (p.id,))
    conn.execute("DELETE FROM proofs WHERE id = ?", (p.id,))
    _insert_proof(conn, p)
    conn.commit()


def upsert_course(conn: sqlite3.Connection, c: Course) -> None:
    conn.execute("DELETE FROM course_prereqs WHERE course_id = ?", (c.id,))
    conn.execute("DELETE FROM courses WHERE id = ?", (c.id,))
    _insert_course(conn, c)
    conn.commit()


def remove_claim(conn: sqlite3.Connection, claim_id: str) -> None:
    conn.execute("DELETE FROM claims WHERE id = ?", (claim_id,))
    conn.execute("DELETE FROM claims_fts WHERE id = ?", (claim_id,))
    conn.commit()


def remove_proof(conn: sqlite3.Connection, proof_id: str) -> None:
    conn.execute("DELETE FROM proof_deps WHERE proof_id = ?", (proof_id,))
    conn.execute("DELETE FROM proofs WHERE id = ?", (proof_id,))
    conn.commit()


def _insert_claim(conn: sqlite3.Connection, c: Claim) -> None:
    src = c.source
    conn.execute(
        """INSERT INTO claims(id, statement, kind, status, course, topic, notes,
                              relation_kind, source_type, source_ref, source_imported_by,
                              date_added, date_canonized)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (c.id, c.statement, c.kind, c.status, c.course, c.topic, c.notes,
         c.relation_kind, src.type if src else None, src.ref if src else None,
         src.imported_by if src else None,
         c.date_added.isoformat() if c.date_added else None,
         c.date_canonized.isoformat() if c.date_canonized else None),
    )
    conn.execute(
        "INSERT INTO claims_fts(id, statement, notes, topic) VALUES (?,?,?,?)",
        (c.id, c.statement, c.notes or "", c.topic or ""),
    )


def _insert_proof(conn: sqlite3.Connection, p: Proof) -> None:
    src = p.source
    conn.execute(
        """INSERT INTO proofs(id, claim_id, body, method, status, is_canonical,
                              source_type, source_ref, date_added)
           VALUES (?,?,?,?,?,?,?,?,?)""",
        (p.id, p.claim_id, p.body, p.method, p.status, int(p.is_canonical),
         src.type if src else None, src.ref if src else None,
         p.date_added.isoformat() if p.date_added else None),
    )
    for dep in p.dependencies:
        conn.execute(
            "INSERT OR IGNORE INTO proof_deps(proof_id, dep_claim_id) VALUES (?,?)",
            (p.id, dep),
        )


def _insert_course(conn: sqlite3.Connection, c: Course) -> None:
    conn.execute("INSERT INTO courses(id, name) VALUES (?,?)", (c.id, c.name))
    for prereq in c.prerequisites:
        conn.execute(
            "INSERT OR IGNORE INTO course_prereqs(course_id, prereq_id) VALUES (?,?)",
            (c.id, prereq),
        )


# ────── Queries ──────

def search_claim_ids(
    conn: sqlite3.Connection,
    q: str | None = None,
    courses: list[str] | None = None,
    statuses: list[str] | None = None,
    kinds: list[str] | None = None,
    topics: list[str] | None = None,
    source_ref: str | None = None,
    limit: int = 100,
    offset: int = 0,
) -> list[str]:
    """Returns matching claim IDs (paged). Filters accept lists — match ANY (OR)
    within a filter, AND across filters."""
    sql, params = _build_search_sql(q, courses, statuses, kinds, topics, source_ref)
    sql += " ORDER BY c.date_added DESC LIMIT ? OFFSET ?"
    params.extend([limit, offset])
    return [row[0] for row in conn.execute(sql, params)]


def count_claims(
    conn: sqlite3.Connection,
    q: str | None = None,
    courses: list[str] | None = None,
    statuses: list[str] | None = None,
    kinds: list[str] | None = None,
    topics: list[str] | None = None,
    source_ref: str | None = None,
) -> int:
    """Counts claims matching the same filters as ``search_claim_ids`` (no paging)."""
    sql, params = _build_search_sql(q, courses, statuses, kinds, topics, source_ref)
    # Wrap as count
    sql = "SELECT COUNT(*) FROM (" + sql + ")"
    return conn.execute(sql, params).fetchone()[0]


def all_topics(conn: sqlite3.Connection) -> list[str]:
    """Distinct non-null topics for the topic filter dropdown."""
    return [row[0] for row in conn.execute(
        "SELECT DISTINCT topic FROM claims WHERE topic IS NOT NULL AND topic != '' ORDER BY topic"
    )]


def _in_clause(values: list[str] | None, column: str) -> tuple[str, list]:
    """Build a SQL `column IN (?,?,…)` fragment + its params, or empty if no values."""
    if not values:
        return "", []
    placeholder = ",".join("?" * len(values))
    return f" AND {column} IN ({placeholder})", list(values)


def _build_search_sql(q, courses, statuses, kinds, topics, source_ref) -> tuple[str, list]:
    if q:
        sql_parts = [
            "SELECT c.id FROM claims c",
            "JOIN claims_fts f ON c.id = f.id",
            "WHERE claims_fts MATCH ?",
        ]
        params: list = [q]
    else:
        sql_parts = ["SELECT c.id FROM claims c WHERE 1=1"]
        params = []

    for vals, col in [(courses, "c.course"), (statuses, "c.status"),
                       (kinds, "c.kind"), (topics, "c.topic")]:
        frag, p = _in_clause(vals, col)
        if frag:
            sql_parts.append(frag.strip())
            params.extend(p)

    if source_ref is not None:
        sql_parts.append("AND c.source_ref = ?")
        params.append(source_ref)

    return " ".join(sql_parts), params


def get_dep_map(conn: sqlite3.Connection) -> dict[str, list[str]]:
    """Canonical-proof dependency map for the whole DAG."""
    dep_map: dict[str, list[str]] = {}
    rows = conn.execute(
        """SELECT p.claim_id, pd.dep_claim_id
           FROM proofs p JOIN proof_deps pd ON p.id = pd.proof_id
           WHERE p.is_canonical = 1"""
    )
    for row in rows:
        dep_map.setdefault(row[0], []).append(row[1])
    return dep_map


def get_status_map(conn: sqlite3.Connection) -> dict[str, str]:
    return {row[0]: row[1] for row in conn.execute("SELECT id, status FROM claims")}


def get_claim_to_course(conn: sqlite3.Connection) -> dict[str, str | None]:
    return {row[0]: row[1] for row in conn.execute("SELECT id, course FROM claims")}


def get_proof_ids_for(conn: sqlite3.Connection, claim_id: str) -> list[str]:
    return [row[0] for row in conn.execute(
        "SELECT id FROM proofs WHERE claim_id = ? ORDER BY is_canonical DESC, date_added",
        (claim_id,))]


def get_canonical_proof_id(conn: sqlite3.Connection, claim_id: str) -> str | None:
    row = conn.execute(
        "SELECT id FROM proofs WHERE claim_id = ? AND is_canonical = 1 LIMIT 1",
        (claim_id,)).fetchone()
    return row[0] if row else None


def get_citing_proofs(conn: sqlite3.Connection, claim_id: str) -> list[tuple[str, str]]:
    """[(proof_id, claim_id_being_proved)] for proofs that cite claim_id as a dependency."""
    return [(row[0], row[1]) for row in conn.execute(
        """SELECT p.id, p.claim_id
           FROM proofs p JOIN proof_deps pd ON p.id = pd.proof_id
           WHERE pd.dep_claim_id = ?""", (claim_id,))]


def all_claim_ids(conn: sqlite3.Connection) -> list[str]:
    return [row[0] for row in conn.execute("SELECT id FROM claims ORDER BY id")]


def all_course_ids(conn: sqlite3.Connection) -> list[str]:
    return [row[0] for row in conn.execute("SELECT id FROM courses ORDER BY id")]
