"""Audit fix phase 1 — 11 HIGH severity corrections + 5 new prerequisite theorems.

Generated from the parallel multi-agent audit (105 confirmed findings, 0 refuted).
This chunk:
  • Adds 5 missing foundational claims that several HS/uni proofs implicitly use.
  • Adds 5 new proofs (one per non-axiom new claim).
  • Provides REPLACE_PROOFS list + apply_replace_proofs() to OVERWRITE the 11
    proofs whose declared dependencies didn't match what their bodies actually use.

The audit also flagged 42 medium + 53 low findings — those land in a later chunk.
"""
from __future__ import annotations

from pathlib import Path

from core.models import Claim, Proof
from storage import files


CANON = "canonical"


def C(cid, kind, course, topic, stmt):
    return Claim(id=cid, kind=kind, status=CANON, course=course, topic=topic, statement=stmt)


def P(pid, cid, deps, body, method="informal", status="reviewed"):
    return Proof(id=pid, claim_id=cid, method=method, status=status,
                 is_canonical=True, dependencies=deps, body=body)


# ─────────────────────────────────────────────────────────────────
# New prerequisite claims
# ─────────────────────────────────────────────────────────────────

CLAIMS = [
    # 1. Used by prf_difference_of_squares — (-a) * b = -(a*b), the basic
    #    "negative times positive" rule (distinct from -a * -b = ab).
    C("thm_negative_times_positive_basic", "theorem",
      "math_elementary", "אלגברה בסיסית",
      r"**מינוס חיובי שלילי (זהות):** לכל $a, b \in \mathbb{R}$ מתקיים $(-a) \cdot b = -(a \cdot b)$."),

    # 2. Used by prf_circle_general_form — completing the square.
    C("thm_completing_the_square", "theorem",
      "math_hs_3", "זהויות אלגבריות",
      r"**השלמת ריבוע:** לכל $x \in \mathbb{R}$ ולכל $b \in \mathbb{R}$ מתקיים $x^2 + b x = \left(x + \tfrac{b}{2}\right)^2 - \tfrac{b^2}{4}$."),

    # 3. Used by prf_remainder_theorem — polynomial division algorithm.
    C("thm_polynomial_division_algorithm", "theorem",
      "math_hs_3", "פולינומים",
      r"**אלגוריתם החילוק לפולינומים:** לכל פולינומים $p(x), d(x)$ עם $\deg d \geq 1$, קיימים פולינומים יחידים $q(x), r(x)$ כך ש-$p(x) = q(x) \cdot d(x) + r(x)$ ו-$\deg r < \deg d$ (או $r \equiv 0$)."),

    # 4. Used by prf_perpendicular_diameter_bisects_chord — Hypotenuse-Leg
    #    congruence (axiom: standard congruence criterion taught alongside SSS).
    C("ax_hl_congruence", "axiom",
      "math_hs_3", "חפיפה ודמיון",
      r"**חפיפת היפוטנוזה-ניצב (יתר-ניצב):** אם בשני משולשים ישרי-זווית היתר ואחד הניצבים שווים, אזי המשולשים חופפים."),

    # 5. Used by prf_derangement_formula — general n-set inclusion-exclusion.
    C("thm_inclusion_exclusion_general", "theorem",
      "math_uni_advanced_algebra", "קומבינטוריקה מתקדמת",
      r"**עקרון ההכלה וההפרדה הכללי:** לכל קבוצות סופיות $A_1, A_2, \ldots, A_n$ מתקיים $\left|\bigcup_{i=1}^{n} A_i\right| = \sum_{k=1}^{n} (-1)^{k+1} \sum_{1 \leq i_1 < \cdots < i_k \leq n} |A_{i_1} \cap \cdots \cap A_{i_k}|$."),
]


# ─────────────────────────────────────────────────────────────────
# Proofs for new claims (HL stays an axiom — no proof needed)
# ─────────────────────────────────────────────────────────────────

