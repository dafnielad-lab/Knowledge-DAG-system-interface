"""HTTP Basic Auth middleware — protects every request behind a username/password.

Credentials come from environment variables (``AUTH_USERNAME`` / ``AUTH_PASSWORD``).
If either is unset, the middleware is a no-op — keeps local development frictionless.
On a public deploy (Render, etc.) you set both env vars and every request is gated.

Why middleware instead of FastAPI Depends:
  • Catches everything, including static files and unmatched routes.
  • Doesn't require touching every route handler.
  • Easy to enable/disable via env vars without code changes.

Static asset paths (/static/*) and favicon are explicitly exempt so the browser
can display the login prompt correctly (otherwise CSS loads also pop the prompt).
"""
from __future__ import annotations

import base64
import os
import secrets

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


_EXEMPT_PREFIXES = ("/static/", "/favicon")


class BasicAuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, username: str | None = None, password: str | None = None,
                 realm: str = "Knowledge DAG"):
        super().__init__(app)
        self.username = username or ""
        self.password = password or ""
        self.realm = realm

    async def dispatch(self, request, call_next):
        # No credentials configured → pass-through (local dev mode).
        if not self.username or not self.password:
            return await call_next(request)

        # Static assets are exempt so the browser can paint the login dialog.
        path = request.url.path
        if any(path.startswith(p) for p in _EXEMPT_PREFIXES):
            return await call_next(request)

        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Basic "):
            return self._unauthorized()

        try:
            decoded = base64.b64decode(auth_header[6:]).decode("utf-8", errors="strict")
            user, sep, pwd = decoded.partition(":")
            if not sep:
                return self._unauthorized()
        except Exception:
            return self._unauthorized()

        # Constant-time comparison to avoid timing side channels.
        user_ok = secrets.compare_digest(user, self.username)
        pass_ok = secrets.compare_digest(pwd, self.password)
        if not (user_ok and pass_ok):
            return self._unauthorized()

        return await call_next(request)

    def _unauthorized(self) -> Response:
        return Response(
            content="Authentication required.",
            status_code=401,
            headers={"WWW-Authenticate": f'Basic realm="{self.realm}"'},
        )


def install(app) -> None:
    """Register the auth middleware on the given FastAPI app, reading env vars."""
    app.add_middleware(
        BasicAuthMiddleware,
        username=os.environ.get("AUTH_USERNAME"),
        password=os.environ.get("AUTH_PASSWORD"),
    )
