---
id: prf_derivative_product
claim_id: thm_derivative_product
method: informal
status: reviewed
dependencies:
- def_derivative_at_point
- thm_differentiable_implies_continuous
- thm_limit_sum
- thm_limit_product
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

$\frac{f(x+h)g(x+h) - f(x)g(x)}{h} = \frac{f(x+h)g(x+h) - f(x)g(x+h) + f(x)g(x+h) - f(x)g(x)}{h}$

$= g(x+h) \cdot \frac{f(x+h) - f(x)}{h} + f(x) \cdot \frac{g(x+h) - g(x)}{h}$.

בגבול $h \to 0$: $g(x+h) \to g(x)$ (רציפות), והאיברים נותנים $g(x) f'(x) + f(x) g'(x)$. $\blacksquare$
