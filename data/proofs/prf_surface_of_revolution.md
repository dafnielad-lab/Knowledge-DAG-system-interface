---
id: prf_surface_of_revolution
claim_id: thm_surface_of_revolution
method: informal
status: reviewed
dependencies:
- thm_arc_length_formula
- def_definite_integral
is_canonical: true
date_added: '2026-06-27T17:14:35.075131Z'
schema_version: 1
---

אלמנט אורך קשת $ds = \sqrt{1 + f'(x)^2} \, dx$. הוא יוצר בסיבוב פס דק ברדיוס $f(x)$ ובהיקף $2\pi f(x)$.

שטח הפס = היקף × אורך הקשת = $2\pi f(x) \sqrt{1 + f'(x)^2} dx$. אינטגרציה: $S = 2\pi \int_a^b f(x) \sqrt{1 + f'(x)^2} dx$. $\blacksquare$
