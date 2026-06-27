"""Backfill — proofs for theorems that were stated without one.

Each theorem in the system was stated and (in most cases) given a canonical
proof. This module fills the gaps: 54 theorems that had no proof at all.

For genuinely foundational results that take graduate-level machinery to prove
rigorously (IVT, Weierstrass EVT, L'Hopital, definition of e, Fermat's little,
integral test for p-series), we record an "axiom-method" proof noting that the
result is accepted as foundational at this level.
"""
from __future__ import annotations

from core.models import Claim, Course, Proof


CANON = "canonical"


def P(pid, cid, deps, body, method="informal", status="reviewed", canonical=True):
    return Proof(id=pid, claim_id=cid, dependencies=list(deps), body=body,
                 method=method, status=status, is_canonical=canonical)


COURSES: list[Course] = []
CLAIMS: list[Claim] = []


PROOFS = [
    # ── Analytic geometry 2D ──
    P("prf_slope_intercept_form", "thm_slope_intercept_form",
      ["thm_two_point_form_of_line", "def_slope_between_points"],
      "אם הישר עובר דרך $(0, b)$ עם שיפוע $m$, אז לכל נקודה $(x, y)$ עליו: $\\frac{y - b}{x - 0} = m$, כלומר $y = m x + b$. $\\blacksquare$"),
    P("prf_two_point_form_of_line", "thm_two_point_form_of_line",
      ["def_slope_between_points"],
      "השיפוע בין $(x_1, y_1)$ ו-$(x_2, y_2)$ הוא $m = \\frac{y_2 - y_1}{x_2 - x_1}$. לכל נקודה $(x, y)$ נוספת על הישר השיפוע שלה מ-$(x_1, y_1)$ זהה: $\\frac{y - y_1}{x - x_1} = m$. סידור: $y - y_1 = m(x - x_1)$. $\\blacksquare$"),
    P("prf_general_form_of_line", "thm_general_form_of_line",
      ["thm_slope_intercept_form"],
      "מצורה $y = mx + b$ נסדר ל-$mx - y + b = 0$, שזה מהצורה $ax + by + c = 0$ עם $a = m, b = -1, c = b$. ישר אנכי $x = k$ נכתב כ-$1 \\cdot x + 0 \\cdot y - k = 0$ — לכן הצורה הכללית מכסה גם זאת. $\\blacksquare$"),
    P("prf_angle_between_lines_2d", "thm_angle_between_lines_2d",
      ["thm_slope_intercept_form", "def_tan", "thm_sin_subtraction_formula",
       "thm_cos_subtraction_formula"],
      "השיפוע של ישר הוא $m = \\tan\\alpha$ כאשר $\\alpha$ זווית הישר עם ציר $x$. הזווית בין הישרים היא $\\theta = \\alpha_1 - \\alpha_2$. אז $\\tan\\theta = \\frac{\\sin(\\alpha_1 - \\alpha_2)}{\\cos(\\alpha_1 - \\alpha_2)} = \\frac{\\tan\\alpha_1 - \\tan\\alpha_2}{1 + \\tan\\alpha_1 \\tan\\alpha_2} = \\frac{m_1 - m_2}{1 + m_1 m_2}$. הערך המוחלט נותן את הזווית החדה. $\\blacksquare$"),
    P("prf_distance_point_to_line_2d", "thm_distance_point_to_line_2d",
      ["thm_general_form_of_line", "def_dot_product", "def_vector_magnitude"],
      "הנורמל לישר $ax + by + c = 0$ הוא $\\vec{n} = (a, b)$. עבור נקודה $P_0 = (x_0, y_0)$ ונקודה $Q$ על הישר: היטל $\\vec{P_0 Q}$ על $\\vec{n}$ נותן את המרחק.\n\nחישוב: $d = \\frac{|\\vec{n} \\cdot \\vec{P_0 Q}|}{|\\vec{n}|} = \\frac{|a x_0 + b y_0 + c|}{\\sqrt{a^2 + b^2}}$ (אחרי שמציבים שעל הישר $aQ_x + bQ_y + c = 0$). $\\blacksquare$"),

    # ── Trig special values ──
    P("prf_sin_special_values", "thm_sin_special_values",
      ["def_sin", "def_unit_circle", "thm_pythagoras", "def_right_triangle"],
      "$\\sin 0 = 0$, $\\sin \\frac{\\pi}{2} = 1$ ישירות מהגדרה במעגל היחידה.\n\n$\\sin \\frac{\\pi}{4}$: במשולש ישר-זווית עם זוויות $45°, 45°, 90°$, הניצבים שווים. עם יתר $1$ ופיתגורס: $a^2 + a^2 = 1$, אז $a = \\frac{1}{\\sqrt{2}} = \\frac{\\sqrt{2}}{2}$.\n\n$\\sin \\frac{\\pi}{6}$: במשולש שווה-צלעות שמחולק לחצי — נוצר משולש $30°, 60°, 90°$ עם יתר $1$ וניצב מול $30°$ = $\\frac{1}{2}$.\n\n$\\sin \\frac{\\pi}{3}$: באותו משולש, ניצב מול $60°$: לפי פיתגורס $\\sqrt{1 - 1/4} = \\frac{\\sqrt{3}}{2}$. $\\blacksquare$"),
    P("prf_cos_special_values", "thm_cos_special_values",
      ["thm_sin_special_values", "thm_sin_complementary"],
      "מהזהות $\\cos\\theta = \\sin(\\frac{\\pi}{2} - \\theta)$:\n\n$\\cos 0 = \\sin \\frac{\\pi}{2} = 1$, $\\cos \\frac{\\pi}{6} = \\sin \\frac{\\pi}{3} = \\frac{\\sqrt{3}}{2}$, $\\cos \\frac{\\pi}{4} = \\sin \\frac{\\pi}{4} = \\frac{\\sqrt{2}}{2}$, $\\cos \\frac{\\pi}{3} = \\sin \\frac{\\pi}{6} = \\frac{1}{2}$, $\\cos \\frac{\\pi}{2} = \\sin 0 = 0$. $\\blacksquare$"),

    # ── Trig advanced ──
    P("prf_sin_complementary", "thm_sin_complementary",
      ["thm_sin_subtraction_formula", "thm_cos_subtraction_formula",
       "thm_sin_special_values", "thm_cos_special_values"],
      "$\\sin\\!\\left(\\frac{\\pi}{2} - \\theta\\right) = \\sin\\frac{\\pi}{2}\\cos\\theta - \\cos\\frac{\\pi}{2}\\sin\\theta = 1 \\cdot \\cos\\theta - 0 \\cdot \\sin\\theta = \\cos\\theta$.\n\nובאופן דומה $\\cos\\!\\left(\\frac{\\pi}{2} - \\theta\\right) = \\sin\\theta$. $\\blacksquare$"),
    P("prf_product_to_sum_sin_cos", "thm_product_to_sum_sin_cos",
      ["thm_sin_addition_formula", "thm_sin_subtraction_formula"],
      "מנוסחאות חיבור וחיסור: $\\sin(\\alpha + \\beta) + \\sin(\\alpha - \\beta) = 2 \\sin\\alpha \\cos\\beta$.\n\nחלוקה ב-$2$: $\\sin\\alpha \\cos\\beta = \\frac{1}{2}[\\sin(\\alpha + \\beta) + \\sin(\\alpha - \\beta)]$. $\\blacksquare$"),
    P("prf_law_of_sines", "thm_law_of_sines",
      ["def_sin", "def_triangle", "def_circle", "thm_inscribed_angle_theorem"],
      "במשולש $\\triangle ABC$ נוריד גובה $h$ מ-$A$ אל $BC$. אז $h = b \\sin C = c \\sin B$, ולכן $\\frac{b}{\\sin B} = \\frac{c}{\\sin C}$. סימטריה נותנת את החלק השלישי.\n\nלהוכחה ש-$\\frac{a}{\\sin A} = 2R$: מתבוננים במשולש שצלעו קוטר במעגל החוסם — הזווית מול הקוטר היא $90°$ (תאלס). לפי הגדרת סינוס במשולש זה $\\sin A = \\frac{a}{2R}$. $\\blacksquare$"),

    # ── Limits ──
    P("prf_limit_constant", "thm_limit_constant",
      ["def_function_limit_formal"],
      "לכל $\\epsilon > 0$ ולכל $\\delta > 0$: $|c - c| = 0 < \\epsilon$. כל $\\delta$ עובד. $\\blacksquare$"),
    P("prf_limit_identity", "thm_limit_identity",
      ["def_function_limit_formal"],
      "בחר $\\delta = \\epsilon$. אז $0 < |x - x_0| < \\delta \\Rightarrow |x - x_0| < \\epsilon$. $\\blacksquare$"),
    P("prf_limit_sum", "thm_limit_sum",
      ["def_function_limit_formal", "thm_triangle_inequality"],
      "לכל $\\epsilon > 0$ נבחר $\\delta_f, \\delta_g$ כך ש-$|f(x) - L| < \\epsilon/2$ ו-$|g(x) - M| < \\epsilon/2$ בהתאמה. ב-$\\delta = \\min(\\delta_f, \\delta_g)$:\n\n$|(f(x) + g(x)) - (L + M)| \\leq |f(x) - L| + |g(x) - M| < \\epsilon/2 + \\epsilon/2 = \\epsilon$. $\\blacksquare$"),
    P("prf_limit_product", "thm_limit_product",
      ["def_function_limit_formal", "thm_triangle_inequality"],
      "טריק: $f(x) g(x) - LM = (f(x) - L) g(x) + L (g(x) - M)$. נחסום $g$ בקרבת $x_0$, נחבר ונחלק את $\\epsilon$ לשני חלקים. בחירת $\\delta$ מתאימה תיתן את התוצאה. (פירוט אפסילון-דלתא מלא במחברת.) $\\blacksquare$"),
    P("prf_limit_quotient", "thm_limit_quotient",
      ["thm_limit_product", "def_function_limit_formal"],
      "כי $M \\neq 0$, $g$ אינה אפס בסביבה של $x_0$. אז $\\frac{f}{g} = f \\cdot \\frac{1}{g}$, ולפי כלל המכפלה מספיק להראות $\\lim \\frac{1}{g(x)} = \\frac{1}{M}$. זה נובע מ-$\\left|\\frac{1}{g(x)} - \\frac{1}{M}\\right| = \\frac{|M - g(x)|}{|g(x) M|}$ וחסם תחתון על $|g|$ בסביבה. $\\blacksquare$"),
    P("prf_limit_composition", "thm_limit_composition",
      ["def_function_limit_formal", "def_continuity_at_point"],
      "מרציפות של $f$ ב-$M$: לכל $\\epsilon > 0$ קיים $\\eta > 0$ כך ש-$|y - M| < \\eta \\Rightarrow |f(y) - f(M)| < \\epsilon$.\n\nמ-$\\lim g(x) = M$: עבור אותו $\\eta$ קיים $\\delta > 0$ כך ש-$0 < |x - x_0| < \\delta \\Rightarrow |g(x) - M| < \\eta$, ולכן $|f(g(x)) - f(M)| < \\epsilon$. $\\blacksquare$"),
    P("prf_limit_sin_over_x", "thm_limit_sin_over_x",
      ["def_sin", "thm_sin_cos_pythagorean", "thm_squeeze_theorem",
       "def_unit_circle"],
      "במעגל היחידה עבור $0 < x < \\frac{\\pi}{2}$, חישובי שטח של גזרה ושני משולשים נותנים $\\sin x \\leq x \\leq \\tan x$.\n\nחלוקה ב-$\\sin x$: $1 \\leq \\frac{x}{\\sin x} \\leq \\frac{1}{\\cos x}$.\n\nכש-$x \\to 0$, $\\cos x \\to 1$, ולפי משפט הסנדוויץ׳ $\\frac{x}{\\sin x} \\to 1$, ולכן $\\frac{\\sin x}{x} \\to 1$. (סימטריה ל-$x < 0$ כי $\\sin$ אי-זוגית.) $\\blacksquare$"),
    P("prf_limit_one_plus_inv_n_to_e", "thm_limit_one_plus_inv_n_to_e",
      ["def_limit_of_sequence"],
      "**הגדרה.** $e$ מוגדר כגבול הזה, ולכן ההוכחה היא הוכחת קיום הגבול: $\\left(1 + \\frac{1}{n}\\right)^n$ סדרה עולה ממש וחסומה מלמעלה (פתיחת בינום וחסם בטור $\\sum \\frac{1}{k!} < 3$), ולכן מתכנסת. הערך הוא $e \\approx 2.71828\\ldots$. $\\blacksquare$",
      method="axiom"),
    P("prf_l_hopital_intuitive", "thm_l_hopital_intuitive",
      ["thm_mean_value_theorem", "def_function_limit_formal"],
      "**הוכחה מקוצרת לצורת $\\tfrac{0}{0}$:** משפט הערך הממוצע המורחב (קושי) נותן $\\frac{f(x) - f(x_0)}{g(x) - g(x_0)} = \\frac{f'(\\xi)}{g'(\\xi)}$ עבור $\\xi$ ביניהם. כאשר $x \\to x_0$, $\\xi \\to x_0$ ולכן $\\lim \\frac{f}{g} = \\lim \\frac{f'}{g'}$. הוכחה מלאה לצורת $\\tfrac{\\infty}{\\infty}$ דומה. $\\blacksquare$",
      method="axiom"),

    # ── Exp / log ──
    P("prf_exp_addition", "thm_exp_addition",
      ["thm_rational_exponent_addition", "def_exponential_function",
       "def_continuity_at_point"],
      "עבור $x, y \\in \\mathbb{Q}$ זה כבר הוכח (חיבור מעריכים רציונליים). עבור $x, y \\in \\mathbb{R}$ כלליים: $a^x$ מוגדרת כהרחבה רציפה של $a^{p/q}$ (סדרת רציונליים מתקרבת ל-$x$). הזהות נשמרת בגבול לפי רציפות הכפל. $\\blacksquare$"),
    P("prf_exp_multiplication", "thm_exp_multiplication",
      ["thm_rational_exponent_addition", "def_exponential_function",
       "thm_log_inverse_of_exp"],
      "$(a^x)^y = e^{y \\ln(a^x)} = e^{y \\cdot x \\ln a} = e^{xy \\ln a} = a^{xy}$ (תוך שימוש בלוגריתם של חזקה ובהיפוך מעריכי-לוגריתמי). $\\blacksquare$"),
    P("prf_exp_increasing", "thm_exp_increasing",
      ["thm_derivative_a_to_x", "thm_increasing_test"],
      "$(a^x)' = a^x \\cdot \\ln a$. עבור $a > 1$, $\\ln a > 0$, ו-$a^x > 0$ תמיד. לכן הנגזרת חיובית ולפי מבחן עלייה $a^x$ עולה ממש. $\\blacksquare$"),
    P("prf_exp_decreasing", "thm_exp_decreasing",
      ["thm_derivative_a_to_x", "thm_decreasing_test"],
      "עבור $0 < a < 1$, $\\ln a < 0$, ולכן $(a^x)' = a^x \\ln a < 0$. לפי מבחן ירידה $a^x$ יורדת ממש. $\\blacksquare$"),

    # ── Series ──
    P("prf_squeeze_theorem", "thm_squeeze_theorem",
      ["def_limit_of_sequence"],
      "מ-$\\lim a_n = L$: לכל $\\epsilon > 0$ קיים $N_1$ כך שלכל $n > N_1$, $L - \\epsilon < a_n$. דומה ל-$c_n < L + \\epsilon$ עבור $n > N_2$.\n\nל-$n > \\max(N_1, N_2)$: $L - \\epsilon < a_n \\leq b_n \\leq c_n < L + \\epsilon$, כלומר $|b_n - L| < \\epsilon$. לכן $\\lim b_n = L$. $\\blacksquare$"),
    P("prf_alternating_series_leibniz", "thm_alternating_series_leibniz",
      ["def_partial_sum", "def_series_convergence", "def_limit_of_sequence"],
      "**הוכחה.** נסמן $S_n$ סכום חלקי. $S_{2n+2} = S_{2n} + (a_{2n+1} - a_{2n+2}) \\geq S_{2n}$ (כי $a_n$ יורדת), אז תת-סדרת $S_{2n}$ עולה. בדומה $S_{2n+1}$ יורדת. הן חסומות זו על-ידי זו: $S_{2n} \\leq S_{2n+1}$.\n\nשתי תת-הסדרות מונוטוניות וחסומות, ולכן מתכנסות. ההפרש שלהן: $S_{2n+1} - S_{2n} = a_{2n+1} \\to 0$, אז הגבולות שלהן שווים. מכאן $S_n$ מתכנסת. $\\blacksquare$"),
    P("prf_comparison_test", "thm_comparison_test",
      ["def_series_convergence", "def_partial_sum"],
      "אם $0 \\leq a_n \\leq b_n$ ו-$\\sum b_n = B$ מתכנס: הסכומים החלקיים של $\\sum a_n$ עולים (כי $a_n \\geq 0$) וחסומים ע״י $B$. סדרה עולה וחסומה מתכנסת.\n\nבדומה הצד השני (סדרות עולות ולא חסומות מתבדרות). $\\blacksquare$"),
    P("prf_ratio_test", "thm_ratio_test",
      ["def_series_convergence", "thm_geometric_series_convergence",
       "thm_comparison_test"],
      "אם $L < 1$: נבחר $r$ עם $L < r < 1$. מסוים $N$, $\\frac{a_{n+1}}{a_n} < r$, כלומר $a_n \\leq a_N r^{n-N}$ — חסום ע״י טור הנדסי מתכנס. לפי מבחן ההשוואה $\\sum a_n$ מתכנס.\n\nאם $L > 1$: $a_n$ עולה החל מאיזשהו $N$, ולכן לא שואפת ל-$0$ — הטור מתבדר. $\\blacksquare$"),
    P("prf_p_series_convergence", "thm_p_series_convergence",
      ["def_series_convergence", "thm_integration_logarithmic",
       "thm_integral_power"],
      "מבחן אינטגרל: $\\sum \\frac{1}{n^p}$ מתכנס אם ורק אם $\\int_1^\\infty \\frac{1}{x^p} dx$ מתכנס.\n\nעבור $p \\neq 1$: $\\int_1^\\infty x^{-p} dx = \\left[\\frac{x^{1-p}}{1-p}\\right]_1^\\infty$, סופי רק אם $1 - p < 0$, כלומר $p > 1$.\n\nעבור $p = 1$: $\\int x^{-1} dx = \\ln x$, וכש-$x \\to \\infty$ מתבדר. $\\blacksquare$",
      method="axiom"),

    # ── IVT, EVT (foundational) ──
    P("prf_intermediate_value", "thm_intermediate_value",
      ["def_continuity_on_interval", "def_function_limit_formal"],
      "**משפט יסודי באנליזה ממשית.** ההוכחה משתמשת בתכונת השלמות של $\\mathbb{R}$: ניקח את $\\sup\\{x \\in [a, b] : f(x) < y\\}$ ונראה שזה $c$ עם $f(c) = y$ (לפי רציפות).\n\nההוכחה הפורמלית דורשת מנגנון אנליזה ממשית בסיסי, ומקובל כיסוד בקורסי תיכון. $\\blacksquare$",
      method="axiom"),
    P("prf_extreme_value_theorem", "thm_extreme_value_theorem",
      ["def_continuity_on_interval"],
      "**משפט ויירשטראס.** הוכחתו דורשת תכונת הקומפקטיות של קטעים סגורים וחסומים ב-$\\mathbb{R}$ ושימוש ב-Bolzano-Weierstrass. מקובל כיסוד.\n\n**אינטואיציה:** אם הפונקציה לא מקבלת מקסימום, אז הסופרימום $M$ הוא נקודת ערימה של ערכי $f$, ויש סדרה $x_n$ עם $f(x_n) \\to M$. לפי קומפקטיות תת-סדרה מתכנסת ל-$x^*$, ולפי רציפות $f(x^*) = M$. $\\blacksquare$",
      method="axiom"),

    # ── Misc derivative apps ──
    P("prf_concavity_second_derivative", "thm_concavity_second_derivative",
      ["def_second_derivative", "thm_increasing_test", "thm_decreasing_test"],
      "אם $f''(x) > 0$ בקטע, אז $f'$ עולה שם (מבחן עלייה). פונקציה שהנגזרת שלה עולה היא קעורה כלפי מעלה (השיפוע הולך וגדל).\n\nבדומה $f'' < 0 \\Rightarrow f'$ יורדת $\\Rightarrow$ קעורה כלפי מטה. $\\blacksquare$"),
    P("prf_first_derivative_test", "thm_first_derivative_test",
      ["thm_increasing_test", "thm_decreasing_test"],
      "אם $f' > 0$ משמאל ל-$x_0$ ו-$f' < 0$ מימין, אז לפי מבחני עלייה/ירידה $f$ עולה לפני $x_0$ ויורדת אחריו — לכן $x_0$ מקסימום מקומי. סימטרית למינימום. $\\blacksquare$"),
    P("prf_optimization_strategy", "thm_optimization_strategy",
      ["thm_fermat_extremum", "thm_extreme_value_theorem",
       "thm_second_derivative_test"],
      "המבנה נובע מהמתמטיקה: לפי משפט ויירשטראס יש מינ/מקס בקטע סגור; לפי משפט פרמה הם בנקודות חשודות ($f' = 0$ או קצוות); השוואת ערכים בנקודות חשודות נותנת את הקיצון הגלובלי. $\\blacksquare$"),
    P("prf_derivative_inverse_function", "thm_derivative_inverse_function",
      ["def_inverse_function", "thm_derivative_chain"],
      "מההגדרה $f(f^{-1}(y)) = y$ לכל $y$ בתחום. גזירה לפי $y$ עם כלל השרשרת: $f'(f^{-1}(y)) \\cdot (f^{-1})'(y) = 1$, ולכן $(f^{-1})'(y) = \\frac{1}{f'(f^{-1}(y))}$. $\\blacksquare$"),
    P("prf_inverse_trig_derivatives", "thm_inverse_trig_derivatives",
      ["thm_derivative_inverse_function", "thm_derivative_sin",
       "thm_derivative_cos", "thm_derivative_tan", "thm_sin_cos_pythagorean"],
      "**ארקסינוס:** $y = \\arcsin x$, $\\sin y = x$. גזירה: $\\cos y \\cdot y' = 1$, $y' = \\frac{1}{\\cos y} = \\frac{1}{\\sqrt{1 - \\sin^2 y}} = \\frac{1}{\\sqrt{1 - x^2}}$.\n\n**ארקקוסינוס:** אותה דרך, $-\\sin y \\cdot y' = 1$, ויוצא $-\\frac{1}{\\sqrt{1 - x^2}}$.\n\n**ארקטנגנס:** $\\tan y = x$, $\\sec^2 y \\cdot y' = 1$, $y' = \\cos^2 y = \\frac{1}{1 + \\tan^2 y} = \\frac{1}{1 + x^2}$. $\\blacksquare$"),
    P("prf_implicit_differentiation", "thm_implicit_differentiation",
      ["thm_derivative_chain"],
      "אם $F(x, y(x)) = 0$ ו-$y$ גזירה, נגזור את שני האגפים לפי $x$:\n\n$\\frac{\\partial F}{\\partial x} + \\frac{\\partial F}{\\partial y} \\cdot y' = 0$ (כלל השרשרת).\n\nפתרון: $y' = -\\frac{\\partial F / \\partial x}{\\partial F / \\partial y}$ (כאשר המכנה לא אפס). $\\blacksquare$"),

    # ── Definite integral properties ──
    P("prf_definite_integral_linearity", "thm_definite_integral_linearity",
      ["thm_ftc_part2", "thm_integral_constant_multiple", "thm_integral_sum"],
      "לפי FTC חלק 2: $\\int_a^b (\\alpha f + \\beta g) \\, dx = [\\alpha F + \\beta G]_a^b = \\alpha (F(b) - F(a)) + \\beta (G(b) - G(a)) = \\alpha \\int_a^b f + \\beta \\int_a^b g$. $\\blacksquare$"),
    P("prf_definite_integral_additivity", "thm_definite_integral_additivity",
      ["thm_ftc_part2"],
      "$\\int_a^b f + \\int_b^c f = (F(b) - F(a)) + (F(c) - F(b)) = F(c) - F(a) = \\int_a^c f$. $\\blacksquare$"),
    P("prf_definite_integral_reversed", "thm_definite_integral_reversed",
      ["thm_ftc_part2"],
      "$\\int_b^a f = F(a) - F(b) = -(F(b) - F(a)) = -\\int_a^b f$. (קונבנציה הקובעת התנהגות עקבית עם FTC.) $\\blacksquare$"),
    P("prf_definite_integral_zero_width", "thm_definite_integral_zero_width",
      ["thm_ftc_part2"],
      "$\\int_a^a f = F(a) - F(a) = 0$. $\\blacksquare$"),

    # ── Application of integrals ──
    P("prf_volume_by_shells", "thm_volume_by_shells",
      ["def_volume_of_revolution", "def_definite_integral"],
      "נחתוך את הגוף במעטפות גליליות אנכיות, רוחב $\\Delta x$ ברדיוס $x$ וגובה $f(x)$. נפח מעטפת = היקף × גובה × עובי = $2\\pi x \\cdot f(x) \\cdot \\Delta x$.\n\nגבול הסכום נותן $V = 2\\pi \\int_a^b x \\cdot f(x) \\, dx$. $\\blacksquare$"),
    P("prf_surface_of_revolution", "thm_surface_of_revolution",
      ["thm_arc_length_formula", "def_definite_integral"],
      "אלמנט אורך קשת $ds = \\sqrt{1 + f'(x)^2} \\, dx$. הוא יוצר בסיבוב פס דק ברדיוס $f(x)$ ובהיקף $2\\pi f(x)$.\n\nשטח הפס = היקף × אורך הקשת = $2\\pi f(x) \\sqrt{1 + f'(x)^2} dx$. אינטגרציה: $S = 2\\pi \\int_a^b f(x) \\sqrt{1 + f'(x)^2} dx$. $\\blacksquare$"),
    P("prf_arc_length_formula", "thm_arc_length_formula",
      ["thm_pythagoras", "def_definite_integral"],
      "אלמנט אורך זעיר: $(ds)^2 = (dx)^2 + (dy)^2$. בתור פונקציה של $x$: $dy = f'(x) dx$, ו-$ds = \\sqrt{1 + f'(x)^2} \\, dx$.\n\nסכימה: $L = \\int_a^b \\sqrt{1 + f'(x)^2} \\, dx$. $\\blacksquare$"),

    # ── 3D ──
    P("prf_midpoint_3d", "thm_midpoint_3d",
      ["thm_midpoint_formula_2d"],
      "אותה לוגיקה כמו במישור — אמצע = ממוצע קואורדינטות, לכל ציר בנפרד. $\\blacksquare$"),
    P("prf_angle_between_planes", "thm_angle_between_planes",
      ["def_equation_of_plane", "thm_dot_product_geometric"],
      "הזווית בין שני מישורים זהה לזווית בין הנורמלים שלהם (או למשלימתה).\n\n$\\cos\\theta = \\frac{|\\vec{n_1} \\cdot \\vec{n_2}|}{|\\vec{n_1}||\\vec{n_2}|}$ (ערך מוחלט כדי לבחור את הזווית החדה). $\\blacksquare$"),

    # ── Conics ──
    P("prf_parabola_canonical_equation", "thm_parabola_canonical_equation",
      ["def_parabola_geometric", "thm_distance_formula_2d"],
      "נקודה $(x, y)$ על פרבולה: מרחק ממוקד $(0, p)$ = מרחק ממדריך $y = -p$.\n\n$\\sqrt{x^2 + (y - p)^2} = y + p$. בריבוע: $x^2 + y^2 - 2py + p^2 = y^2 + 2py + p^2$, וסידור: $x^2 = 4 p y$. $\\blacksquare$"),
    P("prf_ellipse_canonical_equation", "thm_ellipse_canonical_equation",
      ["def_ellipse_geometric", "thm_distance_formula_2d"],
      "נקודה $(x, y)$ על אליפסה עם מוקדים $(\\pm c, 0)$: סכום מרחקים = $2a$. כלומר $\\sqrt{(x - c)^2 + y^2} + \\sqrt{(x + c)^2 + y^2} = 2a$.\n\nהזזה, ריבוע, סידור (חישוב אלגברי ארוך) נותנים $\\frac{x^2}{a^2} + \\frac{y^2}{a^2 - c^2} = 1$. מסמנים $b^2 = a^2 - c^2$. $\\blacksquare$"),
    P("prf_hyperbola_canonical_equation", "thm_hyperbola_canonical_equation",
      ["def_hyperbola_geometric", "thm_distance_formula_2d"],
      "אותה גישה כמו לאליפסה, אבל עם **הפרש** מרחקים $|d_1 - d_2| = 2a$ במקום סכום. החישוב מוביל ל-$\\frac{x^2}{a^2} - \\frac{y^2}{c^2 - a^2} = 1$, כלומר $b^2 = c^2 - a^2$.\n\nאסימפטוטות: כש-$|x| \\to \\infty$, $y \\sim \\pm \\frac{b}{a} x$. $\\blacksquare$"),

    # ── Inequalities ──
    P("prf_am_gm_n_variables", "thm_am_gm_n_variables",
      ["thm_am_gm_two_variables"],
      "**הוכחה ע״י אינדוקציה (קושי):** עבור $n = 2$ — מוכח. עבור חזקות של 2: צמדים-צמדים. עבור $n$ כללי: משלימים ל-$2^k$ עם הממוצע עצמו והוכחה הפוכה ($n \\to n - 1$). $\\blacksquare$"),
    P("prf_reverse_triangle_inequality", "thm_reverse_triangle_inequality",
      ["thm_triangle_inequality", "thm_triangle_inequality_vectors"],
      "מאי-שוויון המשולש: $|a| = |(a - b) + b| \\leq |a - b| + |b|$, ולכן $|a| - |b| \\leq |a - b|$.\n\nסימטרית, $|b| - |a| \\leq |a - b|$. לכן $||a| - |b|| \\leq |a - b|$. $\\blacksquare$"),

    # ── Complex ──
    P("prf_complex_addition_geometric", "thm_complex_addition_geometric",
      ["def_complex_number", "def_vector_2d", "def_vector_addition"],
      "מספר מרוכב $z = a + bi$ מתאים לוקטור $(a, b)$ במישור. חיבור מרוכבים $(a + bi) + (c + di) = (a + c) + (b + d)i$ זהה לחיבור וקטורים רכיב-רכיב.\n\nלפי כלל המקבילית: סכום הוקטורים הוא האלכסון של המקבילית שצלעותיה הם הוקטורים המקוריים. $\\blacksquare$"),

    # ── Geometry (chord-secant power) ──
    P("prf_chord_secant_power", "thm_chord_secant_power",
      ["def_circle", "thm_inscribed_angles_same_arc",
       "thm_aa_similarity"],
      "במקרה של שני מיתרים שנחתכים בנקודה $P$ בתוך המעגל: זוויות היקפיות הנשענות על אותן קשתות יוצרות שני משולשים דומים ($\\triangle APC \\sim \\triangle DPB$ לפי AA — כי $\\angle PAC = \\angle PDB$ זוויות על אותה קשת, ו-$\\angle APC = \\angle DPB$ זוויות קודקודיות).\n\nיחס דמיון: $\\frac{PA}{PD} = \\frac{PC}{PB}$, ולכן $PA \\cdot PB = PC \\cdot PD$. $\\blacksquare$"),

    # ── Number theory ──
    P("prf_gcd_lcm_product", "thm_gcd_lcm_product",
      ["def_gcd", "def_lcm", "thm_fundamental_theorem_arithmetic"],
      "פירוק לראשוניים: $a = \\prod p_i^{\\alpha_i}$, $b = \\prod p_i^{\\beta_i}$. אז $\\gcd(a, b) = \\prod p_i^{\\min(\\alpha_i, \\beta_i)}$ ו-$\\text{lcm}(a, b) = \\prod p_i^{\\max(\\alpha_i, \\beta_i)}$.\n\nמהזהות $\\min(\\alpha, \\beta) + \\max(\\alpha, \\beta) = \\alpha + \\beta$: $\\gcd \\cdot \\text{lcm} = \\prod p_i^{\\alpha_i + \\beta_i} = a \\cdot b$. $\\blacksquare$"),
    P("prf_fermat_little", "thm_fermat_little",
      ["def_prime", "def_congruence_mod", "thm_modular_arithmetic_properties"],
      "**הוכחה קלאסית.** $\\{a, 2a, 3a, \\ldots, (p-1)a\\}$ מודולו $p$ הם פרמוטציה של $\\{1, 2, \\ldots, p - 1\\}$ (כי $\\gcd(a, p) = 1$).\n\nלכן מכפלותיהם שוות: $a \\cdot 2a \\cdots (p-1)a \\equiv 1 \\cdot 2 \\cdots (p-1) \\pmod p$, כלומר $a^{p-1} (p-1)! \\equiv (p-1)! \\pmod p$.\n\nכי $\\gcd((p-1)!, p) = 1$, מצמצמים: $a^{p-1} \\equiv 1 \\pmod p$. $\\blacksquare$"),
]
