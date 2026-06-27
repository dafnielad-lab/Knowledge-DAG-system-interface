---
id: prf_square_nonnegative
claim_id: thm_square_nonnegative
method: informal
status: reviewed
dependencies:
- def_natural_power
- ax_order_trichotomy
- ax_positive_multiplication_preserves_order
- thm_product_of_negatives
- thm_multiplication_by_zero
is_canonical: true
date_added: '2026-06-27T15:32:36.129981Z'
schema_version: 1
---

לפי טריכוטומיה, או $a > 0$, $a = 0$, או $a < 0$.

אם $a = 0$: $a^2 = 0 \cdot 0 = 0 \geq 0$.

אם $a > 0$: לפי שימור סדר בכפל בחיובי, $0 \cdot a < a \cdot a$, כלומר $0 < a^2$.

אם $a < 0$: אז $-a > 0$, ו-$a^2 = a \cdot a = (-a) \cdot (-a) > 0$ (לפי המקרה הקודם ומכפלת שני נגדיים). $\blacksquare$
