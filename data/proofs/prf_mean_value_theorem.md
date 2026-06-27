---
id: prf_mean_value_theorem
claim_id: thm_mean_value_theorem
method: informal
status: reviewed
dependencies:
- thm_rolle_theorem
- thm_derivative_sum
- thm_derivative_constant_multiple
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

נגדיר $h(x) := f(x) - \frac{f(b) - f(a)}{b - a}(x - a)$. אז $h(a) = h(b) = f(a)$, ו-$h$ רציפה וגזירה.

לפי רול קיים $c$ עם $h'(c) = 0$, כלומר $f'(c) - \frac{f(b) - f(a)}{b - a} = 0$, ולכן $f'(c) = \frac{f(b) - f(a)}{b - a}$. $\blacksquare$
