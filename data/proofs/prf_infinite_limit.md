---
id: prf_infinite_limit
claim_id: def_infinite_limit
method: informal
status: reviewed
dependencies:
- def_function_limit_formal
is_canonical: true
date_added: '2026-06-28T21:06:29.489179Z'
schema_version: 1
---

ההגדרה היא וריאנט של הגדרת אפסילון-דלתא לגבול פונקציה (ראו def_function_limit_formal), שבו מחליפים את התנאי $|f(x) - L| < \epsilon$ — המבטא קרבה לערך סופי $L$ — בתנאי $f(x) > M$ (או $f(x) < -M$) המבטא חריגה מעבר לכל גודל מראש. המשמעות: ערכי הפונקציה אינם 'מתקרבים' לערך מסוים אלא הולכים וגדלים ללא חסם (או הולכים וקטנים ללא חסם תחתון) כאשר $x$ קרב ל-$x_0$. ההגדרה אינה מסתמכת על מושג האסימפטוטה האנכית — להפך, def_vertical_asymptote מוגדרת באמצעות מושג זה: $x = a$ היא אסימפטוטה אנכית של $f$ כאשר $\lim_{x \to a} |f(x)| = \infty$, כלומר כשמתקיימת כאן ההגדרה (או הגרסה החד-צדדית שלה) עם הערך המוחלט. לכן הכיוון הלוגי הוא: גבול אינסופי $\Rightarrow$ אסימפטוטה אנכית, ולא להפך.
