"""FastAPI entry point.

Startup:
  • Resolve data dir and db path
  • Rebuild SQLite index from files if stale
  • Mount API routers, web routers, templates, static
"""
from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api import claims as api_claims
from api import courses as api_courses
from api import cowork as api_cowork
from api import proofs as api_proofs
from storage import index
from web import filters as web_filters
from web import ui as web_ui
from web import views as web_views


HERE = Path(__file__).resolve().parent
DATA_DIR = HERE / "data"
DB_PATH = HERE / "index.db"
TEMPLATES_DIR = HERE / "web" / "templates"
STATIC_DIR = HERE / "web" / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Tests can preset these on app.state; otherwise we use the project defaults.
    data_dir: Path = getattr(app.state, "data_dir", DATA_DIR)
    db_path: Path = getattr(app.state, "db_path", DB_PATH)

    data_dir.mkdir(parents=True, exist_ok=True)
    (data_dir / "claims").mkdir(exist_ok=True)
    (data_dir / "proofs").mkdir(exist_ok=True)
    (data_dir / "courses").mkdir(exist_ok=True)
    if not (data_dir / "SCHEMA_VERSION").exists():
        (data_dir / "SCHEMA_VERSION").write_text("1\n", encoding="utf-8")
    rebuilt = index.rebuild_if_stale(data_dir, db_path)
    if rebuilt:
        print(f"[startup] rebuilt index at {db_path}")
    app.state.data_dir = data_dir
    app.state.db_path = db_path
    templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
    web_filters.register(templates.env)
    app.state.templates = templates
    yield


app = FastAPI(title="Knowledge DAG", version="0.1.0", lifespan=lifespan)

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# JSON API
app.include_router(api_claims.router)
app.include_router(api_proofs.router)
app.include_router(api_courses.router)
app.include_router(api_cowork.router)

# HTML views + form-submit routes
app.include_router(web_views.router)
app.include_router(web_ui.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=False)
