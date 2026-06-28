---
id: prf_integration_logarithmic
claim_id: thm_integration_logarithmic
method: informal
status: reviewed
dependencies:
- thm_integral_one_over_x
- thm_integral_substitution
is_canonical: true
date_added: '2026-06-28T15:07:55.522550Z'
schema_version: 1
---

הצבה $u = f(x)$, $du = f'(x) dx$. אז $\int \frac{f'(x)}{f(x)} dx = \int \frac{1}{u} du = \ln|u| + C = \ln|f(x)| + C$. $\blacksquare$
