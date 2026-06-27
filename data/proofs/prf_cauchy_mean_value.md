---
id: prf_cauchy_mean_value
claim_id: thm_cauchy_mean_value
method: informal
status: reviewed
dependencies:
- thm_rolle_theorem
- thm_derivative_sum
is_canonical: true
date_added: '2026-06-27T18:47:27.564532Z'
schema_version: 1
---

**הוכחה.** נגדיר $h(x) := f(x)[g(b) - g(a)] - g(x)[f(b) - f(a)]$.

אז $h(a) = h(b) = f(a) g(b) - g(a) f(b)$ (קלכלילה ישירה).

לפי רול קיים $c$ עם $h'(c) = 0$: $f'(c)[g(b)-g(a)] = g'(c)[f(b)-f(a)]$, וחלוקה ב-$g'(c)[g(b)-g(a)]$ נותנת את המסקנה. $\blacksquare$
