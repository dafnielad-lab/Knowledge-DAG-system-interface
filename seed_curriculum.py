"""Seed the DAG with mathematics curriculum content.

Idempotent: re-running won't duplicate (skips items that already exist).
This script is meant to be extended incrementally — every chunk is a
self-contained block of (claims + proofs) with no orphan dependencies.

Run from the project root:
    python seed_curriculum.py
Then refresh the browser (or restart Run.bat) to see the new content.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from core.models import Claim, Course, Proof
from storage import files, index

# Big chunks live in their own modules for readability
from seed_chunk5 import COURSES as COURSES_CHUNK5, CLAIMS as CLAIMS_CHUNK5, PROOFS as PROOFS_CHUNK5
from seed_chunk6 import COURSES as COURSES_CHUNK6, CLAIMS as CLAIMS_CHUNK6, PROOFS as PROOFS_CHUNK6
from seed_chunk7 import COURSES as COURSES_CHUNK7, CLAIMS as CLAIMS_CHUNK7, PROOFS as PROOFS_CHUNK7
from seed_proofs_backfill import COURSES as COURSES_BF, CLAIMS as CLAIMS_BF, PROOFS as PROOFS_BF
from seed_chunk8 import COURSES as COURSES_CHUNK8, CLAIMS as CLAIMS_CHUNK8, PROOFS as PROOFS_CHUNK8
from seed_chunk9 import COURSES as COURSES_CHUNK9, CLAIMS as CLAIMS_CHUNK9, PROOFS as PROOFS_CHUNK9
from seed_chunk10 import COURSES as COURSES_CHUNK10, CLAIMS as CLAIMS_CHUNK10, PROOFS as PROOFS_CHUNK10
from seed_uni_courses import COURSES as COURSES_UNI, migrate_claims_to_uni_courses


DATA = ROOT / "data"
DB = ROOT / "index.db"

CANON = "canonical"


# ─────────────────────────────────────────────────────────────────
# Chunk 1 — Foundations: field axioms + first derived theorems
# ─────────────────────────────────────────────────────────────────

COURSES_CHUNK1 = [
    Course(
        id="math_foundations",
        name="יסודות המתמטיקה — אקסיומות שדה",
        prerequisites=[],
    ),
]

CLAIMS_CHUNK1 = [
    # ─── Axioms of the real-number field ───
    Claim(
        id="ax_addition_associativity",
        kind="axiom",
        status="canonical",
        course="math_foundations",
        topic="אקסיומות שדה",
        statement=r"**אסוציאטיביות חיבור:** לכל $a, b, c \in \mathbb{R}$ מתקיים $(a + b) + c = a + (b + c)$.",
    ),
    Claim(
        id="ax_addition_commutativity",
        kind="axiom",
        status="canonical",
        course="math_foundations",
        topic="אקסיומות שדה",
        statement=r"**קומוטטיביות חיבור:** לכל $a, b \in \mathbb{R}$ מתקיים $a + b = b + a$.",
    ),
    Claim(
        id="ax_additive_identity",
        kind="axiom",
        status="canonical",
        course="math_foundations",
        topic="אקסיומות שדה",
        statement=r"**איבר ניטרלי לחיבור:** קיים $0 \in \mathbb{R}$ כך שלכל $a \in \mathbb{R}$ מתקיים $a + 0 = a$.",
    ),
    Claim(
        id="ax_additive_inverse",
        kind="axiom",
        status="canonical",
        course="math_foundations",
        topic="אקסיומות שדה",
        statement=r"**איבר נגדי לחיבור:** לכל $a \in \mathbb{R}$ קיים $-a \in \mathbb{R}$ כך ש-$a + (-a) = 0$.",
    ),
    Claim(
        id="ax_multiplicative_identity",
        kind="axiom",
        status="canonical",
        course="math_foundations",
        topic="אקסיומות שדה",
        statement=r"**איבר ניטרלי לכפל:** קיים $1 \in \mathbb{R}$, $1 \neq 0$, כך שלכל $a \in \mathbb{R}$ מתקיים $a \cdot 1 = a$.",
    ),
    Claim(
        id="ax_distributive_law",
        kind="axiom",
        status="canonical",
        course="math_foundations",
        topic="אקסיומות שדה",
        statement=r"**חוק הפילוג:** לכל $a, b, c \in \mathbb{R}$ מתקיים $a \cdot (b + c) = a \cdot b + a \cdot c$.",
    ),

    # ─── First derived theorems ───
    Claim(
        id="thm_addition_cancellation",
        kind="theorem",
        status="canonical",
        course="math_foundations",
        topic="אלגברה בסיסית",
        statement=r"**צמצום בחיבור:** אם $a + b = a + c$ אז $b = c$.",
    ),
    Claim(
        id="thm_multiplication_by_zero",
        kind="theorem",
        status="canonical",
        course="math_foundations",
        topic="אלגברה בסיסית",
        statement=r"**אפס בכפל:** לכל $a \in \mathbb{R}$ מתקיים $0 \cdot a = 0$.",
    ),
    Claim(
        id="thm_multiplication_by_negative_one",
        kind="theorem",
        status="canonical",
        course="math_foundations",
        topic="אלגברה בסיסית",
        statement=r"**כפל ב-$-1$:** לכל $a \in \mathbb{R}$ מתקיים $(-1) \cdot a = -a$.",
    ),
]

PROOFS_CHUNK1 = [
    Proof(
        id="prf_addition_cancellation",
        claim_id="thm_addition_cancellation",
        method="informal",
        status="reviewed",
        is_canonical=True,
        dependencies=["ax_additive_inverse", "ax_addition_associativity", "ax_additive_identity"],
        body=(
            "נניח $a + b = a + c$. נוסיף $-a$ משמאל לשני האגפים:\n\n"
            r"$(-a) + (a + b) = (-a) + (a + c)$"
            "\n\nלפי אסוציאטיביות החיבור:\n\n"
            r"$((-a) + a) + b = ((-a) + a) + c$"
            "\n\nמהגדרת איבר נגדי, $(-a) + a = 0$ (משתמשים גם בקומוטטיביות), ולכן:\n\n"
            r"$0 + b = 0 + c$"
            "\n\nומאיבר ניטרלי לחיבור נקבל $b = c$. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_multiplication_by_zero",
        claim_id="thm_multiplication_by_zero",
        method="informal",
        status="reviewed",
        is_canonical=True,
        dependencies=["ax_additive_identity", "ax_distributive_law", "thm_addition_cancellation"],
        body=(
            "מאיבר ניטרלי לחיבור, $0 + 0 = 0$. נכפול את שני האגפים ב-$a$:\n\n"
            r"$a \cdot (0 + 0) = a \cdot 0$"
            "\n\nלפי חוק הפילוג:\n\n"
            r"$a \cdot 0 + a \cdot 0 = a \cdot 0$"
            "\n\nנכתוב את אגף ימין כ-$a \\cdot 0 + 0$ (מאיבר ניטרלי) ונקבל:\n\n"
            r"$a \cdot 0 + a \cdot 0 = a \cdot 0 + 0$"
            "\n\nמשפט הצמצום מאפשר לבטל את $a \\cdot 0$ משני האגפים:\n\n"
            r"$a \cdot 0 = 0$"
            "\n\nכלומר $0 \\cdot a = 0$ (משתמשים בקומוטטיביות הכפל בהמשך). $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_multiplication_by_negative_one",
        claim_id="thm_multiplication_by_negative_one",
        method="informal",
        status="reviewed",
        is_canonical=True,
        dependencies=["ax_multiplicative_identity", "ax_distributive_law", "ax_additive_inverse", "thm_multiplication_by_zero", "thm_addition_cancellation"],
        body=(
            "נראה ש-$(-1) \\cdot a + a = 0$, וזה יוכיח ש-$(-1) \\cdot a$ הוא ההפכי הנגדי של $a$, כלומר $-a$:\n\n"
            r"$(-1) \cdot a + a = (-1) \cdot a + 1 \cdot a$"
            " (מאיבר ניטרלי לכפל)"
            "\n\n"
            r"$= ((-1) + 1) \cdot a$"
            " (חוק הפילוג)"
            "\n\n"
            r"$= 0 \cdot a$"
            " (מאיבר נגדי)"
            "\n\n"
            r"$= 0$"
            " (משפט אפס בכפל)."
            "\n\n"
            "מכאן $(-1) \\cdot a + a = 0$, ולכן $(-1) \\cdot a = -a$ (יחידות הנגדי, או הוספת $-a$ ב-thm_addition_cancellation). $\\blacksquare$"
        ),
    ),
]


# ─────────────────────────────────────────────────────────────────
# Chunk 2 — Multiplication-side field axioms, order, elementary algebra
# ─────────────────────────────────────────────────────────────────

COURSES_CHUNK2 = [
    Course(
        id="math_elementary",
        name="מתמטיקה יסודי — אלגברה בסיסית",
        prerequisites=["math_foundations"],
    ),
]

_FOUND = "math_foundations"
_ELEM = "math_elementary"

CLAIMS_CHUNK2 = [
    # ─── Field axioms (multiplication side) ───
    Claim(
        id="ax_multiplication_associativity", kind="axiom", status=CANON,
        course=_FOUND, topic="אקסיומות שדה",
        statement=r"**אסוציאטיביות הכפל:** לכל $a, b, c \in \mathbb{R}$ מתקיים $(a \cdot b) \cdot c = a \cdot (b \cdot c)$.",
    ),
    Claim(
        id="ax_multiplication_commutativity", kind="axiom", status=CANON,
        course=_FOUND, topic="אקסיומות שדה",
        statement=r"**קומוטטיביות הכפל:** לכל $a, b \in \mathbb{R}$ מתקיים $a \cdot b = b \cdot a$.",
    ),
    Claim(
        id="ax_multiplicative_inverse", kind="axiom", status=CANON,
        course=_FOUND, topic="אקסיומות שדה",
        statement=r"**איבר הפכי לכפל:** לכל $a \in \mathbb{R}$, $a \neq 0$, קיים $a^{-1} \in \mathbb{R}$ כך ש-$a \cdot a^{-1} = 1$.",
    ),

    # ─── Order axioms ───
    Claim(
        id="ax_order_trichotomy", kind="axiom", status=CANON,
        course=_FOUND, topic="אקסיומות סדר",
        statement=r"**טריכוטומיה:** לכל $a, b \in \mathbb{R}$ מתקיים בדיוק אחד משלושת הבאים: $a < b$, $a = b$, $a > b$.",
    ),
    Claim(
        id="ax_order_transitivity", kind="axiom", status=CANON,
        course=_FOUND, topic="אקסיומות סדר",
        statement=r"**טרנזיטיביות הסדר:** אם $a < b$ ו-$b < c$, אז $a < c$.",
    ),
    Claim(
        id="ax_addition_preserves_order", kind="axiom", status=CANON,
        course=_FOUND, topic="אקסיומות סדר",
        statement=r"**שימור סדר בחיבור:** אם $a < b$, אז $a + c < b + c$ לכל $c \in \mathbb{R}$.",
    ),
    Claim(
        id="ax_positive_multiplication_preserves_order", kind="axiom", status=CANON,
        course=_FOUND, topic="אקסיומות סדר",
        statement=r"**שימור סדר בכפל בחיובי:** אם $a < b$ ו-$c > 0$, אז $a \cdot c < b \cdot c$.",
    ),

    # ─── Basic definitions ───
    Claim(
        id="def_subtraction", kind="definition", status=CANON,
        course=_ELEM, topic="פעולות יסודיות",
        statement=r"**חיסור:** לכל $a, b \in \mathbb{R}$ מגדירים $a - b := a + (-b)$.",
    ),
    Claim(
        id="def_division", kind="definition", status=CANON,
        course=_ELEM, topic="פעולות יסודיות",
        statement=r"**חילוק:** לכל $a, b \in \mathbb{R}$ עם $b \neq 0$ מגדירים $a / b := a \cdot b^{-1}$.",
    ),
    Claim(
        id="def_natural_power", kind="definition", status=CANON,
        course=_ELEM, topic="חזקות",
        statement=r"**חזקה טבעית:** עבור $a \in \mathbb{R}$ ו-$n \in \mathbb{N}$ מגדירים רקורסיבית: $a^0 := 1$, ולכל $n \geq 0$: $a^{n+1} := a^n \cdot a$.",
    ),
    Claim(
        id="def_absolute_value", kind="definition", status=CANON,
        course=_ELEM, topic="ערך מוחלט",
        statement=r"**ערך מוחלט:** $|a| := \begin{cases} a & a \geq 0 \\ -a & a < 0 \end{cases}$",
    ),

    # ─── Theorems ───
    Claim(
        id="thm_additive_identity_uniqueness", kind="theorem", status=CANON,
        course=_ELEM, topic="יחידות",
        statement=r"**יחידות איבר ניטרלי לחיבור:** קיים בדיוק $0 \in \mathbb{R}$ יחיד המקיים $a + 0 = a$ לכל $a$.",
    ),
    Claim(
        id="thm_additive_inverse_uniqueness", kind="theorem", status=CANON,
        course=_ELEM, topic="יחידות",
        statement=r"**יחידות הנגדי:** לכל $a \in \mathbb{R}$, האיבר $-a$ הוא יחיד — אין שני איברים שונים שמקיימים $a + x = 0$.",
    ),
    Claim(
        id="thm_double_negation", kind="theorem", status=CANON,
        course=_ELEM, topic="אלגברה בסיסית",
        statement=r"**ניוד כפול:** לכל $a \in \mathbb{R}$ מתקיים $-(-a) = a$.",
    ),
    Claim(
        id="thm_negation_of_sum", kind="theorem", status=CANON,
        course=_ELEM, topic="אלגברה בסיסית",
        statement=r"**נגדי של סכום:** לכל $a, b \in \mathbb{R}$ מתקיים $-(a + b) = (-a) + (-b)$.",
    ),
    Claim(
        id="thm_right_distributive_law", kind="theorem", status=CANON,
        course=_ELEM, topic="אלגברה בסיסית",
        statement=r"**חוק הפילוג הימני:** לכל $a, b, c \in \mathbb{R}$ מתקיים $(b + c) \cdot a = b \cdot a + c \cdot a$.",
    ),
    Claim(
        id="thm_no_zero_divisors", kind="theorem", status=CANON,
        course=_ELEM, topic="אלגברה בסיסית",
        statement=r"**אין מחלקי אפס:** אם $a \cdot b = 0$ אז $a = 0$ או $b = 0$.",
    ),
    Claim(
        id="thm_product_of_negatives", kind="theorem", status=CANON,
        course=_ELEM, topic="אלגברה בסיסית",
        statement=r"**מינוס כפול מינוס:** לכל $a, b \in \mathbb{R}$ מתקיים $(-a) \cdot (-b) = a \cdot b$.",
    ),
    Claim(
        id="thm_negative_times_positive_is_negative", kind="theorem", status=CANON,
        course=_ELEM, topic="אי-שוויונים",
        statement=r"**כפל שלילי בחיובי שלילי:** אם $a < 0$ ו-$b > 0$, אז $a \cdot b < 0$.",
    ),
    Claim(
        id="thm_square_nonnegative", kind="theorem", status=CANON,
        course=_ELEM, topic="אי-שוויונים",
        statement=r"**ריבוע אי-שלילי:** לכל $a \in \mathbb{R}$ מתקיים $a^2 \geq 0$.",
    ),
    Claim(
        id="thm_zero_lt_one", kind="theorem", status=CANON,
        course=_ELEM, topic="אי-שוויונים",
        statement=r"**$0 < 1$:** האפס קטן מהאחד.",
    ),
    Claim(
        id="thm_power_addition_rule", kind="theorem", status=CANON,
        course=_ELEM, topic="חזקות",
        statement=r"**חיבור מעריכים:** לכל $a \in \mathbb{R}$ ולכל $m, n \in \mathbb{N}$ מתקיים $a^m \cdot a^n = a^{m+n}$.",
    ),
    Claim(
        id="thm_power_multiplication_rule", kind="theorem", status=CANON,
        course=_ELEM, topic="חזקות",
        statement=r"**חזקה של חזקה:** לכל $a \in \mathbb{R}$ ולכל $m, n \in \mathbb{N}$ מתקיים $(a^m)^n = a^{m \cdot n}$.",
    ),
    Claim(
        id="thm_power_of_product", kind="theorem", status=CANON,
        course=_ELEM, topic="חזקות",
        statement=r"**חזקה של מכפלה:** לכל $a, b \in \mathbb{R}$ ולכל $n \in \mathbb{N}$ מתקיים $(a \cdot b)^n = a^n \cdot b^n$.",
    ),
    Claim(
        id="thm_absolute_value_nonnegative", kind="theorem", status=CANON,
        course=_ELEM, topic="ערך מוחלט",
        statement=r"**ערך מוחלט אי-שלילי:** לכל $a \in \mathbb{R}$ מתקיים $|a| \geq 0$.",
    ),
    Claim(
        id="thm_absolute_value_zero_iff", kind="theorem", status=CANON,
        course=_ELEM, topic="ערך מוחלט",
        statement=r"**$|a| = 0$ אם ורק אם $a = 0$:** הערך המוחלט מתאפס בדיוק עבור אפס.",
    ),
    Claim(
        id="thm_absolute_value_of_product", kind="theorem", status=CANON,
        course=_ELEM, topic="ערך מוחלט",
        statement=r"**ערך מוחלט של מכפלה:** לכל $a, b \in \mathbb{R}$ מתקיים $|a \cdot b| = |a| \cdot |b|$.",
    ),
    Claim(
        id="thm_triangle_inequality", kind="theorem", status=CANON,
        course=_ELEM, topic="ערך מוחלט",
        statement=r"**אי-שוויון המשולש:** לכל $a, b \in \mathbb{R}$ מתקיים $|a + b| \leq |a| + |b|$.",
    ),
    Claim(
        id="thm_addition_undoes_subtraction", kind="theorem", status=CANON,
        course=_ELEM, topic="אלגברה בסיסית",
        statement=r"**חיבור הופך חיסור:** לכל $a, b \in \mathbb{R}$ מתקיים $(a - b) + b = a$.",
    ),
    Claim(
        id="thm_difference_of_squares", kind="theorem", status=CANON,
        course=_ELEM, topic="זהויות אלגבריות",
        statement=r"**הפרש ריבועים:** לכל $a, b \in \mathbb{R}$ מתקיים $a^2 - b^2 = (a - b)(a + b)$.",
    ),
]


PROOFS_CHUNK2 = [
    Proof(
        id="prf_additive_identity_uniqueness",
        claim_id="thm_additive_identity_uniqueness",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["ax_additive_identity", "ax_addition_commutativity"],
        body=(
            "נניח שגם $0$ וגם $0'$ הם איברים ניטרליים לחיבור: $a + 0 = a$ ו-$a + 0' = a$ לכל $a$.\n\n"
            "אז $0 = 0 + 0'$ (לפי הניטרליות של $0'$), ו-$0 + 0' = 0' + 0$ (קומוטטיביות), ו-$0' + 0 = 0'$ (ניטרליות של $0$).\n\n"
            "מכאן $0 = 0'$. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_additive_inverse_uniqueness",
        claim_id="thm_additive_inverse_uniqueness",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["ax_addition_associativity", "ax_addition_commutativity",
                      "ax_additive_identity", "ax_additive_inverse"],
        body=(
            "נניח ש-$b$ ו-$c$ שניהם מקיימים $a + b = 0$ ו-$a + c = 0$.\n\n"
            "אז $b = b + 0 = b + (a + c) = (b + a) + c = (a + b) + c = 0 + c = c$.\n\n"
            "השתמשנו באיבר ניטרלי, אסוציאטיביות, קומוטטיביות, ובהגדרת הנגדי. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_double_negation",
        claim_id="thm_double_negation",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["ax_additive_inverse", "ax_addition_commutativity",
                      "thm_additive_inverse_uniqueness"],
        body=(
            "מהגדרת נגדי: $(-a) + (-(-a)) = 0$. \n\n"
            "מצד שני, מקומוטטיביות: $(-a) + a = a + (-a) = 0$. \n\n"
            "כלומר שני האיברים $-(-a)$ ו-$a$ הם נגדיים ל-$(-a)$. מיחידות הנגדי נובע $-(-a) = a$. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_negation_of_sum",
        claim_id="thm_negation_of_sum",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["ax_addition_associativity", "ax_addition_commutativity",
                      "ax_additive_identity", "ax_additive_inverse",
                      "thm_additive_inverse_uniqueness"],
        body=(
            "נראה ש-$(-a) + (-b)$ הוא הנגדי של $a + b$, ומיחידות הנגדי ננבע ש-$-(a+b) = (-a) + (-b)$.\n\n"
            "$(a + b) + ((-a) + (-b)) = (a + (-a)) + (b + (-b)) = 0 + 0 = 0$\n\n"
            "(תוך שימוש באסוציאטיביות וקומוטטיביות לסידור מחדש של הסכום, ובהגדרת הנגדי). $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_right_distributive_law",
        claim_id="thm_right_distributive_law",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["ax_distributive_law", "ax_multiplication_commutativity"],
        body=(
            "$(b + c) \\cdot a = a \\cdot (b + c)$ (קומוטטיביות הכפל) $= a \\cdot b + a \\cdot c$ (חוק הפילוג השמאלי) $= b \\cdot a + c \\cdot a$ (קומוטטיביות). $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_no_zero_divisors",
        claim_id="thm_no_zero_divisors",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["ax_multiplicative_identity", "ax_multiplicative_inverse",
                      "ax_multiplication_associativity", "thm_multiplication_by_zero"],
        body=(
            "נניח $a \\cdot b = 0$ ו-$a \\neq 0$. נראה ש-$b = 0$.\n\n"
            "מאיבר הפכי לכפל קיים $a^{-1}$, ולכן:\n\n"
            "$b = 1 \\cdot b = (a^{-1} \\cdot a) \\cdot b = a^{-1} \\cdot (a \\cdot b) = a^{-1} \\cdot 0 = 0$.\n\n"
            "(אסוציאטיביות הכפל ומשפט אפס בכפל בשורה האחרונה.) $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_product_of_negatives",
        claim_id="thm_product_of_negatives",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["ax_distributive_law", "ax_additive_inverse",
                      "thm_multiplication_by_zero", "thm_double_negation",
                      "thm_additive_inverse_uniqueness"],
        body=(
            "נראה ש-$(-a) \\cdot b = -(a \\cdot b)$:\n\n"
            "$(-a) \\cdot b + a \\cdot b = ((-a) + a) \\cdot b = 0 \\cdot b = 0$, ולכן $(-a) \\cdot b$ הוא הנגדי של $a \\cdot b$, כלומר $-(ab)$.\n\n"
            "באותה דרך, $(-a) \\cdot (-b) + (-a) \\cdot b = (-a) \\cdot ((-b) + b) = (-a) \\cdot 0 = 0$, ולכן $(-a)(-b) = -((-a) \\cdot b) = -(-(ab)) = ab$ (לפי ניוד כפול). $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_negative_times_positive_is_negative",
        claim_id="thm_negative_times_positive_is_negative",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["ax_addition_preserves_order", "ax_positive_multiplication_preserves_order",
                      "ax_additive_identity", "ax_additive_inverse",
                      "thm_multiplication_by_negative_one", "thm_double_negation",
                      "thm_product_of_negatives"],
        body=(
            "מ-$a < 0$ נוסיף $-a$ לשני האגפים: $a + (-a) < 0 + (-a)$, כלומר $0 < -a$.\n\n"
            "עכשיו $-a > 0$ ו-$b > 0$, ולפי שימור סדר בכפל בחיובי: $0 \\cdot b < (-a) \\cdot b$, כלומר $0 < (-a) \\cdot b = -(a \\cdot b)$ (לפי מכפלת נגדי בחיובי).\n\n"
            "מכאן $a \\cdot b < 0$. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_square_nonnegative",
        claim_id="thm_square_nonnegative",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_natural_power", "ax_order_trichotomy",
                      "ax_positive_multiplication_preserves_order",
                      "thm_product_of_negatives", "thm_multiplication_by_zero"],
        body=(
            "לפי טריכוטומיה, או $a > 0$, $a = 0$, או $a < 0$.\n\n"
            "אם $a = 0$: $a^2 = 0 \\cdot 0 = 0 \\geq 0$.\n\n"
            "אם $a > 0$: לפי שימור סדר בכפל בחיובי, $0 \\cdot a < a \\cdot a$, כלומר $0 < a^2$.\n\n"
            "אם $a < 0$: אז $-a > 0$, ו-$a^2 = a \\cdot a = (-a) \\cdot (-a) > 0$ (לפי המקרה הקודם ומכפלת שני נגדיים). $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_zero_lt_one",
        claim_id="thm_zero_lt_one",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["ax_multiplicative_identity", "ax_order_trichotomy",
                      "thm_square_nonnegative", "def_natural_power"],
        body=(
            "מהגדרת חזקה ואיבר ניטרלי: $1 = 1 \\cdot 1 = 1^2$.\n\n"
            "לפי משפט ריבוע אי-שלילי, $1^2 \\geq 0$, כלומר $1 \\geq 0$.\n\n"
            "מאיבר ניטרלי לכפל $1 \\neq 0$, אז לפי טריכוטומיה $1 > 0$. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_power_addition_rule",
        claim_id="thm_power_addition_rule",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_natural_power", "ax_multiplication_associativity",
                      "ax_multiplicative_identity"],
        body=(
            "הוכחה באינדוקציה על $n$.\n\n"
            "**בסיס $n = 0$:** $a^m \\cdot a^0 = a^m \\cdot 1 = a^m = a^{m+0}$.\n\n"
            "**צעד:** נניח $a^m \\cdot a^n = a^{m+n}$. אז $a^m \\cdot a^{n+1} = a^m \\cdot (a^n \\cdot a) = (a^m \\cdot a^n) \\cdot a = a^{m+n} \\cdot a = a^{(m+n)+1} = a^{m+(n+1)}$ (לפי הגדרת חזקה ואסוציאטיביות). $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_power_multiplication_rule",
        claim_id="thm_power_multiplication_rule",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_natural_power", "thm_power_addition_rule",
                      "ax_multiplicative_identity"],
        body=(
            "אינדוקציה על $n$.\n\n"
            "**בסיס $n = 0$:** $(a^m)^0 = 1 = a^0 = a^{m \\cdot 0}$.\n\n"
            "**צעד:** $(a^m)^{n+1} = (a^m)^n \\cdot a^m = a^{m \\cdot n} \\cdot a^m = a^{m \\cdot n + m} = a^{m(n+1)}$ (לפי הגדרת חזקה, הנחת האינדוקציה, וחיבור מעריכים). $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_power_of_product",
        claim_id="thm_power_of_product",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_natural_power", "ax_multiplication_associativity",
                      "ax_multiplication_commutativity", "ax_multiplicative_identity"],
        body=(
            "אינדוקציה על $n$.\n\n"
            "**בסיס $n = 0$:** $(ab)^0 = 1 = 1 \\cdot 1 = a^0 \\cdot b^0$.\n\n"
            "**צעד:** $(ab)^{n+1} = (ab)^n \\cdot (ab) = (a^n b^n)(ab) = (a^n \\cdot a)(b^n \\cdot b) = a^{n+1} b^{n+1}$ (תוך שימוש בקומוטטיביות ואסוציאטיביות לארגון הגורמים). $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_absolute_value_nonnegative",
        claim_id="thm_absolute_value_nonnegative",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_absolute_value", "ax_additive_inverse",
                      "ax_addition_preserves_order", "ax_additive_identity"],
        body=(
            "פיצול לפי הגדרה:\n\n"
            "אם $a \\geq 0$: $|a| = a \\geq 0$.\n\n"
            "אם $a < 0$: נוסיף $-a$ לשני האגפים של $a < 0$ ונקבל $0 < -a$, כלומר $|a| = -a > 0 \\geq 0$. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_absolute_value_zero_iff",
        claim_id="thm_absolute_value_zero_iff",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_absolute_value", "thm_double_negation"],
        body=(
            "($\\Leftarrow$) אם $a = 0$ אז $|0| = 0$ (לפי המקרה $a \\geq 0$ בהגדרה).\n\n"
            "($\\Rightarrow$) אם $|a| = 0$: במקרה $a \\geq 0$ מקבלים $a = |a| = 0$. במקרה $a < 0$ מקבלים $-a = 0$, ולפי ניוד כפול $a = -(-a) = -0 = 0$, סתירה. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_absolute_value_of_product",
        claim_id="thm_absolute_value_of_product",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_absolute_value", "thm_product_of_negatives",
                      "thm_negative_times_positive_is_negative", "thm_multiplication_by_zero"],
        body=(
            "פיצול לפי סימני $a$ ו-$b$ (ארבעה מקרים): שני חיוביים, שני שליליים, אחד חיובי אחד שלילי, או לפחות אחד אפס.\n\n"
            "בכל מקרה בודקים שהסימן של $a \\cdot b$ תואם, ובעזרת מכפלת נגדיים מקבלים $|ab| = |a| \\cdot |b|$. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_triangle_inequality",
        claim_id="thm_triangle_inequality",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_absolute_value", "thm_absolute_value_nonnegative",
                      "ax_addition_preserves_order"],
        body=(
            "מההגדרה: $-|a| \\leq a \\leq |a|$ ו-$-|b| \\leq b \\leq |b|$. \n\n"
            "מחיבור איברי האי-שוויונים (לפי שימור סדר בחיבור פעמיים): $-(|a|+|b|) \\leq a + b \\leq |a|+|b|$.\n\n"
            "כלומר $|a + b| \\leq |a| + |b|$ (לפי הגדרת הערך המוחלט). $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_addition_undoes_subtraction",
        claim_id="thm_addition_undoes_subtraction",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_subtraction", "ax_addition_associativity",
                      "ax_addition_commutativity", "ax_additive_inverse", "ax_additive_identity"],
        body=(
            "$(a - b) + b = (a + (-b)) + b$ (הגדרת חיסור) $= a + ((-b) + b)$ (אסוציאטיביות) $= a + 0$ (קומוטטיביות + נגדי) $= a$ (איבר ניטרלי). $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_difference_of_squares",
        claim_id="thm_difference_of_squares",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_natural_power", "def_subtraction",
                      "ax_distributive_law", "thm_right_distributive_law",
                      "ax_addition_commutativity", "ax_addition_associativity",
                      "ax_additive_inverse", "ax_additive_identity",
                      "thm_product_of_negatives"],
        body=(
            "$(a - b)(a + b) = (a + (-b))(a + b)$ (הגדרת חיסור)\n\n"
            "$= a \\cdot a + a \\cdot b + (-b) \\cdot a + (-b) \\cdot b$ (פילוג ימני ושמאלי)\n\n"
            "$= a^2 + ab + (-(ba)) + (-(b^2))$ (לפי מכפלת נגדי)\n\n"
            "$= a^2 + ab - ab - b^2 = a^2 - b^2$ (קומוטטיביות, איבר נגדי, ואיבר ניטרלי). $\\blacksquare$"
        ),
    ),
]


# ─────────────────────────────────────────────────────────────────
# Chunk 3 — Number systems, divisibility, fractions, linear,
#           Euclidean geometry primitives, functions intro
# ─────────────────────────────────────────────────────────────────

COURSES_CHUNK3 = [
    Course(
        id="math_jhs",
        name="מתמטיקה חטיבת ביניים",
        prerequisites=["math_elementary"],
    ),
]

_JHS = "math_jhs"

CLAIMS_CHUNK3 = [
    # ─── Number systems (kept in elementary, foundational) ───
    Claim(
        id="def_natural_numbers", kind="definition", status=CANON,
        course=_ELEM, topic="מערכות מספרים",
        statement=r"**מספרים טבעיים:** $\mathbb{N} := \{0, 1, 2, 3, \ldots\}$ — קבוצת המספרים שמתחילה ב-0 וכל איבר בה הוא העוקב של קודמו.",
    ),
    Claim(
        id="def_integers", kind="definition", status=CANON,
        course=_ELEM, topic="מערכות מספרים",
        statement=r"**מספרים שלמים:** $\mathbb{Z} := \mathbb{N} \cup \{-n : n \in \mathbb{N}, n > 0\} = \{\ldots, -2, -1, 0, 1, 2, \ldots\}$.",
    ),
    Claim(
        id="def_rational_numbers", kind="definition", status=CANON,
        course=_ELEM, topic="מערכות מספרים",
        statement=r"**מספרים רציונליים:** $\mathbb{Q} := \{a/b : a, b \in \mathbb{Z}, b \neq 0\}$ — מנות של שלמים.",
    ),

    # ─── Divisibility & primes ───
    Claim(
        id="def_divisibility", kind="definition", status=CANON,
        course=_JHS, topic="התחלקות",
        statement=r"**התחלקות:** עבור $a, b \in \mathbb{Z}$ נאמר ש-$a$ מחלק את $b$ (נסמן $a \mid b$) אם קיים $k \in \mathbb{Z}$ כך ש-$b = a \cdot k$.",
    ),
    Claim(
        id="def_prime", kind="definition", status=CANON,
        course=_JHS, topic="התחלקות",
        statement=r"**מספר ראשוני:** מספר טבעי $p > 1$ נקרא ראשוני אם המחלקים החיוביים היחידים שלו הם $1$ ו-$p$.",
    ),
    Claim(
        id="thm_divisibility_transitivity", kind="theorem", status=CANON,
        course=_JHS, topic="התחלקות",
        statement=r"**טרנזיטיביות ההתחלקות:** אם $a \mid b$ ו-$b \mid c$, אז $a \mid c$.",
    ),
    Claim(
        id="thm_divisibility_linear_combinations", kind="theorem", status=CANON,
        course=_JHS, topic="התחלקות",
        statement=r"**צירוף לינארי של מחלקים:** אם $a \mid b$ ו-$a \mid c$, אז $a \mid (m \cdot b + n \cdot c)$ לכל $m, n \in \mathbb{Z}$.",
    ),
    Claim(
        id="thm_division_algorithm", kind="theorem", status=CANON,
        course=_JHS, topic="התחלקות",
        statement=r"**אלגוריתם החילוק:** לכל $a \in \mathbb{Z}$ ו-$b \in \mathbb{Z}$ עם $b > 0$ קיימים $q, r \in \mathbb{Z}$ יחידים כך ש-$a = b \cdot q + r$ ו-$0 \leq r < b$.",
    ),
    Claim(
        id="thm_fundamental_theorem_arithmetic", kind="theorem", status=CANON,
        course=_JHS, topic="התחלקות",
        statement=r"**המשפט היסודי של האריתמטיקה:** לכל מספר טבעי $n > 1$ קיים פירוק יחיד (עד כדי סדר הגורמים) למכפלה של מספרים ראשוניים: $n = p_1 \cdot p_2 \cdots p_k$.",
    ),

    # ─── Fractions ───
    Claim(
        id="def_fraction", kind="definition", status=CANON,
        course=_JHS, topic="שברים",
        statement=r"**שבר:** הביטוי $\frac{a}{b}$ עבור $a, b \in \mathbb{Z}$ עם $b \neq 0$ הוא המספר $a \cdot b^{-1}$ (לפי הגדרת חילוק).",
    ),
    Claim(
        id="thm_fraction_equality", kind="theorem", status=CANON,
        course=_JHS, topic="שברים",
        statement=r"**שוויון שברים:** $\frac{a}{b} = \frac{c}{d}$ אם ורק אם $a \cdot d = b \cdot c$ (עבור $b, d \neq 0$).",
    ),
    Claim(
        id="thm_fraction_addition", kind="theorem", status=CANON,
        course=_JHS, topic="שברים",
        statement=r"**חיבור שברים:** $\frac{a}{b} + \frac{c}{d} = \frac{a \cdot d + b \cdot c}{b \cdot d}$ (עבור $b, d \neq 0$).",
    ),
    Claim(
        id="thm_fraction_multiplication", kind="theorem", status=CANON,
        course=_JHS, topic="שברים",
        statement=r"**כפל שברים:** $\frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d}$ (עבור $b, d \neq 0$).",
    ),

    # ─── Linear equations & inequalities ───
    Claim(
        id="thm_linear_equation_solution", kind="theorem", status=CANON,
        course=_JHS, topic="משוואות לינאריות",
        statement=r"**פתרון משוואה לינארית:** למשוואה $a \cdot x + b = 0$ עם $a \neq 0$ קיים פתרון יחיד $x = -\frac{b}{a}$.",
    ),
    Claim(
        id="thm_inequality_negation_flips", kind="theorem", status=CANON,
        course=_JHS, topic="אי-שוויונים",
        statement=r"**ניוד הופך אי-שוויון:** אם $a < b$ אז $-b < -a$.",
    ),
    Claim(
        id="thm_reciprocal_flips_inequality", kind="theorem", status=CANON,
        course=_JHS, topic="אי-שוויונים",
        statement=r"**הופכי הופך אי-שוויון (חיוביים):** אם $0 < a < b$ אז $0 < \frac{1}{b} < \frac{1}{a}$.",
    ),

    # ─── Euclidean geometry primitives ───
    Claim(
        id="ax_euclid_two_points_one_line", kind="axiom", status=CANON,
        course=_JHS, topic="גאומטריה",
        statement=r"**שתי נקודות קובעות ישר:** עבור כל שתי נקודות שונות במישור קיים ישר יחיד העובר דרכן.",
    ),
    Claim(
        id="ax_euclid_parallel_postulate", kind="axiom", status=CANON,
        course=_JHS, topic="גאומטריה",
        statement=r"**אקסיומת המקבילים:** דרך נקודה שאינה על ישר נתון, קיים ישר יחיד המקביל אליו.",
    ),
    Claim(
        id="def_segment", kind="definition", status=CANON,
        course=_JHS, topic="גאומטריה",
        statement=r"**קטע:** עבור שתי נקודות $A, B$, קטע $\overline{AB}$ הוא חלק הישר שביניהן, כולל את נקודות הקצה.",
    ),
    Claim(
        id="def_angle", kind="definition", status=CANON,
        course=_JHS, topic="גאומטריה",
        statement=r"**זווית:** איחוד של שתי קרניים בעלות נקודת מוצא משותפת (קודקוד הזווית). הזווית נמדדת במעלות בין $0°$ ל-$360°$.",
    ),
    Claim(
        id="def_triangle", kind="definition", status=CANON,
        course=_JHS, topic="גאומטריה",
        statement=r"**משולש:** שלוש נקודות $A, B, C$ שאינן על ישר אחד, יחד עם שלושת הקטעים המחברים ביניהן: $\overline{AB}, \overline{BC}, \overline{CA}$.",
    ),
    Claim(
        id="thm_triangle_angle_sum", kind="theorem", status=CANON,
        course=_JHS, topic="גאומטריה",
        statement=r"**סכום זוויות במשולש:** סכום שלוש הזוויות הפנימיות של משולש שווה ל-$180°$.",
    ),
    Claim(
        id="def_right_triangle", kind="definition", status=CANON,
        course=_JHS, topic="גאומטריה",
        statement=r"**משולש ישר-זווית:** משולש שבו אחת מהזוויות הפנימיות שווה ל-$90°$. הצלע שמול הזווית הישרה נקראת **יתר**, ושתי הצלעות האחרות **ניצבים**.",
    ),
    Claim(
        id="thm_pythagoras", kind="theorem", status=CANON,
        course=_JHS, topic="גאומטריה",
        statement=r"**משפט פיתגורס:** במשולש ישר-זווית עם ניצבים באורך $a$ ו-$b$ ויתר באורך $c$, מתקיים $a^2 + b^2 = c^2$.",
    ),

    # ─── Functions intro ───
    Claim(
        id="def_function", kind="definition", status=CANON,
        course=_JHS, topic="פונקציות",
        statement=r"**פונקציה:** פונקציה $f: A \to B$ היא התאמה המקצה לכל איבר $x \in A$ איבר יחיד $f(x) \in B$.",
    ),
    Claim(
        id="def_domain", kind="definition", status=CANON,
        course=_JHS, topic="פונקציות",
        statement=r"**תחום הגדרה:** עבור פונקציה $f: A \to B$, תחום ההגדרה הוא הקבוצה $A$ — כל ה-$x$-ים שעליהם הפונקציה מוגדרת.",
    ),
    Claim(
        id="def_range", kind="definition", status=CANON,
        course=_JHS, topic="פונקציות",
        statement=r"**טווח הפונקציה:** עבור פונקציה $f: A \to B$, הטווח הוא $\{f(x) : x \in A\} \subseteq B$ — קבוצת הערכים שהפונקציה מקבלת בפועל.",
    ),
    Claim(
        id="def_linear_function", kind="definition", status=CANON,
        course=_JHS, topic="פונקציות",
        statement=r"**פונקציה לינארית:** פונקציה מהצורה $f(x) = a \cdot x + b$ עבור $a, b \in \mathbb{R}$ קבועים. $a$ נקרא ה**שיפוע** ו-$b$ נקרא ה**חותך** (ערך הפונקציה ב-$x = 0$).",
    ),
    Claim(
        id="def_slope_between_points", kind="definition", status=CANON,
        course=_JHS, topic="פונקציות",
        statement=r"**שיפוע בין שתי נקודות:** השיפוע של הישר העובר דרך $(x_1, y_1)$ ו-$(x_2, y_2)$ (עם $x_1 \neq x_2$) הוא $m = \frac{y_2 - y_1}{x_2 - x_1}$.",
    ),
    Claim(
        id="thm_linear_function_unique_zero", kind="theorem", status=CANON,
        course=_JHS, topic="פונקציות",
        statement=r"**אפס של פונקציה לינארית:** לפונקציה $f(x) = a \cdot x + b$ עם $a \neq 0$ קיים אפס יחיד: $x = -\frac{b}{a}$.",
    ),
]


PROOFS_CHUNK3 = [
    Proof(
        id="prf_divisibility_transitivity",
        claim_id="thm_divisibility_transitivity",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_divisibility", "ax_multiplication_associativity"],
        body=(
            "מ-$a \\mid b$ קיים $k_1$ כך ש-$b = a \\cdot k_1$. מ-$b \\mid c$ קיים $k_2$ כך ש-$c = b \\cdot k_2$.\n\n"
            "אז $c = (a \\cdot k_1) \\cdot k_2 = a \\cdot (k_1 \\cdot k_2)$ (לפי אסוציאטיביות), ולכן $a \\mid c$ (העד הוא $k_1 \\cdot k_2$). $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_divisibility_linear_combinations",
        claim_id="thm_divisibility_linear_combinations",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_divisibility", "ax_distributive_law",
                      "ax_multiplication_associativity", "ax_multiplication_commutativity"],
        body=(
            "$a \\mid b$ נותן $b = a \\cdot k_1$, ו-$a \\mid c$ נותן $c = a \\cdot k_2$. אז:\n\n"
            "$m \\cdot b + n \\cdot c = m \\cdot (a \\cdot k_1) + n \\cdot (a \\cdot k_2) = a \\cdot (m \\cdot k_1) + a \\cdot (n \\cdot k_2) = a \\cdot (m \\cdot k_1 + n \\cdot k_2)$\n\n"
            "(אסוציאטיביות, קומוטטיביות, פילוג). לכן $a \\mid (mb + nc)$. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_division_algorithm",
        claim_id="thm_division_algorithm",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_integers", "ax_order_trichotomy"],
        body=(
            "**קיום:** נסתכל בקבוצה $S = \\{a - b \\cdot k : k \\in \\mathbb{Z}, a - b \\cdot k \\geq 0\\}$. $S$ אינה ריקה (לדוגמה, עבור $k = -|a|$). לפי עקרון הסדר הטוב במספרים הטבעיים, ל-$S$ יש איבר מינימלי $r = a - b \\cdot q$. ברור $r \\geq 0$. אם $r \\geq b$ אז $r - b = a - b(q+1) \\geq 0$ ב-$S$ וקטן מ-$r$, סתירה. לכן $0 \\leq r < b$.\n\n"
            "**יחידות:** אם $a = b q_1 + r_1 = b q_2 + r_2$ אז $b(q_1 - q_2) = r_2 - r_1$. אבל $|r_2 - r_1| < b$, אז בהכרח $q_1 = q_2$ ו-$r_1 = r_2$. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_fundamental_theorem_arithmetic",
        claim_id="thm_fundamental_theorem_arithmetic",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_prime", "def_divisibility",
                      "thm_division_algorithm"],
        body=(
            "**קיום הפירוק:** באינדוקציה חזקה על $n$. אם $n$ ראשוני, סיימנו. אחרת קיים מחלק $1 < d < n$, ולכן $n = d \\cdot (n/d)$ כאשר שני הגורמים קטנים מ-$n$. לפי הנחת האינדוקציה לכל אחד מהם פירוק לראשוניים — נצרף ונקבל פירוק ל-$n$.\n\n"
            "**יחידות:** משתמשים בלמת אוקלידס (אם $p \\mid ab$ ו-$p$ ראשוני, אז $p \\mid a$ או $p \\mid b$), ומראים שכל פירוק שונה היה מוביל לסתירה עם הלמה. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_fraction_equality",
        claim_id="thm_fraction_equality",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_fraction", "ax_multiplicative_inverse",
                      "ax_multiplication_associativity", "ax_multiplication_commutativity"],
        body=(
            "($\\Rightarrow$) אם $\\frac{a}{b} = \\frac{c}{d}$ אז $a \\cdot b^{-1} = c \\cdot d^{-1}$. נכפול שני האגפים ב-$b \\cdot d$: $a \\cdot d = c \\cdot b$.\n\n"
            "($\\Leftarrow$) אם $a \\cdot d = b \\cdot c$ נכפול שני האגפים ב-$b^{-1} \\cdot d^{-1}$: $a \\cdot b^{-1} = c \\cdot d^{-1}$, כלומר $\\frac{a}{b} = \\frac{c}{d}$. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_fraction_addition",
        claim_id="thm_fraction_addition",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_fraction", "ax_distributive_law",
                      "ax_multiplication_associativity", "ax_multiplication_commutativity",
                      "ax_multiplicative_inverse"],
        body=(
            "$\\frac{a}{b} + \\frac{c}{d} = a \\cdot b^{-1} + c \\cdot d^{-1}$. נכפול ונחלק במכנה משותף $b \\cdot d$:\n\n"
            "$= \\frac{a \\cdot d}{b \\cdot d} + \\frac{c \\cdot b}{d \\cdot b} = \\frac{a \\cdot d + b \\cdot c}{b \\cdot d}$\n\n"
            "(לפי שוויון שברים וחוק הפילוג). $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_fraction_multiplication",
        claim_id="thm_fraction_multiplication",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_fraction", "ax_multiplication_associativity",
                      "ax_multiplication_commutativity"],
        body=(
            "$\\frac{a}{b} \\cdot \\frac{c}{d} = (a \\cdot b^{-1}) \\cdot (c \\cdot d^{-1}) = (a \\cdot c) \\cdot (b^{-1} \\cdot d^{-1}) = (a \\cdot c) \\cdot (b \\cdot d)^{-1} = \\frac{a \\cdot c}{b \\cdot d}$\n\n"
            "(אסוציאטיביות וקומוטטיביות הכפל; $b^{-1} \\cdot d^{-1} = (bd)^{-1}$ מההגדרה). $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_linear_equation_solution",
        claim_id="thm_linear_equation_solution",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["ax_addition_associativity", "ax_additive_inverse",
                      "ax_additive_identity", "ax_multiplicative_inverse",
                      "ax_multiplication_associativity", "ax_multiplicative_identity",
                      "thm_no_zero_divisors", "def_subtraction", "def_division"],
        body=(
            "**קיום:** $a \\cdot \\left(-\\frac{b}{a}\\right) + b = -\\frac{a \\cdot b}{a} + b = -b + b = 0$.\n\n"
            "**יחידות:** אם $a x_1 + b = 0 = a x_2 + b$, אז $a x_1 = a x_2$. מ-$a \\neq 0$ ומאי-קיום מחלקי אפס נקבל $x_1 = x_2$. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_inequality_negation_flips",
        claim_id="thm_inequality_negation_flips",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["ax_addition_preserves_order", "ax_addition_associativity",
                      "ax_addition_commutativity", "ax_additive_inverse", "ax_additive_identity"],
        body=(
            "מ-$a < b$, נוסיף $-a - b$ לשני האגפים (לפי שימור סדר בחיבור):\n\n"
            "$a + (-a) + (-b) < b + (-a) + (-b)$, כלומר $-b < -a$ (לפי איבר נגדי וניטרלי). $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_reciprocal_flips_inequality",
        claim_id="thm_reciprocal_flips_inequality",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["ax_multiplicative_inverse", "ax_positive_multiplication_preserves_order",
                      "ax_multiplication_associativity", "ax_multiplicative_identity",
                      "thm_zero_lt_one"],
        body=(
            "מ-$a > 0$ ו-$b > 0$ נובע ש-$ab > 0$ ולכן $\\frac{1}{ab} > 0$. נכפול את $a < b$ ב-$\\frac{1}{ab}$ (חיובי):\n\n"
            "$a \\cdot \\frac{1}{ab} < b \\cdot \\frac{1}{ab}$, כלומר $\\frac{1}{b} < \\frac{1}{a}$. ושני האגפים חיוביים (הפכי של חיובי חיובי). $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_triangle_angle_sum",
        claim_id="thm_triangle_angle_sum",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["ax_euclid_parallel_postulate", "def_triangle", "def_angle"],
        body=(
            "יהי $\\triangle ABC$. נעביר דרך $A$ ישר מקביל לצלע $BC$ (לפי אקסיומת המקבילים).\n\n"
            "שלוש הזוויות לאורך הישר העליון ב-$A$ — זווית הקודקוד של $A$ במשולש ושתי הזוויות שמשמאלה ומימינה — סוכמות ל-$180°$ (זוויות לאורך ישר).\n\n"
            "שתי הזוויות הצדדיות שוות לזוויות $B$ ו-$C$ במשולש (זוויות מתחלפות בין מקבילים), ולכן $\\angle A + \\angle B + \\angle C = 180°$. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_pythagoras",
        claim_id="thm_pythagoras",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_right_triangle", "def_triangle",
                      "thm_triangle_angle_sum", "thm_square_nonnegative",
                      "ax_distributive_law", "thm_right_distributive_law",
                      "ax_addition_commutativity"],
        body=(
            "הוכחה גאומטרית-אלגברית (סידור ריבועים):\n\n"
            "ניקח ריבוע עם צלע $a + b$. נסדר בתוכו ארבעה משולשים ישרי-זווית חופפים (ניצבים $a, b$, יתר $c$) כך שיתריהם יוצרים ריבוע פנימי עם צלע $c$.\n\n"
            "**חישוב שטח הריבוע הגדול בשתי דרכים:**\n\n"
            "1. $(a + b)^2 = a^2 + 2ab + b^2$ (פתיחת בינום).\n\n"
            "2. שטח 4 משולשים + ריבוע פנימי = $4 \\cdot \\frac{ab}{2} + c^2 = 2ab + c^2$.\n\n"
            "השוואה: $a^2 + 2ab + b^2 = 2ab + c^2$, ולכן $a^2 + b^2 = c^2$. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_linear_function_unique_zero",
        claim_id="thm_linear_function_unique_zero",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_linear_function", "thm_linear_equation_solution"],
        body=(
            "אפס של $f$ הוא $x$ המקיים $f(x) = 0$, כלומר $a x + b = 0$. \n\n"
            "לפי משפט פתרון משוואה לינארית, עם $a \\neq 0$, הפתרון היחיד הוא $x = -\\frac{b}{a}$. $\\blacksquare$"
        ),
    ),
]


# ─────────────────────────────────────────────────────────────────
# Chunk 4 — HS 3-unit: roots, polynomials, quadratics, geometry
# ─────────────────────────────────────────────────────────────────

COURSES_CHUNK4 = [
    Course(
        id="math_hs_3",
        name="מתמטיקה תיכון 3 יחל",
        prerequisites=["math_jhs"],
    ),
]

_HS3 = "math_hs_3"

CLAIMS_CHUNK4 = [
    # ─── Roots & rational exponents ───
    Claim(
        id="def_nth_root", kind="definition", status=CANON,
        course=_HS3, topic="חזקות ושורשים",
        statement=r"**שורש מסדר $n$:** עבור $a \geq 0$ ו-$n \in \mathbb{N}, n \geq 1$, השורש $\sqrt[n]{a}$ הוא המספר $x \geq 0$ היחיד המקיים $x^n = a$.",
    ),
    Claim(
        id="def_square_root", kind="definition", status=CANON,
        course=_HS3, topic="חזקות ושורשים",
        statement=r"**שורש ריבועי:** $\sqrt{a} := \sqrt[2]{a}$ — המספר האי-שלילי שריבועו $a$ (עבור $a \geq 0$).",
    ),
    Claim(
        id="thm_sqrt_of_product", kind="theorem", status=CANON,
        course=_HS3, topic="חזקות ושורשים",
        statement=r"**שורש של מכפלה:** $\sqrt{a \cdot b} = \sqrt{a} \cdot \sqrt{b}$ לכל $a, b \geq 0$.",
    ),
    Claim(
        id="def_rational_exponent", kind="definition", status=CANON,
        course=_HS3, topic="חזקות ושורשים",
        statement=r"**חזקה רציונלית:** עבור $a > 0$ ו-$\frac{p}{q} \in \mathbb{Q}$ (עם $q > 0$), מגדירים $a^{p/q} := \sqrt[q]{a^p}$.",
    ),
    Claim(
        id="thm_rational_exponent_addition", kind="theorem", status=CANON,
        course=_HS3, topic="חזקות ושורשים",
        statement=r"**חיבור מעריכים רציונליים:** $a^r \cdot a^s = a^{r+s}$ לכל $a > 0$ ו-$r, s \in \mathbb{Q}$.",
    ),

    # ─── Polynomials ───
    Claim(
        id="def_polynomial", kind="definition", status=CANON,
        course=_HS3, topic="פולינומים",
        statement=r"**פולינום:** ביטוי מהצורה $p(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0$ עבור מקדמים $a_0, \ldots, a_n \in \mathbb{R}$.",
    ),
    Claim(
        id="def_polynomial_degree", kind="definition", status=CANON,
        course=_HS3, topic="פולינומים",
        statement=r"**דרגת פולינום:** הדרגה של פולינום $p(x) = a_n x^n + \cdots + a_0$ היא ה-$n$ הגדול ביותר שעבורו $a_n \neq 0$. דרגת פולינום האפס מוגדרת בנפרד (לעיתים $-\infty$).",
    ),
    Claim(
        id="thm_polynomial_addition_degree", kind="theorem", status=CANON,
        course=_HS3, topic="פולינומים",
        statement=r"**דרגת סכום פולינומים:** $\deg(p + q) \leq \max(\deg p, \deg q)$. שוויון מתקיים אם המקדמים המובילים אינם מתאפסים בסכום.",
    ),
    Claim(
        id="thm_polynomial_multiplication_degree", kind="theorem", status=CANON,
        course=_HS3, topic="פולינומים",
        statement=r"**דרגת מכפלת פולינומים:** $\deg(p \cdot q) = \deg p + \deg q$ (לפולינומים שאינם פולינום האפס).",
    ),
    Claim(
        id="thm_remainder_theorem", kind="theorem", status=CANON,
        course=_HS3, topic="פולינומים",
        statement=r"**משפט השארית:** השארית בחילוק פולינום $p(x)$ ב-$(x - a)$ שווה ל-$p(a)$.",
    ),
    Claim(
        id="thm_factor_theorem", kind="theorem", status=CANON,
        course=_HS3, topic="פולינומים",
        statement=r"**משפט הגורם:** $(x - a)$ הוא גורם של $p(x)$ אם ורק אם $p(a) = 0$.",
    ),

    # ─── Quadratics ───
    Claim(
        id="def_quadratic_function", kind="definition", status=CANON,
        course=_HS3, topic="פונקציה ריבועית",
        statement=r"**פונקציה ריבועית:** $f(x) = a x^2 + b x + c$ עבור $a, b, c \in \mathbb{R}$ קבועים ו-$a \neq 0$.",
    ),
    Claim(
        id="def_discriminant", kind="definition", status=CANON,
        course=_HS3, topic="פונקציה ריבועית",
        statement=r"**דיסקרימיננטה:** $\Delta := b^2 - 4ac$ עבור משוואה ריבועית $a x^2 + b x + c = 0$.",
    ),
    Claim(
        id="thm_quadratic_vertex", kind="theorem", status=CANON,
        course=_HS3, topic="פונקציה ריבועית",
        statement=r"**קודקוד הפרבולה:** לפונקציה הריבועית $f(x) = a x^2 + b x + c$ נקודת קיצון יחידה ב-$x = -\frac{b}{2a}$, בערך $f\!\left(-\frac{b}{2a}\right) = c - \frac{b^2}{4a}$.",
    ),
    Claim(
        id="thm_quadratic_formula", kind="theorem", status=CANON,
        course=_HS3, topic="פונקציה ריבועית",
        statement=r"**הנוסחה הריבועית:** למשוואה $a x^2 + b x + c = 0$ עם $a \neq 0$ ו-$\Delta \geq 0$ הפתרונות הם $x = \frac{-b \pm \sqrt{\Delta}}{2a}$.",
    ),
    Claim(
        id="thm_discriminant_roots_count", kind="theorem", status=CANON,
        course=_HS3, topic="פונקציה ריבועית",
        statement=r"**הדיסקרימיננטה קובעת את מספר הפתרונות:** למשוואה ריבועית עם $a \neq 0$: אם $\Delta > 0$ יש שני פתרונות ממשיים שונים; אם $\Delta = 0$ יש פתרון יחיד (כפול); אם $\Delta < 0$ אין פתרונות ממשיים.",
    ),
    Claim(
        id="thm_vieta_formulas", kind="theorem", status=CANON,
        course=_HS3, topic="פונקציה ריבועית",
        statement=r"**נוסחאות וייטה (ריבועי):** אם $x_1, x_2$ הם שורשי $a x^2 + b x + c = 0$ (עם $a \neq 0$), אז $x_1 + x_2 = -\frac{b}{a}$ ו-$x_1 \cdot x_2 = \frac{c}{a}$.",
    ),
    Claim(
        id="thm_factoring_quadratic", kind="theorem", status=CANON,
        course=_HS3, topic="פונקציה ריבועית",
        statement=r"**פירוק טרינום ריבועי:** אם $x_1, x_2$ הם שורשי $a x^2 + b x + c$, אז $a x^2 + b x + c = a(x - x_1)(x - x_2)$.",
    ),

    # ─── Geometry: congruence, similarity, circle ───
    Claim(
        id="def_congruent_triangles", kind="definition", status=CANON,
        course=_HS3, topic="חפיפה ודמיון",
        statement=r"**משולשים חופפים:** שני משולשים נקראים **חופפים** אם קיימת התאמה בין הקודקודים שתחתיה הצלעות המתאימות שוות באורכן והזוויות המתאימות שוות בגודלן.",
    ),
    Claim(
        id="def_similar_triangles", kind="definition", status=CANON,
        course=_HS3, topic="חפיפה ודמיון",
        statement=r"**משולשים דומים:** שני משולשים נקראים **דומים** אם הזוויות המתאימות שוות והצלעות המתאימות פרופורציונליות (יחס קבוע).",
    ),
    Claim(
        id="ax_sas_congruence", kind="axiom", status=CANON,
        course=_HS3, topic="חפיפה ודמיון",
        statement=r"**צ.ז.צ (SAS):** אם בשני משולשים שתי צלעות והזווית הכלואה ביניהן שוות בהתאמה — המשולשים חופפים.",
    ),
    Claim(
        id="ax_asa_congruence", kind="axiom", status=CANON,
        course=_HS3, topic="חפיפה ודמיון",
        statement=r"**ז.צ.ז (ASA):** אם בשני משולשים שתי זוויות והצלע הכלואה ביניהן שוות בהתאמה — המשולשים חופפים.",
    ),
    Claim(
        id="ax_sss_congruence", kind="axiom", status=CANON,
        course=_HS3, topic="חפיפה ודמיון",
        statement=r"**צ.צ.צ (SSS):** אם בשני משולשים שלוש הצלעות שוות בהתאמה — המשולשים חופפים.",
    ),
    Claim(
        id="thm_aa_similarity", kind="theorem", status=CANON,
        course=_HS3, topic="חפיפה ודמיון",
        statement=r"**דמיון לפי שתי זוויות (AA):** אם בשני משולשים שתי זוויות שוות בהתאמה — המשולשים דומים.",
    ),
    Claim(
        id="thm_isosceles_triangle_base_angles", kind="theorem", status=CANON,
        course=_HS3, topic="חפיפה ודמיון",
        statement=r"**זוויות בסיס במשולש שווה-שוקיים:** במשולש שווה-שוקיים, הזוויות שמול שתי הצלעות השוות שוות.",
    ),
    Claim(
        id="def_circle", kind="definition", status=CANON,
        course=_HS3, topic="גאומטריה",
        statement=r"**מעגל:** אוסף כל הנקודות במישור שמרחקן מנקודה קבועה (הנקראת **מרכז המעגל**) שווה למספר חיובי קבוע (הנקרא **רדיוס**).",
    ),
    Claim(
        id="thm_inscribed_angle_theorem", kind="theorem", status=CANON,
        course=_HS3, topic="גאומטריה",
        statement=r"**משפט הזווית ההיקפית:** זווית היקפית במעגל שווה למחצית הזווית המרכזית הנשענת על אותה קשת.",
    ),
    Claim(
        id="thm_triangle_inequality_geometry", kind="theorem", status=CANON,
        course=_HS3, topic="גאומטריה",
        statement=r"**אי-שוויון המשולש (גאומטרי):** בכל משולש, סכום אורכי שתי צלעות גדול מאורך הצלע השלישית.",
    ),
    Claim(
        id="thm_pythagoras_converse", kind="theorem", status=CANON,
        course=_HS3, topic="גאומטריה",
        statement=r"**הפכי משפט פיתגורס:** במשולש עם צלעות באורכים $a, b, c$, אם $a^2 + b^2 = c^2$ אז המשולש הוא ישר-זווית והזווית מול $c$ היא $90°$.",
    ),
]


PROOFS_CHUNK4 = [
    Proof(
        id="prf_sqrt_of_product",
        claim_id="thm_sqrt_of_product",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_square_root", "thm_power_of_product",
                      "def_natural_power", "ax_multiplication_commutativity",
                      "thm_square_nonnegative"],
        body=(
            "$(\\sqrt{a} \\cdot \\sqrt{b})^2 = (\\sqrt{a})^2 \\cdot (\\sqrt{b})^2 = a \\cdot b$ (לפי חזקה של מכפלה והגדרת השורש).\n\n"
            "$\\sqrt{a} \\cdot \\sqrt{b} \\geq 0$ כי שני הגורמים אי-שליליים. גם $\\sqrt{ab}$ הוא המספר היחיד האי-שלילי שריבועו $ab$. מיחידות השורש: $\\sqrt{a} \\cdot \\sqrt{b} = \\sqrt{ab}$. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_rational_exponent_addition",
        claim_id="thm_rational_exponent_addition",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_rational_exponent", "def_nth_root",
                      "thm_power_addition_rule", "thm_power_multiplication_rule"],
        body=(
            "נסמן $r = p/q$ ו-$s = m/n$. נחבר במכנה משותף: $r + s = (pn + qm)/(qn)$.\n\n"
            "$a^r \\cdot a^s = \\sqrt[qn]{a^{pn}} \\cdot \\sqrt[qn]{a^{qm}} = \\sqrt[qn]{a^{pn} \\cdot a^{qm}} = \\sqrt[qn]{a^{pn + qm}} = a^{(pn+qm)/(qn)} = a^{r+s}$\n\n"
            "(תוך שימוש בחוקי חזקות הטבעיים והגדרת השורש מסדר $n$). $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_polynomial_addition_degree",
        claim_id="thm_polynomial_addition_degree",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_polynomial", "def_polynomial_degree"],
        body=(
            "נסמן $\\deg p = m$, $\\deg q = n$, ובלי הגבלת כלליות $m \\geq n$.\n\n"
            "בסכום $p + q$, מקדם $x^k$ עבור $k > m$ הוא $0$ (כי $p$ ו-$q$ אינן מכילות חזקות גבוהות מ-$m$). לכן $\\deg(p+q) \\leq m$.\n\n"
            "שוויון מתקיים כאשר $m > n$ (המקדם המוביל של $p$ נשמר), או כאשר $m = n$ והמקדמים המובילים לא מתבטלים בסכום. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_polynomial_multiplication_degree",
        claim_id="thm_polynomial_multiplication_degree",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_polynomial", "def_polynomial_degree",
                      "thm_no_zero_divisors"],
        body=(
            "נסמן $p(x) = a_m x^m + \\ldots$ (עם $a_m \\neq 0$), $q(x) = b_n x^n + \\ldots$ (עם $b_n \\neq 0$). \n\n"
            "במכפלה $p \\cdot q$, המקדם של $x^{m+n}$ הוא $a_m \\cdot b_n$, ולפי אי-קיום מחלקי אפס $a_m \\cdot b_n \\neq 0$. אין מקדם של חזקה גבוהה יותר. לכן $\\deg(p \\cdot q) = m + n$. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_remainder_theorem",
        claim_id="thm_remainder_theorem",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_polynomial", "thm_polynomial_multiplication_degree"],
        body=(
            "מאלגוריתם החילוק של פולינומים: $p(x) = (x - a) \\cdot Q(x) + R(x)$ עם $\\deg R < \\deg(x - a) = 1$, כלומר $R$ הוא קבוע $r$.\n\n"
            "נציב $x = a$: $p(a) = (a - a) \\cdot Q(a) + r = 0 + r = r$. \n\n"
            "לכן השארית $r = p(a)$. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_factor_theorem",
        claim_id="thm_factor_theorem",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["thm_remainder_theorem"],
        body=(
            "($\\Leftarrow$) אם $p(a) = 0$, אז לפי משפט השארית השארית בחילוק ב-$(x - a)$ היא $0$, כלומר $(x - a)$ מחלק את $p$.\n\n"
            "($\\Rightarrow$) אם $(x - a)$ מחלק את $p$, כלומר $p(x) = (x - a) \\cdot Q(x)$, אז $p(a) = (a - a) \\cdot Q(a) = 0$. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_quadratic_vertex",
        claim_id="thm_quadratic_vertex",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_quadratic_function", "ax_distributive_law",
                      "def_natural_power", "thm_difference_of_squares",
                      "thm_square_nonnegative"],
        body=(
            "השלמת ריבוע: \n\n"
            "$f(x) = a x^2 + b x + c = a\\!\\left(x^2 + \\tfrac{b}{a} x\\right) + c = a\\!\\left(x + \\tfrac{b}{2a}\\right)^2 - \\tfrac{b^2}{4a} + c$\n\n"
            "מאחר ש-$(x + \\tfrac{b}{2a})^2 \\geq 0$ עם שוויון רק עבור $x = -\\tfrac{b}{2a}$, הקיצון של $f$ מתקבל ב-$x = -\\tfrac{b}{2a}$, בערך $c - \\tfrac{b^2}{4a}$. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_quadratic_formula",
        claim_id="thm_quadratic_formula",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_quadratic_function", "def_discriminant",
                      "def_square_root", "thm_quadratic_vertex",
                      "thm_linear_equation_solution"],
        body=(
            "מהשלמת ריבוע (כמו במשפט קודקוד הפרבולה): $a x^2 + b x + c = 0$ שקול ל-$a\\!\\left(x + \\tfrac{b}{2a}\\right)^2 = \\tfrac{b^2 - 4ac}{4a} = \\tfrac{\\Delta}{4a}$.\n\n"
            "נחלק ב-$a$ ונוציא שורש: $x + \\tfrac{b}{2a} = \\pm \\tfrac{\\sqrt{\\Delta}}{2a}$ (כש-$\\Delta \\geq 0$).\n\n"
            "מכאן $x = \\tfrac{-b \\pm \\sqrt{\\Delta}}{2a}$. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_discriminant_roots_count",
        claim_id="thm_discriminant_roots_count",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["thm_quadratic_formula", "def_discriminant",
                      "def_square_root", "ax_order_trichotomy"],
        body=(
            "לפי הנוסחה הריבועית $x = \\tfrac{-b \\pm \\sqrt{\\Delta}}{2a}$:\n\n"
            "- אם $\\Delta > 0$: $\\sqrt{\\Delta} > 0$, ולכן $+\\sqrt{\\Delta}$ ו-$-\\sqrt{\\Delta}$ נותנים שני פתרונות שונים.\n\n"
            "- אם $\\Delta = 0$: $\\sqrt{\\Delta} = 0$, ולכן $+0$ ו-$-0$ זה אותו פתרון $x = -\\tfrac{b}{2a}$ (פתרון יחיד, נקרא 'כפול').\n\n"
            "- אם $\\Delta < 0$: השורש $\\sqrt{\\Delta}$ אינו ממשי, לכן אין פתרון ממשי. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_vieta_formulas",
        claim_id="thm_vieta_formulas",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["thm_quadratic_formula", "def_discriminant",
                      "ax_addition_commutativity", "thm_difference_of_squares"],
        body=(
            "מהנוסחה הריבועית $x_{1,2} = \\tfrac{-b \\pm \\sqrt{\\Delta}}{2a}$:\n\n"
            "$x_1 + x_2 = \\tfrac{-b + \\sqrt{\\Delta}}{2a} + \\tfrac{-b - \\sqrt{\\Delta}}{2a} = \\tfrac{-2b}{2a} = -\\tfrac{b}{a}$.\n\n"
            "$x_1 \\cdot x_2 = \\tfrac{(-b)^2 - (\\sqrt{\\Delta})^2}{(2a)^2} = \\tfrac{b^2 - \\Delta}{4a^2} = \\tfrac{b^2 - (b^2 - 4ac)}{4a^2} = \\tfrac{4ac}{4a^2} = \\tfrac{c}{a}$. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_factoring_quadratic",
        claim_id="thm_factoring_quadratic",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["thm_vieta_formulas", "ax_distributive_law",
                      "thm_right_distributive_law", "def_subtraction"],
        body=(
            "נפתח: $a(x - x_1)(x - x_2) = a(x^2 - (x_1 + x_2) x + x_1 x_2)$\n\n"
            "$= a x^2 - a(x_1 + x_2) x + a x_1 x_2 = a x^2 - a \\cdot \\left(-\\tfrac{b}{a}\\right) x + a \\cdot \\tfrac{c}{a} = a x^2 + b x + c$\n\n"
            "(בשלב האחרון, נוסחאות וייטה). $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_aa_similarity",
        claim_id="thm_aa_similarity",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_similar_triangles", "thm_triangle_angle_sum"],
        body=(
            "אם שתי זוויות בשני משולשים שוות בהתאמה, אז גם הזווית השלישית שווה (כי סכום הזוויות במשולש $180°$).\n\n"
            "כך כל שלוש הזוויות המתאימות שוות. ניתן להראות (באמצעות בניית משולש דומה והפעלת SAS או SSS) שיחס הצלעות המתאימות קבוע. לכן המשולשים דומים. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_isosceles_triangle_base_angles",
        claim_id="thm_isosceles_triangle_base_angles",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_triangle", "ax_sas_congruence", "def_congruent_triangles"],
        body=(
            "יהי $\\triangle ABC$ עם $AB = AC$. נחלק את זווית $A$ בחצי על ידי הקטע $AD$ שיורד ל-$BC$.\n\n"
            "במשולשים $\\triangle ABD$ ו-$\\triangle ACD$: $AB = AC$ (נתון), $\\angle BAD = \\angle CAD$ (חציית הזווית), והצלע $AD$ משותפת. לפי צ.ז.צ — המשולשים חופפים.\n\n"
            "מכאן זוויות הבסיס $\\angle B = \\angle C$ (זוויות מתאימות במשולשים חופפים). $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_inscribed_angle_theorem",
        claim_id="thm_inscribed_angle_theorem",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_circle", "thm_isosceles_triangle_base_angles",
                      "thm_triangle_angle_sum"],
        body=(
            "ננתח שלושה מקרים לפי מיקום המרכז $O$ ביחס לזווית ההיקפית $\\angle APB$:\n\n"
            "**מקרה 1 (המרכז על אחת מהקרניים):** $\\triangle OAP$ שווה שוקיים ($OA = OP$ רדיוסים). זווית חיצונית של $\\triangle OAP$ ב-$O$ שווה לסכום הזוויות הפנימיות הלא-סמוכות = $2 \\angle APO$. זו הזווית המרכזית, לכן $\\angle AOB = 2 \\angle APB$.\n\n"
            "**מקרה 2 (המרכז בתוך הזווית):** נעביר את הקטע $PO$ ונחלק את הזווית ההיקפית לשתי חלקים, כל אחד לפי מקרה 1. סיכום נותן את התוצאה.\n\n"
            "**מקרה 3 (המרכז מחוץ):** אותה טכניקה, חיסור במקום חיבור. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_triangle_inequality_geometry",
        claim_id="thm_triangle_inequality_geometry",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["def_triangle", "thm_isosceles_triangle_base_angles"],
        body=(
            "במשולש $\\triangle ABC$ נראה $AB + BC > AC$.\n\n"
            "נאריך את $AB$ עד נקודה $D$ כך ש-$BD = BC$, כך ש-$AD = AB + BC$.\n\n"
            "$\\triangle BCD$ שווה שוקיים, לכן $\\angle BDC = \\angle BCD$. הזווית $\\angle ACD$ גדולה מ-$\\angle BCD = \\angle BDC = \\angle ADC$.\n\n"
            "במשולש $\\triangle ACD$: מול הזווית הגדולה יותר הצלע גדולה יותר. כלומר $AD > AC$, ולכן $AB + BC > AC$. $\\blacksquare$"
        ),
    ),
    Proof(
        id="prf_pythagoras_converse",
        claim_id="thm_pythagoras_converse",
        method="informal", status="reviewed", is_canonical=True,
        dependencies=["thm_pythagoras", "ax_sss_congruence", "def_right_triangle"],
        body=(
            "יהי $\\triangle ABC$ עם $a^2 + b^2 = c^2$. נבנה משולש עזר $\\triangle A'B'C'$ ישר-זווית ב-$C'$ עם ניצבים באורכים $a, b$.\n\n"
            "לפי משפט פיתגורס היתר של $\\triangle A'B'C'$ הוא $\\sqrt{a^2 + b^2} = c$.\n\n"
            "אז ל-$\\triangle ABC$ ול-$\\triangle A'B'C'$ שלוש הצלעות שוות. לפי צ.צ.צ הם חופפים, בפרט $\\angle C = \\angle C' = 90°$. $\\blacksquare$"
        ),
    ),
]


# ─────────────────────────────────────────────────────────────────
# Orchestration
# ─────────────────────────────────────────────────────────────────

def main() -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / "claims").mkdir(exist_ok=True)
    (DATA / "proofs").mkdir(exist_ok=True)
    (DATA / "courses").mkdir(exist_ok=True)
    if not (DATA / "SCHEMA_VERSION").exists():
        (DATA / "SCHEMA_VERSION").write_text("1\n", encoding="utf-8")

    def write_if_new(obj, exists_fn, save_fn, kind: str) -> bool:
        if exists_fn(DATA, obj.id) is not None:
            return False
        save_fn(obj, DATA)
        return True

    all_courses = (COURSES_CHUNK1 + COURSES_CHUNK2 + COURSES_CHUNK3
                   + COURSES_CHUNK4 + COURSES_CHUNK5 + COURSES_CHUNK6
                   + COURSES_CHUNK7 + COURSES_BF + COURSES_CHUNK8
                   + COURSES_CHUNK9 + COURSES_CHUNK10 + COURSES_UNI)
    all_claims = (CLAIMS_CHUNK1 + CLAIMS_CHUNK2 + CLAIMS_CHUNK3
                  + CLAIMS_CHUNK4 + CLAIMS_CHUNK5 + CLAIMS_CHUNK6
                  + CLAIMS_CHUNK7 + CLAIMS_BF + CLAIMS_CHUNK8
                  + CLAIMS_CHUNK9 + CLAIMS_CHUNK10)
    all_proofs = (PROOFS_CHUNK1 + PROOFS_CHUNK2 + PROOFS_CHUNK3
                  + PROOFS_CHUNK4 + PROOFS_CHUNK5 + PROOFS_CHUNK6
                  + PROOFS_CHUNK7 + PROOFS_BF + PROOFS_CHUNK8
                  + PROOFS_CHUNK9 + PROOFS_CHUNK10)

    n_courses = sum(write_if_new(c, files.load_course, files.save_course, "course")
                    for c in all_courses)
    n_claims = sum(write_if_new(c, files.load_claim, files.save_claim, "claim")
                   for c in all_claims)
    n_proofs = sum(write_if_new(p, files.load_proof, files.save_proof, "proof")
                   for p in all_proofs)

    print(f"courses: {n_courses} new (of {len(all_courses)})")
    print(f"claims:  {n_claims} new (of {len(all_claims)})")
    print(f"proofs:  {n_proofs} new (of {len(all_proofs)})")

    # Re-classify claims whose topic belongs to a university course.
    moved, by_target = migrate_claims_to_uni_courses(DATA)
    if moved:
        print(f"reclassified {moved} claims to university courses:")
        for target, n in sorted(by_target.items()):
            print(f"  {n:>4} -> {target}")

    index.rebuild_index(DATA, DB)
    print(f"index rebuilt at {DB}")


if __name__ == "__main__":
    main()