PROOFS = [
    P("prf_negative_times_positive_basic", "thm_negative_times_positive_basic",
      ["ax_distributive_law", "ax_additive_inverse", "ax_additive_identity",
       "thm_multiplication_by_zero", "thm_additive_inverse_uniqueness"],
      "נראה ש-$(-a) \\cdot b$ הוא הנגדי של $a \\cdot b$, ומיחידות הנגדי ינבע ש-$(-a) \\cdot b = -(a \\cdot b)$.\n\n"
      "$(-a) \\cdot b + a \\cdot b = ((-a) + a) \\cdot b$ (חוק הפילוג הימני — או הימני המוכח)\n\n"
      "$= 0 \\cdot b$ (לפי איבר נגדי)\n\n"
      "$= 0$ (משפט אפס בכפל).\n\n"
      "לכן $(-a) \\cdot b$ הוא הנגדי של $a \\cdot b$, ומיחידות הנגדי $(-a) \\cdot b = -(a \\cdot b)$. $\\blacksquare$"),

    P("prf_completing_the_square", "thm_completing_the_square",
      ["def_natural_power", "ax_distributive_law", "thm_right_distributive_law",
       "ax_addition_commutativity", "ax_addition_associativity",
       "thm_addition_undoes_subtraction"],
      "נחשב את $\\left(x + \\tfrac{b}{2}\\right)^2$:\n\n"
      "$\\left(x + \\tfrac{b}{2}\\right)^2 = \\left(x + \\tfrac{b}{2}\\right) \\cdot \\left(x + \\tfrac{b}{2}\\right)$\n\n"
      "$= x \\cdot x + x \\cdot \\tfrac{b}{2} + \\tfrac{b}{2} \\cdot x + \\tfrac{b}{2} \\cdot \\tfrac{b}{2}$ (פילוג דו-צדדי)\n\n"
      "$= x^2 + 2 \\cdot \\tfrac{b}{2} \\cdot x + \\tfrac{b^2}{4}$ (קומוטטיביות וצמצום)\n\n"
      "$= x^2 + b x + \\tfrac{b^2}{4}$.\n\n"
      "נחסר $\\tfrac{b^2}{4}$ משני האגפים: $x^2 + b x = \\left(x + \\tfrac{b}{2}\\right)^2 - \\tfrac{b^2}{4}$. $\\blacksquare$"),

    P("prf_polynomial_division_algorithm", "thm_polynomial_division_algorithm",
      ["def_polynomial", "thm_polynomial_multiplication_degree"],
      "**קיום (אינדוקציה על $\\deg p$):**\n\n"
      "**בסיס:** אם $\\deg p < \\deg d$, ניקח $q \\equiv 0$ ו-$r \\equiv p$. אז $p = 0 \\cdot d + p$ ו-$\\deg r = \\deg p < \\deg d$.\n\n"
      "**צעד:** נניח שהמשפט נכון לכל פולינום מדרגה קטנה מ-$n$, ויהי $\\deg p = n \\geq \\deg d$. נסמן $p(x) = a_n x^n + \\ldots$ ו-$d(x) = b_m x^m + \\ldots$ עם $b_m \\neq 0$. הפולינום $\\tilde p(x) := p(x) - \\tfrac{a_n}{b_m} x^{n-m} \\cdot d(x)$ מבטל את אבר ה-$x^n$, ולכן $\\deg \\tilde p < n$. לפי הנחת האינדוקציה $\\tilde p = \\tilde q \\cdot d + r$ עם $\\deg r < \\deg d$, ואז $p = \\left(\\tfrac{a_n}{b_m} x^{n-m} + \\tilde q\\right) \\cdot d + r$.\n\n"
      "**יחידות:** אם $p = q_1 d + r_1 = q_2 d + r_2$, אז $(q_1 - q_2) d = r_2 - r_1$. דרגת אגף שמאל לפחות $\\deg d$ (אם $q_1 \\neq q_2$), אך דרגת אגף ימין קטנה מ-$\\deg d$. סתירה, אלא אם $q_1 = q_2$, וממילא $r_1 = r_2$. $\\blacksquare$"),

    P("prf_inclusion_exclusion_general", "thm_inclusion_exclusion_general",
      ["def_proof_by_induction", "thm_inclusion_exclusion_two_sets"],
      "**אינדוקציה על $n$.**\n\n"
      "**בסיס $n = 2$:** זה בדיוק עקרון ההכלה וההפרדה לשתי קבוצות: $|A_1 \\cup A_2| = |A_1| + |A_2| - |A_1 \\cap A_2|$.\n\n"
      "**צעד $n \\to n+1$:** נסמן $B := A_1 \\cup \\cdots \\cup A_n$. מבסיס $n=2$:\n\n"
      "$|B \\cup A_{n+1}| = |B| + |A_{n+1}| - |B \\cap A_{n+1}|$.\n\n"
      "לפי הנחת האינדוקציה, $|B|$ נתון בידי הנוסחה ל-$n$ קבוצות. עבור $B \\cap A_{n+1} = \\bigcup_{i=1}^{n} (A_i \\cap A_{n+1})$, גם הוא איחוד של $n$ קבוצות, ולכן ניתן לפיתוח לפי הנחת האינדוקציה (כל איבר $|A_{i_1} \\cap \\cdots \\cap A_{i_k} \\cap A_{n+1}|$).\n\n"
      "חיבור שני הפיתוחים תוך הקפדה על סימן ה-$(-1)^{k+1}$ נותן בדיוק את הנוסחה ל-$n+1$ קבוצות: כל החיתוכים שאינם כוללים את $A_{n+1}$ מגיעים מ-$|B|$, החיתוכים שכוללים את $A_{n+1}$ מגיעים מ-$-|B \\cap A_{n+1}|$ (עם היפוך סימן שתואם את הנוסחה), והאיבר היחיד $|A_{n+1}|$ מתווסף בנפרד. $\\blacksquare$"),
]


