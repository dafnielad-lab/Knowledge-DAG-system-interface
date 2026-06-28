---
id: prf_hyperbolic_derivatives
claim_id: thm_hyperbolic_derivatives
method: informal
status: reviewed
dependencies:
- def_hyperbolic_sin_cos
- thm_derivative_exp
- thm_derivative_sum
- thm_derivative_quotient
- thm_hyperbolic_identity
is_canonical: true
date_added: '2026-06-28T15:07:55.514549Z'
schema_version: 1
---

$(\sinh x)' = \frac{(e^x - e^{-x})'}{2} = \frac{e^x + e^{-x}}{2} = \cosh x$.

$(\cosh x)' = \frac{(e^x + e^{-x})'}{2} = \frac{e^x - e^{-x}}{2} = \sinh x$.

$(\tanh x)' = \frac{\cosh^2 x - \sinh^2 x}{\cosh^2 x} = \frac{1}{\cosh^2 x}$ (זהות היפרבולית). $\blacksquare$
