---
id: prf_direct_proportion
claim_id: def_direct_proportion
method: informal
status: reviewed
dependencies:
- def_proportion
- def_ratio
- def_linear_function
- thm_fraction_equality
is_canonical: true
date_added: '2026-06-28T20:34:16.490041Z'
schema_version: 1
---

**שקילות שתי הצורות:** טוענים שהצורה $y = k \cdot x$ (עם $k$ קבוע) שקולה לכך ש-$\frac{y}{x}$ קבוע עבור $x \neq 0$.

- מ-$y = k \cdot x$ ו-$x \neq 0$, חלוקה ב-$x$ נותנת $\frac{y}{x} = k$, קבוע.
- בכיוון ההפוך: אם $\frac{y}{x} = k$ עבור כל $x \neq 0$, אז כפל ב-$x$ נותן $y = k \cdot x$. כאשר $x = 0$, מהצורה $y = k \cdot x$ נקבל $y = 0$ — מה שמתאים גם לרציפות המתבקשת של היחס.

**קשר ל-`def_proportion`:** לפי `def_proportion`, פרופורציה היא שוויון של יחסים $\frac{a}{b} = \frac{c}{d}$. אם $(x_1, y_1)$ ו-$(x_2, y_2)$ הם שני זוגות ערכים תואמים של גדלים בפרופורציה ישירה (עם $x_1, x_2 \neq 0$), אז $\frac{y_1}{x_1} = k = \frac{y_2}{x_2}$, ומ-`thm_fraction_equality` (שוויון שברים) נובע $y_1 \cdot x_2 = y_2 \cdot x_1$ — בדיוק כפל הצלבי של פרופורציה. גם היחס $\frac{y}{x}$ הוא יחס במובן `def_ratio`.

**קשר ל-`def_linear_function`:** הצורה $y = k \cdot x$ היא מקרה פרטי של פונקציה לינארית $f(x) = a \cdot x + b$ עם $a = k$ ו-$b = 0$. כלומר, פרופורציה ישירה היא בדיוק פונקציה לינארית שעוברת דרך הראשית. שיפוע הישר הוא קבוע הפרופורציוניות $k$.

**תכונת ההגדלה היחסית:** אם $x$ גדל פי $\lambda$, אז $y_{\text{חדש}} = k \cdot (\lambda \cdot x) = \lambda \cdot (k \cdot x) = \lambda \cdot y_{\text{ישן}}$ (שימוש באסוציאטיביות וקומוטטיביות של כפל). זוהי התכונה האינטואיטיבית: שני גדלים בפרופורציה ישירה — גידול באחד גורר גידול פרופורציוני בשני באותו יחס.

**הדרישה $k \neq 0$:** אם $k = 0$ אז $y \equiv 0$ ללא תלות ב-$x$, וזה לא מקיים את הרעיון של תלות יחסית בין שני גדלים משתנים. $\blacksquare$
