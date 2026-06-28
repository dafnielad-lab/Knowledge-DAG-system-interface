---
id: prf_line_equation_point_slope
claim_id: def_line_equation_point_slope
method: informal
status: reviewed
dependencies:
- def_slope_between_points
- thm_slope_intercept_form
is_canonical: true
date_added: '2026-06-28T15:49:27.926704Z'
schema_version: 1
---

זוהי הגדרה (תבנית קנונית) של משוואת ישר, אך נראה שהיא שקולה לצורות מוכרות כדי לוודא שאינה ריקה מתוכן.

**שקילות לצורת השיפוע:** נניח שהישר עובר דרך $(x_0, y_0)$ ושיפועו $m$. לפי הגדרת השיפוע בין שתי נקודות (def_slope_between_points), עבור נקודה כללית $(x, y)$ על הישר עם $x \neq x_0$ מתקיים $m = \frac{y - y_0}{x - x_0}$. בכפל שני האגפים ב-$(x - x_0)$ מקבלים $y - y_0 = m(x - x_0)$. גם הנקודה $(x_0, y_0)$ עצמה מקיימת את המשוואה (שני האגפים אפס), כך שכל נקודה על הישר פותרת את המשוואה.

**הכיוון ההפוך:** אם $(x, y)$ מקיים $y - y_0 = m(x - x_0)$, אזי כאשר $x \neq x_0$ מתקיים $\frac{y - y_0}{x - x_0} = m$, כלומר הנקודה נמצאת על הישר עם השיפוע הנתון העובר דרך $(x_0, y_0)$. אם $x = x_0$ אז $y = y_0$ — גם זו נקודה על הישר.

**שקילות לצורת שיפוע-חותך:** מפתיחת הסוגריים: $y = m x - m x_0 + y_0 = m x + b$ עם $b = y_0 - m x_0$ — בדיוק הצורה $y = mx + b$ של thm_slope_intercept_form. לכן כל ישר שאינו אנכי ניתן לכתיבה בצורת נקודה-שיפוע, ולהיפך. $\blacksquare$
