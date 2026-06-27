---
id: prf_addition_undoes_subtraction
claim_id: thm_addition_undoes_subtraction
method: informal
status: reviewed
dependencies:
- def_subtraction
- ax_addition_associativity
- ax_addition_commutativity
- ax_additive_inverse
- ax_additive_identity
is_canonical: true
date_added: '2026-06-27T15:32:36.129981Z'
schema_version: 1
---

$(a - b) + b = (a + (-b)) + b$ (הגדרת חיסור) $= a + ((-b) + b)$ (אסוציאטיביות) $= a + 0$ (קומוטטיביות + נגדי) $= a$ (איבר ניטרלי). $\blacksquare$
