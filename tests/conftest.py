"""Pytest fixtures — a fresh temp data dir + index DB per test."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from fastapi.templating import Jinja2Templates

# Ensure project root on path so `from core...` works under pytest
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


@pytest.fixture
def tmp_data_dir(tmp_path: Path) -> Path:
    d = tmp_path / "data"
    (d / "claims").mkdir(parents=True)
    (d / "proofs").mkdir(parents=True)
    (d / "courses").mkdir(parents=True)
    (d / "SCHEMA_VERSION").write_text("1\n", encoding="utf-8")
    return d


@pytest.fixture
def tmp_db_path(tmp_path: Path) -> Path:
    return tmp_path / "index.db"


@pytest.fixture
def client(tmp_data_dir: Path, tmp_db_path: Path) -> TestClient:
    """A FastAPI TestClient pointed at a fresh data dir + db."""
    import app as app_module
    from storage import index

    # Build app fresh (so lifespan picks up our temp paths)
    test_app = app_module.app
    test_app.state.data_dir = tmp_data_dir
    test_app.state.db_path = tmp_db_path
    test_app.state.templates = Jinja2Templates(directory=str(app_module.TEMPLATES_DIR))

    # Build a fresh empty index
    index.rebuild_index(tmp_data_dir, tmp_db_path)

    with TestClient(test_app) as c:
        yield c
