---
id: prf_power_of_product
claim_id: thm_power_of_product
method: informal
status: reviewed
dependencies:
- def_natural_power
- ax_multiplication_associativity
- ax_multiplication_commutativity
- ax_multiplicative_identity
is_canonical: true
date_added: '2026-06-27T15:32:36.129981Z'
schema_version: 1
---

אינדוקציה על $n$.

**בסיס $n = 0$:** $(ab)^0 = 1 = 1 \cdot 1 = a^0 \cdot b^0$.

**צעד:** $(ab)^{n+1} = (ab)^n \cdot (ab) = (a^n b^n)(ab) = (a^n \cdot a)(b^n \cdot b) = a^{n+1} b^{n+1}$ (תוך שימוש בקומוטטיביות ואסוציאטיביות לארגון הגורמים). $\blacksquare$
