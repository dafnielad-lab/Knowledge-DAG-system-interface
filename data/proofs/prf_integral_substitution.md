---
id: prf_integral_substitution
claim_id: thm_integral_substitution
method: informal
status: reviewed
dependencies:
- thm_derivative_chain
- def_antiderivative
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

אם $F$ קדומה של $f$, אז $(F(g(x)))' = F'(g(x)) \cdot g'(x) = f(g(x)) \cdot g'(x)$ (לפי כלל השרשרת).

לכן $F(g(x))$ קדומה של $f(g(x)) \cdot g'(x)$, כלומר $\int f(g(x)) g'(x) \, dx = F(g(x)) + C = \int f(u) \, du$. $\blacksquare$
