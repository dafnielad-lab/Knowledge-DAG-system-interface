---
id: prf_line_equation_two_point
claim_id: def_line_equation_two_point
method: informal
status: reviewed
dependencies:
- def_slope_between_points
- def_line_equation_point_slope
is_canonical: true
date_added: '2026-06-28T15:49:27.929701Z'
schema_version: 1
---

נראה שצורה זו שקולה לצורת נקודה-שיפוע (def_line_equation_point_slope) כאשר השיפוע מחושב לפי שתי הנקודות.

**שלב 1 — חישוב השיפוע:** כאשר $x_1 \neq x_2$, השיפוע של הישר העובר דרך $(x_1, y_1)$ ו-$(x_2, y_2)$ הוא לפי def_slope_between_points: $m = \frac{y_2 - y_1}{x_2 - x_1}$.

**שלב 2 — הצבה בצורת נקודה-שיפוע:** לפי def_line_equation_point_slope עם הנקודה $(x_1, y_1)$ והשיפוע $m$: $y - y_1 = m(x - x_1) = \frac{y_2 - y_1}{x_2 - x_1} (x - x_1)$. אם נוסף לכך $y_1 \neq y_2$ (כלומר הישר אינו אופקי), נחלק את שני האגפים ב-$(y_2 - y_1)$ ונקבל $\frac{y - y_1}{y_2 - y_1} = \frac{x - x_1}{x_2 - x_1}$ — בדיוק הצורה המבוקשת.

**שלב 3 — מקרי הקצה:** אם $x_1 = x_2$, אז כל הנקודות על הישר חולקות את אותו $x$, ולכן הישר הוא $x = x_1$ (ישר אנכי, אין לו שיפוע סופי). אם $y_1 = y_2$, אז $m = 0$ ולפי הצורה $y - y_1 = 0 \cdot (x - x_1)$ מקבלים $y = y_1$ (ישר אופקי).

**שלב 4 — הכיוון ההפוך:** כל נקודה המקיימת את המשוואה מסיפא נכפלת ב-$(y_2 - y_1)(x_2 - x_1)$ אל $(y - y_1)(x_2 - x_1) = (x - x_1)(y_2 - y_1)$, שניתן לפתוח לצורת נקודה-שיפוע — לכן הנקודה על הישר. $\blacksquare$
