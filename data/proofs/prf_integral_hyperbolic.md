---
id: prf_integral_hyperbolic
claim_id: thm_integral_hyperbolic
method: informal
status: reviewed
dependencies:
- def_hyperbolic_sin_cos
- thm_derivative_hyperbolic
- def_antiderivative
is_canonical: true
date_added: '2026-06-28T20:34:16.570707Z'
schema_version: 1
---

לפי `thm_derivative_hyperbolic`: $(\cosh x)' = \sinh x$ ו-$(\sinh x)' = \cosh x$.

לכן, לפי `def_antiderivative`:

- $\cosh x$ היא קדומה של $\sinh x$, כלומר $\int \sinh x \, dx = \cosh x + C$.
- $\sinh x$ היא קדומה של $\cosh x$, כלומר $\int \cosh x \, dx = \sinh x + C$.

ההגדרות `def_hyperbolic_sin_cos` נותנות $\sinh x = \frac{e^x - e^{-x}}{2}$ ו-$\cosh x = \frac{e^x + e^{-x}}{2}$, ואפשר לאמת ישירות: $\int \frac{e^x - e^{-x}}{2} \, dx = \frac{e^x + e^{-x}}{2} + C = \cosh x + C$, וכן לכיוון השני. $\blacksquare$
