---
id: prf_negation_of_sum
claim_id: thm_negation_of_sum
method: informal
status: reviewed
dependencies:
- ax_addition_associativity
- ax_addition_commutativity
- ax_additive_identity
- ax_additive_inverse
- thm_additive_inverse_uniqueness
is_canonical: true
date_added: '2026-06-27T15:32:36.129981Z'
schema_version: 1
---

נראה ש-$(-a) + (-b)$ הוא הנגדי של $a + b$, ומיחידות הנגדי ננבע ש-$-(a+b) = (-a) + (-b)$.

$(a + b) + ((-a) + (-b)) = (a + (-a)) + (b + (-b)) = 0 + 0 = 0$

(תוך שימוש באסוציאטיביות וקומוטטיביות לסידור מחדש של הסכום, ובהגדרת הנגדי). $\blacksquare$
