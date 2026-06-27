---
id: prf_expected_value_linearity
claim_id: thm_expected_value_linearity
method: informal
status: reviewed
dependencies:
- def_expected_value
- ax_distributive_law
- ax_addition_commutativity
is_canonical: true
date_added: '2026-06-27T17:22:39.263705Z'
schema_version: 1
---

$E[aX + bY] = \sum_{x, y} (ax + by) P(X = x, Y = y) = a \sum_x x \sum_y P(x, y) + b \sum_y y \sum_x P(x, y) = a E[X] + b E[Y]$.

(ההוכחה לרציף זהה עם אינטגרלים.) הזהות לא דורשת אי-תלות בין $X$ ו-$Y$. $\blacksquare$
