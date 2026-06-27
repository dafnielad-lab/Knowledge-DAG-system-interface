---
id: prf_cos_triple_angle
claim_id: thm_cos_triple_angle
method: informal
status: reviewed
dependencies:
- thm_cos_addition_formula
- thm_sin_double_angle
- thm_cos_double_angle
- thm_sin_cos_pythagorean
is_canonical: true
date_added: '2026-06-27T18:26:22.743198Z'
schema_version: 1
---

$\cos(3\alpha) = \cos(2\alpha + \alpha) = \cos 2\alpha \cos\alpha - \sin 2\alpha \sin\alpha = (2\cos^2\alpha - 1)\cos\alpha - 2\sin\alpha\cos\alpha\sin\alpha$.

$= 2\cos^3\alpha - \cos\alpha - 2(1 - \cos^2\alpha)\cos\alpha = 4\cos^3\alpha - 3\cos\alpha$. $\blacksquare$
