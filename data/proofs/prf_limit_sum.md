---
id: prf_limit_sum
claim_id: thm_limit_sum
method: informal
status: reviewed
dependencies:
- def_function_limit_formal
- thm_triangle_inequality
is_canonical: true
date_added: '2026-06-27T17:14:35.074631Z'
schema_version: 1
---

לכל $\epsilon > 0$ נבחר $\delta_f, \delta_g$ כך ש-$|f(x) - L| < \epsilon/2$ ו-$|g(x) - M| < \epsilon/2$ בהתאמה. ב-$\delta = \min(\delta_f, \delta_g)$:

$|(f(x) + g(x)) - (L + M)| \leq |f(x) - L| + |g(x) - M| < \epsilon/2 + \epsilon/2 = \epsilon$. $\blacksquare$
