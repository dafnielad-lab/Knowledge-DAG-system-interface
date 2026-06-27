---
id: prf_multiplication_by_zero
claim_id: thm_multiplication_by_zero
method: informal
status: reviewed
dependencies:
- ax_additive_identity
- ax_distributive_law
- thm_addition_cancellation
is_canonical: true
date_added: '2026-06-27T14:26:34.298163Z'
schema_version: 1
---

מאיבר ניטרלי לחיבור, $0 + 0 = 0$. נכפול את שני האגפים ב-$a$:

$a \cdot (0 + 0) = a \cdot 0$

לפי חוק הפילוג:

$a \cdot 0 + a \cdot 0 = a \cdot 0$

נכתוב את אגף ימין כ-$a \cdot 0 + 0$ (מאיבר ניטרלי) ונקבל:

$a \cdot 0 + a \cdot 0 = a \cdot 0 + 0$

משפט הצמצום מאפשר לבטל את $a \cdot 0$ משני האגפים:

$a \cdot 0 = 0$

כלומר $0 \cdot a = 0$ (משתמשים בקומוטטיביות הכפל בהמשך). $\blacksquare$
