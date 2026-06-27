---
id: prf_derivative_sum
claim_id: thm_derivative_sum
method: informal
status: reviewed
dependencies:
- def_derivative_at_point
- thm_limit_sum
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

$(f+g)'(x) = \lim_{h \to 0} \frac{(f+g)(x+h) - (f+g)(x)}{h} = \lim_{h \to 0} \left[\frac{f(x+h) - f(x)}{h} + \frac{g(x+h) - g(x)}{h}\right]$.

לפי גבול של סכום: $= f'(x) + g'(x)$. $\blacksquare$
