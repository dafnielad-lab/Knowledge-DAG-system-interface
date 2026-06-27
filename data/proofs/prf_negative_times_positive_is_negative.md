---
id: prf_negative_times_positive_is_negative
claim_id: thm_negative_times_positive_is_negative
method: informal
status: reviewed
dependencies:
- ax_addition_preserves_order
- ax_positive_multiplication_preserves_order
- ax_additive_identity
- ax_additive_inverse
- thm_multiplication_by_negative_one
- thm_double_negation
- thm_product_of_negatives
is_canonical: true
date_added: '2026-06-27T15:32:36.129981Z'
schema_version: 1
---

מ-$a < 0$ נוסיף $-a$ לשני האגפים: $a + (-a) < 0 + (-a)$, כלומר $0 < -a$.

עכשיו $-a > 0$ ו-$b > 0$, ולפי שימור סדר בכפל בחיובי: $0 \cdot b < (-a) \cdot b$, כלומר $0 < (-a) \cdot b = -(a \cdot b)$ (לפי מכפלת נגדי בחיובי).

מכאן $a \cdot b < 0$. $\blacksquare$
