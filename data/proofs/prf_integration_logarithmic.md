---
id: prf_integration_logarithmic
claim_id: thm_integration_logarithmic
method: informal
status: reviewed
dependencies:
- thm_integral_one_over_x
- thm_integral_substitution
- thm_derivative_log_natural
is_canonical: true
date_added: '2026-06-27T16:34:26.423690Z'
schema_version: 1
---

הצבה $u = f(x)$, $du = f'(x) dx$. אז $\int \frac{f'(x)}{f(x)} dx = \int \frac{1}{u} du = \ln|u| + C = \ln|f(x)| + C$. $\blacksquare$
