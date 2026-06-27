"""Shared FastAPI dependencies.

``get_current_user`` is a stub today (single hardcoded user). When the system
goes multi-user, only this function changes; routes that depend on it are not
touched.
"""
from __future__ import annotations

from pathlib import Path
from typing import Generator

from fastapi import Request

from storage import index


def get_data_dir(request: Request) -> Path:
    return request.app.state.data_dir


def get_db_path(request: Request) -> Path:
    return request.app.state.db_path


def get_db(request: Request) -> Generator:
    conn = index.open_db(request.app.state.db_path)
    try:
        yield conn
    finally:
        conn.close()


def get_current_user() -> dict:
    return {"id": "elad", "name": "Elad"}
