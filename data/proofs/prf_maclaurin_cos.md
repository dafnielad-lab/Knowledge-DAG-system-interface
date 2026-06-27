---
id: prf_maclaurin_cos
claim_id: thm_maclaurin_cos
method: informal
status: reviewed
dependencies:
- def_maclaurin_series
- thm_derivative_sin
- thm_derivative_cos
is_canonical: true
date_added: '2026-06-27T17:22:39.263705Z'
schema_version: 1
---

$\cos(0) = 1$, $\cos'(0) = -\sin(0) = 0$, $\cos''(0) = -\cos(0) = -1$, $\cos'''(0) = \sin(0) = 0$. מחזור 4.

רק חזקות זוגיות נשארות: $\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}$. $\blacksquare$
