---
id: prf_difference_of_squares
claim_id: thm_difference_of_squares
method: informal
status: reviewed
dependencies:
- def_natural_power
- def_subtraction
- ax_distributive_law
- thm_right_distributive_law
- ax_addition_commutativity
- ax_addition_associativity
- ax_additive_inverse
- ax_additive_identity
- thm_product_of_negatives
is_canonical: true
date_added: '2026-06-27T15:32:36.129981Z'
schema_version: 1
---

$(a - b)(a + b) = (a + (-b))(a + b)$ (הגדרת חיסור)

$= a \cdot a + a \cdot b + (-b) \cdot a + (-b) \cdot b$ (פילוג ימני ושמאלי)

$= a^2 + ab + (-(ba)) + (-(b^2))$ (לפי מכפלת נגדי)

$= a^2 + ab - ab - b^2 = a^2 - b^2$ (קומוטטיביות, איבר נגדי, ואיבר ניטרלי). $\blacksquare$
