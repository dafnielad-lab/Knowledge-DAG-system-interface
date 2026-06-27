---
id: prf_derivative_inverse_function
claim_id: thm_derivative_inverse_function
method: informal
status: reviewed
dependencies:
- def_inverse_function
- thm_derivative_chain
is_canonical: true
date_added: '2026-06-27T17:14:35.075131Z'
schema_version: 1
---

מההגדרה $f(f^{-1}(y)) = y$ לכל $y$ בתחום. גזירה לפי $y$ עם כלל השרשרת: $f'(f^{-1}(y)) \cdot (f^{-1})'(y) = 1$, ולכן $(f^{-1})'(y) = \frac{1}{f'(f^{-1}(y))}$. $\blacksquare$
