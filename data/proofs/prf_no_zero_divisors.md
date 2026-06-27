---
id: prf_no_zero_divisors
claim_id: thm_no_zero_divisors
method: informal
status: reviewed
dependencies:
- ax_multiplicative_identity
- ax_multiplicative_inverse
- ax_multiplication_associativity
- thm_multiplication_by_zero
is_canonical: true
date_added: '2026-06-27T15:32:36.129981Z'
schema_version: 1
---

נניח $a \cdot b = 0$ ו-$a \neq 0$. נראה ש-$b = 0$.

מאיבר הפכי לכפל קיים $a^{-1}$, ולכן:

$b = 1 \cdot b = (a^{-1} \cdot a) \cdot b = a^{-1} \cdot (a \cdot b) = a^{-1} \cdot 0 = 0$.

(אסוציאטיביות הכפל ומשפט אפס בכפל בשורה האחרונה.) $\blacksquare$
