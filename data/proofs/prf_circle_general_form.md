---
id: prf_circle_general_form
claim_id: thm_circle_general_form
method: informal
status: reviewed
dependencies:
- thm_equation_of_circle
- thm_completing_the_square
is_canonical: true
date_added: '2026-06-27T20:41:51.335588Z'
schema_version: 1
---

נתונה משוואה כללית $x^2 + y^2 + Dx + Ey + F = 0$. נשלים ריבועים לכל אחד מהמשתנים בנפרד.

לפי משפט השלמת ריבוע: $x^2 + Dx = \left(x + \tfrac{D}{2}\right)^2 - \tfrac{D^2}{4}$ ו-$y^2 + Ey = \left(y + \tfrac{E}{2}\right)^2 - \tfrac{E^2}{4}$.

נציב במשוואה:

$\left(x + \tfrac{D}{2}\right)^2 - \tfrac{D^2}{4} + \left(y + \tfrac{E}{2}\right)^2 - \tfrac{E^2}{4} + F = 0$

$\left(x + \tfrac{D}{2}\right)^2 + \left(y + \tfrac{E}{2}\right)^2 = \tfrac{D^2 + E^2 - 4F}{4}$.

אם הצד הימני חיובי, זו משוואת מעגל עם מרכז $\left(-\tfrac{D}{2}, -\tfrac{E}{2}\right)$ ורדיוס $r = \tfrac{1}{2}\sqrt{D^2 + E^2 - 4F}$. אם הוא אפס המעגל מנוון לנקודה, ואם הוא שלילי אין פתרונות ממשיים. $\blacksquare$
