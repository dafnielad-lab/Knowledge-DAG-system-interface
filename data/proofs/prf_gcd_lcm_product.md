---
id: prf_gcd_lcm_product
claim_id: thm_gcd_lcm_product
method: informal
status: reviewed
dependencies:
- def_gcd
- def_lcm
- thm_fundamental_theorem_arithmetic
is_canonical: true
date_added: '2026-06-27T17:14:35.075131Z'
schema_version: 1
---

פירוק לראשוניים: $a = \prod p_i^{\alpha_i}$, $b = \prod p_i^{\beta_i}$. אז $\gcd(a, b) = \prod p_i^{\min(\alpha_i, \beta_i)}$ ו-$\text{lcm}(a, b) = \prod p_i^{\max(\alpha_i, \beta_i)}$.

מהזהות $\min(\alpha, \beta) + \max(\alpha, \beta) = \alpha + \beta$: $\gcd \cdot \text{lcm} = \prod p_i^{\alpha_i + \beta_i} = a \cdot b$. $\blacksquare$
