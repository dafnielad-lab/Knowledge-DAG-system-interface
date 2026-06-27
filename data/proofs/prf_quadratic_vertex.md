---
id: prf_quadratic_vertex
claim_id: thm_quadratic_vertex
method: informal
status: reviewed
dependencies:
- def_quadratic_function
- ax_distributive_law
- def_natural_power
- thm_difference_of_squares
- thm_square_nonnegative
is_canonical: true
date_added: '2026-06-27T16:03:56.115377Z'
schema_version: 1
---

השלמת ריבוע: 

$f(x) = a x^2 + b x + c = a\!\left(x^2 + \tfrac{b}{a} x\right) + c = a\!\left(x + \tfrac{b}{2a}\right)^2 - \tfrac{b^2}{4a} + c$

מאחר ש-$(x + \tfrac{b}{2a})^2 \geq 0$ עם שוויון רק עבור $x = -\tfrac{b}{2a}$, הקיצון של $f$ מתקבל ב-$x = -\tfrac{b}{2a}$, בערך $c - \tfrac{b^2}{4a}$. $\blacksquare$
