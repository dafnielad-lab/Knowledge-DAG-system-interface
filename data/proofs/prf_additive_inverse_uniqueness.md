---
id: prf_additive_inverse_uniqueness
claim_id: thm_additive_inverse_uniqueness
method: informal
status: reviewed
dependencies:
- ax_addition_associativity
- ax_addition_commutativity
- ax_additive_identity
- ax_additive_inverse
is_canonical: true
date_added: '2026-06-27T15:32:36.129981Z'
schema_version: 1
---

נניח ש-$b$ ו-$c$ שניהם מקיימים $a + b = 0$ ו-$a + c = 0$.

אז $b = b + 0 = b + (a + c) = (b + a) + c = (a + b) + c = 0 + c = c$.

השתמשנו באיבר ניטרלי, אסוציאטיביות, קומוטטיביות, ובהגדרת הנגדי. $\blacksquare$
