---
id: prf_line_equation_2d_parametric
claim_id: def_line_equation_2d_parametric
method: informal
status: reviewed
dependencies:
- def_vector_2d
- def_line_equation_point_slope
- def_line_equation_general_form
is_canonical: true
date_added: '2026-06-28T15:49:27.935695Z'
schema_version: 1
---

נראה שהיצוג הפרמטרי מתאר בדיוק את אותו אוסף נקודות שמהווה ישר במישור.

**שלב 1 — כל $t$ נותן נקודה על אותו ישר:** מתוך def_vector_2d, $(a, b) \in \mathbb{R}^2$, ולכל $t$ ממשי $(x_0 + ta, y_0 + tb)$ נקודה במישור. בחישוב השיפוע בין שתי נקודות שונות שמתקבלות מ-$t_1, t_2$ (עם $t_1 \neq t_2$ ו-$a \neq 0$): $\frac{(y_0 + t_2 b) - (y_0 + t_1 b)}{(x_0 + t_2 a) - (x_0 + t_1 a)} = \frac{(t_2 - t_1) b}{(t_2 - t_1) a} = \frac{b}{a}$. השיפוע קבוע, כלומר כל הנקודות על אותו ישר (def_line_equation_point_slope עם שיפוע $b/a$).

**שלב 2 — חילוץ $t$ והוכחה שכל נקודה על הישר מתקבלת:** אם $a \neq 0$, מהמשוואה הראשונה $t = (x - x_0)/a$. הצבה בשנייה: $y = y_0 + b \cdot \frac{x - x_0}{a}$, כלומר $y - y_0 = \frac{b}{a}(x - x_0)$ — בדיוק צורת נקודה-שיפוע. כל פתרון $(x, y)$ של משוואת הישר נותן ערך יחיד $t = (x - x_0)/a$.

**שלב 3 — מקרה הישר האנכי:** אם $a = 0$ אז $b \neq 0$ (כי הוקטור לא אפס). אז $x = x_0$ קבוע, ו-$y = y_0 + tb$ עובר על כל הממשיים כש-$t$ עובר על כל הממשיים. זה ישר אנכי, שגם הוא ישר חוקי בצורה הכללית $1 \cdot x + 0 \cdot y - x_0 = 0$ (def_line_equation_general_form).

**מסקנה:** הצורה הפרמטרית והצורה הכללית מתארות בדיוק את אותם ישרים. $\blacksquare$
