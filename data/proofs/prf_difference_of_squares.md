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
- thm_negative_times_positive_basic
is_canonical: true
date_added: '2026-06-27T20:41:51.335588Z'
schema_version: 1
---

$(a - b)(a + b) = (a + (-b))(a + b)$ (הגדרת חיסור)

$= a \cdot a + a \cdot b + (-b) \cdot a + (-b) \cdot b$ (פילוג ימני ושמאלי)

$= a^2 + ab + (-(ba)) + (-(b \cdot b))$ (לפי מינוס חיובי שלילי)

$= a^2 + ab - ab - b^2 = a^2 - b^2$ (קומוטטיביות, איבר נגדי, ואיבר ניטרלי). $\blacksquare$
