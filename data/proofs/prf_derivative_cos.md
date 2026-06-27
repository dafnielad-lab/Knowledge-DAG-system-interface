---
id: prf_derivative_cos
claim_id: thm_derivative_cos
method: informal
status: reviewed
dependencies:
- def_derivative_at_point
- thm_cos_addition_formula
- thm_limit_sin_over_x
- thm_derivative_sin
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

$(\cos x)' = \lim_{h \to 0} \frac{\cos(x+h) - \cos x}{h} = \lim_{h \to 0} \frac{\cos x \cos h - \sin x \sin h - \cos x}{h}$

$= \cos x \cdot 0 - \sin x \cdot 1 = -\sin x$. $\blacksquare$
