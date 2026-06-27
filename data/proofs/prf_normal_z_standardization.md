---
id: prf_normal_z_standardization
claim_id: thm_normal_z_standardization
method: informal
status: reviewed
dependencies:
- def_normal_distribution
- thm_expected_value_linearity
- thm_variance_sum_independent
is_canonical: true
date_added: '2026-06-27T18:26:22.743198Z'
schema_version: 1
---

$Z = \frac{X - \mu}{\sigma}$. תוחלת: $E[Z] = \frac{E[X] - \mu}{\sigma} = 0$.

שונות: $\text{Var}(Z) = \frac{\text{Var}(X)}{\sigma^2} = 1$.

טרנספורמציה לינארית של $N$ נותנת $N$, אז $Z \sim N(0, 1)$. $\blacksquare$
