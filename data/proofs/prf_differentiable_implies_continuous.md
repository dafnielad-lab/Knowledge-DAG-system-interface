---
id: prf_differentiable_implies_continuous
claim_id: thm_differentiable_implies_continuous
method: informal
status: reviewed
dependencies:
- def_derivative_at_point
- def_continuity_at_point
- thm_limit_product
- thm_limit_sum
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

אם $f$ גזירה ב-$x_0$, אז $\lim_{h \to 0} \frac{f(x_0+h) - f(x_0)}{h} = f'(x_0)$ קיים.

$\lim_{h \to 0} (f(x_0+h) - f(x_0)) = \lim_{h \to 0} h \cdot \frac{f(x_0+h) - f(x_0)}{h} = 0 \cdot f'(x_0) = 0$.

כלומר $\lim_{h \to 0} f(x_0+h) = f(x_0)$, וזו רציפות ב-$x_0$. $\blacksquare$
