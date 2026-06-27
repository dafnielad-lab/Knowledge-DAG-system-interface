---
id: prf_maclaurin_ln_one_plus_x
claim_id: thm_maclaurin_ln_one_plus_x
method: informal
status: reviewed
dependencies:
- thm_derivative_log_natural
- def_maclaurin_series
is_canonical: true
date_added: '2026-06-27T18:47:27.564532Z'
schema_version: 1
---

$f(x) = \ln(1+x)$. נגזרות: $f'(x) = \frac{1}{1+x}$, $f''(x) = -\frac{1}{(1+x)^2}$, $f^{(n)}(x) = \frac{(-1)^{n-1}(n-1)!}{(1+x)^n}$.

ערכים ב-$0$: $f^{(n)}(0) = (-1)^{n-1}(n-1)!$. הצבה במקלורין: $\sum_n \frac{(-1)^{n-1}(n-1)!}{n!} x^n = \sum \frac{(-1)^{n-1} x^n}{n}$. $\blacksquare$
