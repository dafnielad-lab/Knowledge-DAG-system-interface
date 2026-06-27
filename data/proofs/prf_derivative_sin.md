---
id: prf_derivative_sin
claim_id: thm_derivative_sin
method: informal
status: reviewed
dependencies:
- def_derivative_at_point
- thm_sin_addition_formula
- thm_limit_sin_over_x
- thm_limit_sum
- thm_limit_product
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

$(\sin x)' = \lim_{h \to 0} \frac{\sin(x+h) - \sin x}{h} = \lim_{h \to 0} \frac{\sin x \cos h + \cos x \sin h - \sin x}{h}$

$= \sin x \cdot \lim_{h \to 0} \frac{\cos h - 1}{h} + \cos x \cdot \lim_{h \to 0} \frac{\sin h}{h} = \sin x \cdot 0 + \cos x \cdot 1 = \cos x$.

(הגבול הראשון $0$ מתקבל מ-$\cos h - 1 = -2 \sin^2(h/2)$.) $\blacksquare$
