---
id: prf_power_multiplication_rule
claim_id: thm_power_multiplication_rule
method: informal
status: reviewed
dependencies:
- def_natural_power
- thm_power_addition_rule
- ax_multiplicative_identity
is_canonical: true
date_added: '2026-06-27T15:32:36.129981Z'
schema_version: 1
---

אינדוקציה על $n$.

**בסיס $n = 0$:** $(a^m)^0 = 1 = a^0 = a^{m \cdot 0}$.

**צעד:** $(a^m)^{n+1} = (a^m)^n \cdot a^m = a^{m \cdot n} \cdot a^m = a^{m \cdot n + m} = a^{m(n+1)}$ (לפי הגדרת חזקה, הנחת האינדוקציה, וחיבור מעריכים). $\blacksquare$
