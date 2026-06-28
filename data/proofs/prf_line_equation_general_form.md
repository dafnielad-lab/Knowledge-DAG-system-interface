---
id: prf_line_equation_general_form
claim_id: def_line_equation_general_form
method: informal
status: reviewed
dependencies:
- thm_general_form_of_line
- thm_slope_intercept_form
is_canonical: true
date_added: '2026-06-28T15:49:27.932696Z'
schema_version: 1
---

נראה שכל משוואה מהצורה הכללית מתארת ישר, וכל ישר ניתן לכתיבה בצורה הזו — בדיוק התוכן של thm_general_form_of_line.

**מהצורה הכללית לישר:** נניח $Ax + By + C = 0$ עם $A, B$ לא שניהם אפס. מבחינים בשני מקרים:

*מקרה 1:* $B \neq 0$. ניתן לבודד $y$: $y = -\frac{A}{B} x - \frac{C}{B}$, וזו צורת שיפוע-חותך (thm_slope_intercept_form) עם שיפוע $m = -A/B$ וחותך $b = -C/B$. לכן המשוואה מתארת ישר.

*מקרה 2:* $B = 0$. אז בהכרח $A \neq 0$ (כי לא שניהם אפס), והמשוואה הופכת ל-$Ax + C = 0$, כלומר $x = -C/A$ — ישר אנכי קבוע.

**מישר לצורה כללית:** אם הישר אינו אנכי, נכתב $y = mx + b$ ונסדר ל-$mx - y + b = 0$ — צורה כללית עם $A = m, B = -1, C = b$. אם הישר אנכי $x = k$, נכתב $1 \cdot x + 0 \cdot y - k = 0$ — צורה כללית עם $A = 1, B = 0, C = -k$.

**וקטור הנורמל:** אם $(x_1, y_1)$ ו-$(x_2, y_2)$ שתי נקודות על הישר, אז שתיהן פותרות את המשוואה, ובחיסור: $A(x_2 - x_1) + B(y_2 - y_1) = 0$. כלומר וקטור הכיוון $(x_2 - x_1, y_2 - y_1)$ מאונך ל-$(A, B)$ במכפלה הסקלרית — לכן $\vec{n} = (A, B)$ נורמל לישר. $\blacksquare$
