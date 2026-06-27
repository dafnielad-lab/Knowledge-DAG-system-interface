---
id: prf_product_of_negatives
claim_id: thm_product_of_negatives
method: informal
status: reviewed
dependencies:
- ax_distributive_law
- ax_additive_inverse
- thm_multiplication_by_zero
- thm_double_negation
- thm_additive_inverse_uniqueness
is_canonical: true
date_added: '2026-06-27T15:32:36.129981Z'
schema_version: 1
---

נראה ש-$(-a) \cdot b = -(a \cdot b)$:

$(-a) \cdot b + a \cdot b = ((-a) + a) \cdot b = 0 \cdot b = 0$, ולכן $(-a) \cdot b$ הוא הנגדי של $a \cdot b$, כלומר $-(ab)$.

באותה דרך, $(-a) \cdot (-b) + (-a) \cdot b = (-a) \cdot ((-b) + b) = (-a) \cdot 0 = 0$, ולכן $(-a)(-b) = -((-a) \cdot b) = -(-(ab)) = ab$ (לפי ניוד כפול). $\blacksquare$