# ─────────────────────────────────────────────────────────────────
# 11 corrected proofs — force-overwritten (existing proofs replaced)
# ─────────────────────────────────────────────────────────────────

REPLACE_PROOFS = [
    # FIX 1: prf_difference_of_squares used thm_product_of_negatives (-a*-b=ab),
    #        but the body actually applies (-x)*y = -(xy) twice. Swap to the
    #        new dedicated theorem.
    P("prf_difference_of_squares", "thm_difference_of_squares",
      ["def_natural_power", "def_subtraction",
       "ax_distributive_law", "thm_right_distributive_law",
       "ax_addition_commutativity", "ax_addition_associativity",
       "ax_additive_inverse", "ax_additive_identity",
       "thm_negative_times_positive_basic"],
      "$(a - b)(a + b) = (a + (-b))(a + b)$ (הגדרת חיסור)\n\n"
      "$= a \\cdot a + a \\cdot b + (-b) \\cdot a + (-b) \\cdot b$ (פילוג ימני ושמאלי)\n\n"
      "$= a^2 + ab + (-(ba)) + (-(b \\cdot b))$ (לפי מינוס חיובי שלילי)\n\n"
      "$= a^2 + ab - ab - b^2 = a^2 - b^2$ (קומוטטיביות, איבר נגדי, ואיבר ניטרלי). $\\blacksquare$"),

    # FIX 2: prf_circle_general_form claimed difference-of-squares but actually
    #        completes the square — use the new theorem.
    P("prf_circle_general_form", "thm_circle_general_form",
      ["thm_equation_of_circle", "thm_completing_the_square"],
      "נתונה משוואה כללית $x^2 + y^2 + Dx + Ey + F = 0$. נשלים ריבועים לכל אחד מהמשתנים בנפרד.\n\n"
      "לפי משפט השלמת ריבוע: $x^2 + Dx = \\left(x + \\tfrac{D}{2}\\right)^2 - \\tfrac{D^2}{4}$ ו-$y^2 + Ey = \\left(y + \\tfrac{E}{2}\\right)^2 - \\tfrac{E^2}{4}$.\n\n"
      "נציב במשוואה:\n\n"
      "$\\left(x + \\tfrac{D}{2}\\right)^2 - \\tfrac{D^2}{4} + \\left(y + \\tfrac{E}{2}\\right)^2 - \\tfrac{E^2}{4} + F = 0$\n\n"
      "$\\left(x + \\tfrac{D}{2}\\right)^2 + \\left(y + \\tfrac{E}{2}\\right)^2 = \\tfrac{D^2 + E^2 - 4F}{4}$.\n\n"
      "אם הצד הימני חיובי, זו משוואת מעגל עם מרכז $\\left(-\\tfrac{D}{2}, -\\tfrac{E}{2}\\right)$ ורדיוס $r = \\tfrac{1}{2}\\sqrt{D^2 + E^2 - 4F}$. אם הוא אפס המעגל מנוון לנקודה, ואם הוא שלילי אין פתרונות ממשיים. $\\blacksquare$"),

    # FIX 3: prf_exp_multiplication (claim = "חזקה של חזקה (a^x)^y = a^{xy}")
    #        previously cited thm_rational_exponent_addition, but the body uses
    #        thm_log_of_power. Original body preserved; dep corrected.
    P("prf_exp_multiplication", "thm_exp_multiplication",
      ["def_exponential_function", "thm_log_of_power", "thm_log_inverse_of_exp"],
      "$(a^x)^y = e^{y \\ln(a^x)}$ (לפי הגדרת חזקה כללית $z^t = e^{t \\ln z}$, כאן עם $z = a^x$).\n\n"
      "$= e^{y \\cdot x \\ln a}$ (לפי משפט לוגריתם של חזקה: $\\ln(a^x) = x \\ln a$).\n\n"
      "$= e^{xy \\ln a} = a^{xy}$ (לפי הגדרת חזקה שוב). $\\blacksquare$"),

    # FIX 4: prf_perpendicular_diameter_bisects_chord cited SSS, but body uses
    #        Hypotenuse-Leg (יתר-ניצב) congruence.
    P("prf_perpendicular_diameter_bisects_chord", "thm_perpendicular_diameter_bisects_chord",
      ["def_circle", "ax_hl_congruence", "def_right_triangle"],
      "יהי $O$ מרכז המעגל, $AB$ מיתר, ו-$CD$ קוטר המאונך ל-$AB$ בנקודה $M$.\n\n"
      "נסתכל במשולשים $\\triangle OMA$ ו-$\\triangle OMB$. שניהם ישרי-זווית ב-$M$ (כי $CD \\perp AB$).\n\n"
      "$OA = OB$ (שני רדיוסים) — אלה היתרים של המשולשים הללו.\n\n"
      "$OM$ ניצב משותף.\n\n"
      "לפי חפיפת יתר-ניצב, $\\triangle OMA \\cong \\triangle OMB$, ובפרט $MA = MB$. כלומר הקוטר חוצה את המיתר. $\\blacksquare$"),

    # FIX 5: prf_second_derivative_test cited concavity, but body actually applies
    #        "f'>0 → increasing" to f' (i.e. the increasing/decreasing tests
    #        directly on the first derivative).
    P("prf_second_derivative_test", "thm_second_derivative_test",
      ["def_second_derivative", "thm_increasing_test", "thm_decreasing_test",
       "thm_fermat_extremum"],
      "תהי $f$ פונקציה גזירה פעמיים בנקודה פנימית $c$ עם $f'(c) = 0$.\n\n"
      "**מקסימום ($f''(c) < 0$):** המשמעות היא שהנגזרת של $f'$ ב-$c$ שלילית, ולכן $f'$ יורדת בסביבת $c$ (משפט אם נגזרת שלילית אז יורדת, מופעל על הפונקציה $f'$ במקום $f$). ביחד עם $f'(c) = 0$ מקבלים $f' > 0$ משמאל ל-$c$ ו-$f' < 0$ מימין לה — כלומר $f$ עולה ואז יורדת, אז $c$ מקסימום מקומי.\n\n"
      "**מינימום ($f''(c) > 0$):** סימטרית, $f'$ עולה (לפי משפט אם נגזרת חיובית אז עולה, מופעל על $f'$). אז $f' < 0$ משמאל ל-$c$ ו-$f' > 0$ מימין — $f$ יורדת ואז עולה, אז $c$ מינימום מקומי.\n\n"
      "(הקיום של אקסטרמום ב-$c$ עצמו עוקב ממשפט פרמה.) $\\blacksquare$"),

    # FIX 6: prf_triangle_area_cross_product declared thm_dot_product_geometric
    #        but the body never invokes the dot product. Just remove it.
    P("prf_triangle_area_cross_product", "thm_triangle_area_cross_product",
      ["thm_cross_product_magnitude", "thm_triangle_area_sin"],
      "יהי $\\triangle ABC$. נסמן $\\vec u = \\vec{AB}$ ו-$\\vec v = \\vec{AC}$, ויהי $\\theta$ הזווית ב-$A$.\n\n"
      "לפי משפט גודל המכפלה הוקטורית: $\\|\\vec u \\times \\vec v\\| = \\|\\vec u\\| \\cdot \\|\\vec v\\| \\cdot \\sin \\theta = |AB| \\cdot |AC| \\cdot \\sin \\theta$.\n\n"
      "לפי משפט שטח משולש לפי סינוס: $S(\\triangle ABC) = \\tfrac{1}{2} |AB| \\cdot |AC| \\cdot \\sin \\theta = \\tfrac{1}{2} \\|\\vec u \\times \\vec v\\| = \\tfrac{1}{2} \\|\\vec{AB} \\times \\vec{AC}\\|$. $\\blacksquare$"),

    # FIX 7: prf_remainder_theorem implicitly used polynomial division; declare it.
    P("prf_remainder_theorem", "thm_remainder_theorem",
      ["def_polynomial", "thm_polynomial_division_algorithm"],
      "יהי $p(x)$ פולינום ו-$a \\in \\mathbb{R}$. נחלק את $p(x)$ ב-$(x - a)$ לפי אלגוריתם החילוק לפולינומים: קיימים $q(x), r(x)$ יחידים עם $p(x) = q(x)(x - a) + r(x)$ ו-$\\deg r < \\deg(x - a) = 1$.\n\n"
      "$\\deg r < 1$ אומר ש-$r(x)$ הוא קבוע — נסמן $r(x) \\equiv r$.\n\n"
      "נציב $x = a$: $p(a) = q(a) \\cdot (a - a) + r = q(a) \\cdot 0 + r = r$.\n\n"
      "לכן השארית בחלוקת $p(x)$ ב-$(x - a)$ היא $r = p(a)$. $\\blacksquare$"),

    # FIX 8: prf_sphere_surface_area cited sphere volume, but body uses the
    #        surface-of-revolution formula. The right theorem exists — wire it.
    P("prf_sphere_surface_area", "thm_sphere_surface_area",
      ["def_sphere", "thm_surface_of_revolution", "def_definite_integral"],
      "ניצור את הספירה כסיבוב חצי-המעגל $y = \\sqrt{R^2 - x^2}$, $-R \\leq x \\leq R$, סביב ציר $x$.\n\n"
      "לפי נוסחת שטח-פני-סיבוב: $S = 2\\pi \\int_{-R}^{R} y \\sqrt{1 + (y')^2}\\, dx$.\n\n"
      "מחשבים: $y' = -\\tfrac{x}{\\sqrt{R^2 - x^2}}$, ולכן $1 + (y')^2 = \\tfrac{R^2}{R^2 - x^2}$, ו-$\\sqrt{1 + (y')^2} = \\tfrac{R}{\\sqrt{R^2 - x^2}}$.\n\n"
      "$y \\sqrt{1 + (y')^2} = \\sqrt{R^2 - x^2} \\cdot \\tfrac{R}{\\sqrt{R^2 - x^2}} = R$ (קבוע).\n\n"
      "אז $S = 2\\pi \\int_{-R}^{R} R\\, dx = 2\\pi R \\cdot 2R = 4\\pi R^2$. $\\blacksquare$"),

    # FIX 9: prf_wilson_theorem declared thm_fermat_little but doesn't use it.
    #        The body uses no-zero-divisors mod p ((x-1)(x+1)≡0 → x ≡ ±1).
    P("prf_wilson_theorem", "thm_wilson_theorem",
      ["def_prime", "def_congruence_mod", "thm_no_zero_divisors",
       "ax_multiplicative_inverse"],
      "יהי $p$ ראשוני. נסתכל במכפלה $(p-1)! = 1 \\cdot 2 \\cdots (p-1)$ מודולו $p$.\n\n"
      "**זיווג בהפכיים:** כל $a \\in \\{1, \\ldots, p-1\\}$ הוא בעל הפכי כפלי מודולו $p$ (כי $\\gcd(a, p) = 1$). נזווג כל $a$ עם $a^{-1}$ ב-$\\{1, \\ldots, p-1\\}$. כל זוג כזה תורם $a \\cdot a^{-1} = 1$ למכפלה.\n\n"
      "**איברים שזוויגו עם עצמם:** $a^2 \\equiv 1 \\pmod p$, כלומר $(a-1)(a+1) \\equiv 0 \\pmod p$. כיוון ש-$p$ ראשוני אין מחלקי אפס מודולו $p$, ולכן $a \\equiv 1$ או $a \\equiv -1 \\equiv p-1$.\n\n"
      "כלומר רק $1$ ו-$p-1$ הם המכפילים העצמיים. שאר האיברים $\\{2, 3, \\ldots, p-2\\}$ מתחלקים לזוגות $(a, a^{-1})$ עם $a \\neq a^{-1}$, וכל זוג תורם $1$.\n\n"
      "אז $(p-1)! \\equiv 1 \\cdot (p-1) \\cdot \\underbrace{1 \\cdot 1 \\cdots 1}_{\\text{זוגות}} \\equiv (p-1) \\equiv -1 \\pmod p$. $\\blacksquare$"),

    # FIX 10: prf_tangent_secant_angle was CIRCULAR (used the inscribed-angle
    #        theorem in a way that quietly assumed the conclusion). Rewrite using
    #        the diameter trick + Thales + inscribed angle on the auxiliary triangle.
    P("prf_tangent_secant_angle", "thm_tangent_secant_angle",
      ["thm_tangent_perpendicular_to_radius", "thm_thales",
       "thm_inscribed_angle_theorem", "thm_triangle_angle_sum"],
      "ניקח משיק $\\ell$ במעגל בנקודה $T$, וחותך $TA$ (כאשר $A$ נקודה נוספת על המעגל). נסמן $\\alpha$ את הזווית בין $\\ell$ ל-$TA$, ונראה שהיא שווה למחצית הקשת $\\widehat{TA}$ הכלואה ביניהם.\n\n"
      "**שלב 1 — בניית עזר:** נעביר את הקוטר $TC$ דרך $T$. לפי משפט \"משיק מאונך לרדיוס\", $\\ell \\perp TC$, ולכן הזווית בין $\\ell$ ל-$TC$ היא $90°$.\n\n"
      "**שלב 2 — תאלס:** במשולש $TAC$ הצלע $TC$ קוטר, ולפי משפט תאלס $\\angle TAC = 90°$.\n\n"
      "**שלב 3 — סכום זוויות במשולש:** במשולש ישר-זווית $TAC$ עם $\\angle TAC = 90°$ מתקיים $\\angle ATC + \\angle TCA = 90°$.\n\n"
      "**שלב 4 — שיוויון זוויות:** הזווית בין $\\ell$ ל-$TC$ היא $90°$, וזווית $\\angle ATC$ נמצאת בתוכה. הזווית בין $\\ell$ ל-$TA$ היא ההפרש: $\\alpha = 90° - \\angle ATC = \\angle TCA$ (לפי שלב 3).\n\n"
      "**שלב 5 — זווית היקפית:** $\\angle TCA$ זווית היקפית הנשענת על הקשת $\\widehat{TA}$. לפי משפט הזווית ההיקפית, $\\angle TCA = \\tfrac{1}{2} \\widehat{TA}$.\n\n"
      "**שלב 6:** ולכן $\\alpha = \\tfrac{1}{2} \\widehat{TA}$. $\\blacksquare$\n\n"
      "*הערה:* טיעון זה לא מסתמך על משפט הזווית ההיקפית עבור הקשת $\\widehat{TA}$ ישירות, אלא עבור הזווית $\\angle TCA$ שאינה הזווית שבין משיק לחותך — ולכן אינו מעגלי."),

    # BONUS FIX (cycle-break): prf_log_of_power used thm_exp_multiplication
    #        (power-of-power), which creates a cycle with FIX 3 above. Rewrite
    #        using only def_exponential_function + def_logarithm + log_inverse.
    P("prf_log_of_power", "thm_log_of_power",
      ["def_logarithm", "def_exponential_function", "thm_log_inverse_of_exp"],
      "**שלב 1 — שינוי בסיס לטבעי:** לכל $y > 0$ ולכל $b > 0$, $b \\neq 1$:\n\n"
      "מצד אחד $y = e^{\\ln y}$ (הופכי של ln). מצד שני $y = b^{\\log_b y}$ (הופכי של log_b לפי ההגדרה), ולפי הגדרת חזקה כללית $b^{\\log_b y} = e^{\\log_b y \\cdot \\ln b}$.\n\n"
      "מהשוויון $e^{\\ln y} = e^{\\log_b y \\cdot \\ln b}$ ומחד-חד-ערכיות של $\\exp$: $\\ln y = \\log_b y \\cdot \\ln b$, כלומר $\\log_b y = \\tfrac{\\ln y}{\\ln b}$. (זו נוסחת שינוי בסיס.)\n\n"
      "**שלב 2 — לוגריתם של חזקה:** לפי הגדרת חזקה כללית $x^n = e^{n \\ln x}$. אז:\n\n"
      "$\\log_b(x^n) = \\tfrac{\\ln(x^n)}{\\ln b} = \\tfrac{\\ln(e^{n \\ln x})}{\\ln b}$ (שלב 1)\n\n"
      "$= \\tfrac{n \\ln x}{\\ln b}$ (לפי הופכי $\\ln(e^t) = t$)\n\n"
      "$= n \\cdot \\tfrac{\\ln x}{\\ln b} = n \\log_b x$ (שלב 1 הפוך). $\\blacksquare$"),

    # FIX 11: prf_derangement_formula cited 3-set inclusion-exclusion but the
    #        body needs n-set inclusion-exclusion (new theorem above).
    P("prf_derangement_formula", "thm_derangement_formula",
      ["def_derangement", "thm_inclusion_exclusion_general", "thm_maclaurin_exp"],
      "תהי $A_i$ קבוצת התמורות $\\pi$ המקיימות $\\pi(i) = i$ (כלומר $i$ נשאר במקומו). תמורה $\\pi$ היא דה-רנג'מנט אם ורק אם $\\pi \\notin \\bigcup_{i=1}^{n} A_i$, אז $!n = n! - \\left|\\bigcup_{i=1}^{n} A_i\\right|$.\n\n"
      "**הכלה-הפרדה כללי:** $\\left|\\bigcup_{i=1}^{n} A_i\\right| = \\sum_{k=1}^{n} (-1)^{k+1} \\sum_{|I|=k} \\left|\\bigcap_{i \\in I} A_i\\right|$.\n\n"
      "**חישוב כל חיתוך:** $\\left|\\bigcap_{i \\in I} A_i\\right| = (n - k)!$ — מספר התמורות שמותירות את כל ה-$k$ אינדקסים שבקבוצה $I$ במקומם (השאר חופשי). מספר תת-קבוצות בגודל $k$ הוא $\\binom{n}{k}$.\n\n"
      "אז $\\left|\\bigcup A_i\\right| = \\sum_{k=1}^{n} (-1)^{k+1} \\binom{n}{k} (n-k)! = \\sum_{k=1}^{n} (-1)^{k+1} \\tfrac{n!}{k!}$.\n\n"
      "ולכן $!n = n! - \\sum_{k=1}^{n} (-1)^{k+1} \\tfrac{n!}{k!} = n! \\sum_{k=0}^{n} \\tfrac{(-1)^k}{k!}$.\n\n"
      "**גבול:** הסדרה הפנימית היא סדרת מקלורן של $e^{-1}$, ולכן $\\lim_{n \\to \\infty} \\tfrac{!n}{n!} = e^{-1}$, כלומר $!n \\approx \\tfrac{n!}{e}$. $\\blacksquare$"),
]


# ─────────────────────────────────────────────────────────────────
# Apply force-overwrite of REPLACE_PROOFS
# ─────────────────────────────────────────────────────────────────

def apply_replace_proofs(data_dir: Path) -> int:
    """Force-overwrite every proof in REPLACE_PROOFS. Returns count."""
    for proof in REPLACE_PROOFS:
        files.save_proof(proof, data_dir)
    return len(REPLACE_PROOFS)
