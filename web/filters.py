"""Jinja2 template filters.

Two filters for rendering claim/proof bodies:

  render_md  — full Markdown → HTML, preserving $...$ and $$...$$ math blocks
               for KaTeX to handle client-side.
  plain_md   — strip Markdown markers for snippet/truncation display, keeping
               math delimiters untouched.

Why we protect math: Python-Markdown sees $...$ as plain text but happily
mangles content inside (e.g., underscores become italics). We stash math
blocks before rendering and restore them after.
"""
from __future__ import annotations

import re

import markdown
from markupsafe import Markup


_MATH_BLOCK = re.compile(r"(\$\$[\s\S]+?\$\$)")
_MATH_INLINE = re.compile(r"(\$(?:\\.|[^$\\])+?\$)")
_BOLD = re.compile(r"\*\*([^*\n]+?)\*\*")
_ITALIC = re.compile(r"(?<!\*)\*([^*\n]+?)\*(?!\*)")

# Leading "**name:**" prefix at the start of a statement — lets us promote the
# name into the page/card header instead of repeating it in the body.
_NAME_PREFIX = re.compile(r"^\s*\*\*([^*\n]+?)\*\*[\s:：]*", re.UNICODE)


def render_md(text: str | None) -> Markup:
    """Render Markdown to HTML, preserving math blocks for client-side KaTeX."""
    if not text:
        return Markup("")
    stash: list[str] = []

    def _save(m: re.Match) -> str:
        stash.append(m.group(0))
        return f"@@KDMATH{len(stash) - 1}@@"

    protected = _MATH_BLOCK.sub(_save, text)
    protected = _MATH_INLINE.sub(_save, protected)

    html = markdown.markdown(protected, extensions=["extra"])

    for i, chunk in enumerate(stash):
        html = html.replace(f"@@KDMATH{i}@@", chunk)
    return Markup(html)


def plain_md(text: str | None) -> str:
    """Strip Markdown markers (** and *) but leave math delimiters intact.

    Use for card snippets where we truncate before display — full HTML rendering
    would risk cutting mid-tag.
    """
    if not text:
        return ""
    s = _BOLD.sub(r"\1", text)
    s = _ITALIC.sub(r"\1", s)
    return s


def claim_name(text: str | None) -> str | None:
    """Extract a leading '**name:**' prefix from a statement, if present.

    Returns the name string (without the asterisks or trailing colon),
    or None if the statement doesn't begin with a bolded prefix.
    """
    if not text:
        return None
    m = _NAME_PREFIX.match(text)
    if not m:
        return None
    return m.group(1).strip().rstrip(":：").strip()


def claim_body(text: str | None) -> str:
    """Return the statement with the leading '**name:**' prefix stripped.

    Lets us render the name in the header row and the body separately —
    avoiding redundant repetition of the name in two places.
    """
    if not text:
        return ""
    return _NAME_PREFIX.sub("", text, count=1).lstrip()


# ─── LaTeX → Unicode for non-KaTeX surfaces (graph, plain-text tree) ───

_LATEX_REPLACEMENTS = {
    r"\cdot": "·", r"\times": "×", r"\div": "÷", r"\pm": "±", r"\mp": "∓",
    r"\geq": "≥", r"\leq": "≤", r"\neq": "≠", r"\approx": "≈", r"\equiv": "≡",
    r"\implies": "⇒", r"\iff": "⇔",
    r"\Rightarrow": "⇒", r"\Leftarrow": "⇐", r"\Leftrightarrow": "⇔",
    r"\rightarrow": "→", r"\leftarrow": "←", r"\to": "→",
    r"\infty": "∞", r"\partial": "∂", r"\nabla": "∇",
    r"\sum": "Σ", r"\prod": "Π", r"\int": "∫", r"\sqrt": "√",
    r"\alpha": "α", r"\beta": "β", r"\gamma": "γ", r"\Gamma": "Γ",
    r"\delta": "δ", r"\Delta": "Δ", r"\epsilon": "ε", r"\varepsilon": "ε",
    r"\zeta": "ζ", r"\eta": "η", r"\theta": "θ", r"\Theta": "Θ",
    r"\iota": "ι", r"\kappa": "κ", r"\lambda": "λ", r"\Lambda": "Λ",
    r"\mu": "μ", r"\nu": "ν", r"\xi": "ξ", r"\pi": "π", r"\Pi": "Π",
    r"\rho": "ρ", r"\sigma": "σ", r"\Sigma": "Σ", r"\tau": "τ",
    r"\phi": "φ", r"\varphi": "φ", r"\Phi": "Φ", r"\chi": "χ",
    r"\psi": "ψ", r"\Psi": "Ψ", r"\omega": "ω", r"\Omega": "Ω",
    r"\subseteq": "⊆", r"\subset": "⊂", r"\supseteq": "⊇", r"\supset": "⊃",
    r"\cup": "∪", r"\cap": "∩", r"\setminus": "∖",
    r"\in": "∈", r"\notin": "∉", r"\emptyset": "∅", r"\varnothing": "∅",
    r"\forall": "∀", r"\exists": "∃", r"\nexists": "∄",
    r"\angle": "∠", r"\perp": "⊥", r"\parallel": "∥",
    r"\overline": "", r"\vec": "",
    r"\,": " ", r"\;": " ", r"\!": "",
    r"\left": "", r"\right": "",
}
# Sort longest-first so e.g. \Gamma matches before \gamma's prefix \g.
_LATEX_PATTERN = re.compile(
    "|".join(re.escape(k) for k in sorted(_LATEX_REPLACEMENTS, key=len, reverse=True))
)

_BRACED_COMMANDS = re.compile(r"\\(text|mathbb|mathrm|mathbf|mathit|operatorname)\{([^}]*)\}")
_FRAC = re.compile(r"\\frac\{([^}]*)\}\{([^}]*)\}")
_REMAINING_COMMAND = re.compile(r"\\([a-zA-Z]+)\*?")
_DOLLAR = re.compile(r"\$+")
_BACKSLASH_UNDERSCORE = re.compile(r"\\_")
_ESCAPED_BRACES = re.compile(r"\\([{}])")
_BRACES = re.compile(r"[{}]")
_MULTISPACE = re.compile(r"\s+")


def clean_latex_for_label(text: str | None) -> str:
    """Best-effort conversion of LaTeX in a short label to readable Unicode.

    Used in surfaces that don't render math (graph node labels, plain-text
    tree). Cards/tagline keep the raw `$...$` markers so KaTeX can render them.
    """
    if not text:
        return ""
    s = text
    s = _FRAC.sub(r"\1/\2", s)
    s = _BRACED_COMMANDS.sub(r"\2", s)
    s = _LATEX_PATTERN.sub(lambda m: _LATEX_REPLACEMENTS[m.group(0)], s)
    s = _REMAINING_COMMAND.sub(r"\1", s)
    s = _DOLLAR.sub("", s)
    s = _BACKSLASH_UNDERSCORE.sub("_", s)
    s = _ESCAPED_BRACES.sub(r"\1", s)   # \{ \} → { } (so the brace strip below removes them cleanly)
    s = _BRACES.sub("", s)
    s = _MULTISPACE.sub(" ", s).strip()
    return s


def register(jinja_env) -> None:
    """Attach filters to a Jinja2 Environment (called from app startup)."""
    jinja_env.filters["render_md"] = render_md
    jinja_env.filters["plain_md"] = plain_md
    jinja_env.filters["claim_name"] = claim_name
    jinja_env.filters["claim_body"] = claim_body
    jinja_env.filters["clean_latex_for_label"] = clean_latex_for_label
