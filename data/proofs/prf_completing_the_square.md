---
id: prf_completing_the_square
claim_id: thm_completing_the_square
method: informal
status: reviewed
dependencies:
- def_natural_power
- ax_distributive_law
- thm_right_distributive_law
- ax_addition_commutativity
- ax_addition_associativity
- thm_addition_undoes_subtraction
is_canonical: true
date_added: '2026-06-27T20:38:28.101554Z'
schema_version: 1
---

נחשב את $\left(x + \tfrac{b}{2}\right)^2$:

$\left(x + \tfrac{b}{2}\right)^2 = \left(x + \tfrac{b}{2}\right) \cdot \left(x + \tfrac{b}{2}\right)$

$= x \cdot x + x \cdot \tfrac{b}{2} + \tfrac{b}{2} \cdot x + \tfrac{b}{2} \cdot \tfrac{b}{2}$ (פילוג דו-צדדי)

$= x^2 + 2 \cdot \tfrac{b}{2} \cdot x + \tfrac{b^2}{4}$ (קומוטטיביות וצמצום)

$= x^2 + b x + \tfrac{b^2}{4}$.

נחסר $\tfrac{b^2}{4}$ משני האגפים: $x^2 + b x = \left(x + \tfrac{b}{2}\right)^2 - \tfrac{b^2}{4}$. $\blacksquare$
