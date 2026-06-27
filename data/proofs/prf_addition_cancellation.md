---
id: prf_addition_cancellation
claim_id: thm_addition_cancellation
method: informal
status: reviewed
dependencies:
- ax_additive_inverse
- ax_addition_associativity
- ax_additive_identity
is_canonical: true
date_added: '2026-06-27T14:26:34.298163Z'
schema_version: 1
---

נניח $a + b = a + c$. נוסיף $-a$ משמאל לשני האגפים:

$(-a) + (a + b) = (-a) + (a + c)$

לפי אסוציאטיביות החיבור:

$((-a) + a) + b = ((-a) + a) + c$

מהגדרת איבר נגדי, $(-a) + a = 0$ (משתמשים גם בקומוטטיביות), ולכן:

$0 + b = 0 + c$

ומאיבר ניטרלי לחיבור נקבל $b = c$. $\blacksquare$
