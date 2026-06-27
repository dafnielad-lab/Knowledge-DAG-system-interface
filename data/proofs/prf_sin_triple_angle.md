---
id: prf_sin_triple_angle
claim_id: thm_sin_triple_angle
method: informal
status: reviewed
dependencies:
- thm_sin_addition_formula
- thm_sin_double_angle
- thm_cos_double_angle
- thm_sin_cos_pythagorean
is_canonical: true
date_added: '2026-06-27T18:26:22.743198Z'
schema_version: 1
---

$\sin(3\alpha) = \sin(2\alpha + \alpha) = \sin 2\alpha \cos\alpha + \cos 2\alpha \sin\alpha = 2 \sin\alpha\cos^2\alpha + (1 - 2\sin^2\alpha) \sin\alpha$.

$= 2 \sin\alpha(1 - \sin^2\alpha) + \sin\alpha - 2\sin^3\alpha = 3\sin\alpha - 4\sin^3\alpha$. $\blacksquare$
