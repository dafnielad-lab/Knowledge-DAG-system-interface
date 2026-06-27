---
id: prf_absolute_value_zero_iff
claim_id: thm_absolute_value_zero_iff
method: informal
status: reviewed
dependencies:
- def_absolute_value
- thm_double_negation
is_canonical: true
date_added: '2026-06-27T15:32:36.129981Z'
schema_version: 1
---

($\Leftarrow$) אם $a = 0$ אז $|0| = 0$ (לפי המקרה $a \geq 0$ בהגדרה).

($\Rightarrow$) אם $|a| = 0$: במקרה $a \geq 0$ מקבלים $a = |a| = 0$. במקרה $a < 0$ מקבלים $-a = 0$, ולפי ניוד כפול $a = -(-a) = -0 = 0$, סתירה. $\blacksquare$
