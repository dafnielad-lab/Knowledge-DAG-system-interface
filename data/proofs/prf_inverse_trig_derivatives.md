---
id: prf_inverse_trig_derivatives
claim_id: thm_inverse_trig_derivatives
method: informal
status: reviewed
dependencies:
- thm_derivative_inverse_function
- thm_derivative_sin
- thm_derivative_cos
- thm_derivative_tan
- thm_sin_cos_pythagorean
is_canonical: true
date_added: '2026-06-27T17:14:35.075131Z'
schema_version: 1
---

**ארקסינוס:** $y = \arcsin x$, $\sin y = x$. גזירה: $\cos y \cdot y' = 1$, $y' = \frac{1}{\cos y} = \frac{1}{\sqrt{1 - \sin^2 y}} = \frac{1}{\sqrt{1 - x^2}}$.

**ארקקוסינוס:** אותה דרך, $-\sin y \cdot y' = 1$, ויוצא $-\frac{1}{\sqrt{1 - x^2}}$.

**ארקטנגנס:** $\tan y = x$, $\sec^2 y \cdot y' = 1$, $y' = \cos^2 y = \frac{1}{1 + \tan^2 y} = \frac{1}{1 + x^2}$. $\blacksquare$
