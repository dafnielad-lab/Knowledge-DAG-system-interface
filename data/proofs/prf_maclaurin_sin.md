---
id: prf_maclaurin_sin
claim_id: thm_maclaurin_sin
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

$\sin(0) = 0$, $\sin'(0) = \cos(0) = 1$, $\sin''(0) = -\sin(0) = 0$, $\sin'''(0) = -\cos(0) = -1$. המחזור 4 חוזר.

רק חזקות אי-זוגיות $x^{2k+1}$ נשארות, עם סימנים מתחלפים: $\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}$. $\blacksquare$
