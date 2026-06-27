---
id: prf_variance_sum_independent
claim_id: thm_variance_sum_independent
method: informal
status: reviewed
dependencies:
- def_variance_rv
- def_expected_value
- def_independent_random_variables
- thm_expected_value_linearity
is_canonical: true
date_added: '2026-06-27T17:22:39.263705Z'
schema_version: 1
---

$\text{Var}(X + Y) = E[(X + Y)^2] - (E[X + Y])^2 = E[X^2 + 2XY + Y^2] - (E[X] + E[Y])^2$

$= E[X^2] + 2E[XY] + E[Y^2] - E[X]^2 - 2E[X]E[Y] - E[Y]^2$.

בהינתן אי-תלות, $E[XY] = E[X]E[Y]$, אז המקדם של 2 מתבטל. נשאר $\text{Var}(X) + \text{Var}(Y)$. $\blacksquare$
