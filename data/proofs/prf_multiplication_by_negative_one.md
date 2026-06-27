---
id: prf_multiplication_by_negative_one
claim_id: thm_multiplication_by_negative_one
method: informal
status: reviewed
dependencies:
- ax_multiplicative_identity
- ax_distributive_law
- ax_additive_inverse
- thm_multiplication_by_zero
- thm_addition_cancellation
is_canonical: true
date_added: '2026-06-27T14:26:34.298163Z'
schema_version: 1
---

נראה ש-$(-1) \cdot a + a = 0$, וזה יוכיח ש-$(-1) \cdot a$ הוא ההפכי הנגדי של $a$, כלומר $-a$:

$(-1) \cdot a + a = (-1) \cdot a + 1 \cdot a$ (מאיבר ניטרלי לכפל)

$= ((-1) + 1) \cdot a$ (חוק הפילוג)

$= 0 \cdot a$ (מאיבר נגדי)

$= 0$ (משפט אפס בכפל).

מכאן $(-1) \cdot a + a = 0$, ולכן $(-1) \cdot a = -a$ (יחידות הנגדי, או הוספת $-a$ ב-$thm\_cancel\_add$). $\blacksquare$
