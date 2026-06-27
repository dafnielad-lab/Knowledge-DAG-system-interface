---
id: prf_derivative_constant_multiple
claim_id: thm_derivative_constant_multiple
method: informal
status: reviewed
dependencies:
- def_derivative_at_point
- thm_limit_product
- thm_limit_constant
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

$(cf)'(x) = \lim_{h \to 0} \frac{c \cdot f(x+h) - c \cdot f(x)}{h} = c \cdot \lim_{h \to 0} \frac{f(x+h) - f(x)}{h} = c \cdot f'(x)$. $\blacksquare$
