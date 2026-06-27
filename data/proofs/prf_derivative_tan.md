---
id: prf_derivative_tan
claim_id: thm_derivative_tan
method: informal
status: reviewed
dependencies:
- def_tan
- thm_derivative_quotient
- thm_derivative_sin
- thm_derivative_cos
- thm_sin_cos_pythagorean
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

$(\tan x)' = \left(\frac{\sin x}{\cos x}\right)' = \frac{\cos x \cdot \cos x - \sin x \cdot (-\sin x)}{\cos^2 x} = \frac{\cos^2 x + \sin^2 x}{\cos^2 x} = \frac{1}{\cos^2 x}$. $\blacksquare$
