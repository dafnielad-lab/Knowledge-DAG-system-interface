---
id: prf_point_slope_form
claim_id: thm_point_slope_form
method: informal
status: reviewed
dependencies:
- def_slope_between_points
- def_coordinate_plane
is_canonical: true
date_added: '2026-06-28T15:07:55.455549Z'
schema_version: 1
---

נסמן ב-$\ell$ את הישר העובר דרך $(x_0, y_0)$ בעל שיפוע $m$. צריך להוכיח שלכל $(x, y) \in \mathbb{R}^2$ (כאשר $\mathbb{R}^2$ הוא המישור הקרטזי לפי def_coordinate_plane) מתקיים: $(x, y) \in \ell$ אם ורק אם $y - y_0 = m(x - x_0)$.

**כיוון ראשון — נקודה על הישר מקיימת את המשוואה.** נניח ש-$(x, y)$ נקודה על $\ell$. נפריד למקרים:

*מקרה א: $x = x_0$.* אז בהכרח $y = y_0$ (אחרת היו על $\ell$ שתי נקודות שונות בעלות אותו שיעור $x$, ולפי def_slope_between_points השיפוע ביניהן אינו מוגדר — בסתירה לכך של-$\ell$ שיפוע $m$). מציבים במשוואה: $y - y_0 = 0$ וגם $m(x - x_0) = m \cdot 0 = 0$, ולכן השוויון מתקיים.

*מקרה ב: $x \neq x_0$.* לפי def_slope_between_points השיפוע בין שתי הנקודות $(x_0, y_0)$ ו-$(x, y)$ השוכנות על $\ell$ הוא $\frac{y - y_0}{x - x_0}$. מכיוון של-$\ell$ שיפוע יחיד $m$ (השיפוע בין כל שתי נקודות על אותו ישר זהה), נקבל $\frac{y - y_0}{x - x_0} = m$. כפל שני האגפים ב-$(x - x_0) \neq 0$ נותן $y - y_0 = m(x - x_0)$.

**כיוון שני — נקודה המקיימת את המשוואה נמצאת על הישר.** נניח ש-$(x, y)$ מקיימת $y - y_0 = m(x - x_0)$. אם $x = x_0$ אז $y = y_0$, ו-$(x_0, y_0) \in \ell$ לפי הנתון. אם $x \neq x_0$ אזי $\frac{y - y_0}{x - x_0} = m$, כלומר השיפוע בין $(x_0, y_0)$ ל-$(x, y)$ (לפי def_slope_between_points) שווה לשיפוע $\ell$. שתי נקודות וערך שיפוע נתון קובעים ישר יחיד, ולכן $(x, y)$ שוכנת על $\ell$.

מהשילוב נובע השקילות הדרושה. $\blacksquare$
