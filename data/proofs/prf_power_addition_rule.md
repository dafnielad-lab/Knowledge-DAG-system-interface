---
id: prf_power_addition_rule
claim_id: thm_power_addition_rule
method: informal
status: reviewed
dependencies:
- def_natural_power
- ax_multiplication_associativity
- ax_multiplicative_identity
is_canonical: true
date_added: '2026-06-27T15:32:36.129981Z'
schema_version: 1
---

הוכחה באינדוקציה על $n$.

**בסיס $n = 0$:** $a^m \cdot a^0 = a^m \cdot 1 = a^m = a^{m+0}$.

**צעד:** נניח $a^m \cdot a^n = a^{m+n}$. אז $a^m \cdot a^{n+1} = a^m \cdot (a^n \cdot a) = (a^m \cdot a^n) \cdot a = a^{m+n} \cdot a = a^{(m+n)+1} = a^{m+(n+1)}$ (לפי הגדרת חזקה ואסוציאטיביות). $\blacksquare$
