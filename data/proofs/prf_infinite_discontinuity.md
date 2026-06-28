---
id: prf_infinite_discontinuity
claim_id: def_infinite_discontinuity
method: informal
status: reviewed
dependencies:
- def_infinite_limit
- def_continuity_at_point
- def_one_sided_limit_right
- def_one_sided_limit_left
is_canonical: true
date_added: '2026-06-28T21:06:29.491677Z'
schema_version: 1
---

ההגדרה מבחינה אי-רציפות מסוג קוטב מאי-רציפויות אחרות (קפיצה, סליקה) על ידי דרישה ספציפית: לפחות אחד הגבולות החד-צדדיים (def_one_sided_limit_right או def_one_sided_limit_left) קיים במובן המורחב כאחד הערכים $+\infty$ או $-\infty$ — כלומר מתקיימת הגדרת הגבול האינסופי החד-צדדי (וריאנט של def_infinite_limit). מאחר וערך הגבול אינו מספר ממשי, אזי בפרט אינו שווה ל-$f(x_0)$, ולכן תנאי הרציפות $\lim_{x \to x_0} f(x) = f(x_0)$ (ראו def_continuity_at_point) אינו מתקיים, ו-$f$ אינה רציפה ב-$x_0$. ההגבלה לערכים $+\infty$ או $-\infty$ במפורש מוציאה מקרים מתנדנדים שבהם הגבול החד-צדדי אינו קיים כלל (לא במובן הסופי ולא במובן האינסופי), כגון $\sin(1/x)$ ליד $0$ — אלו מסווגים כאי-רציפות מסוג אחר (אי-רציפות מהותית מתנדנדת).
