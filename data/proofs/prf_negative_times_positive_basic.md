---
id: prf_negative_times_positive_basic
claim_id: thm_negative_times_positive_basic
method: informal
status: reviewed
dependencies:
- ax_distributive_law
- ax_additive_inverse
- ax_additive_identity
- thm_multiplication_by_zero
- thm_additive_inverse_uniqueness
is_canonical: true
date_added: '2026-06-27T20:38:28.101554Z'
schema_version: 1
---

נראה ש-$(-a) \cdot b$ הוא הנגדי של $a \cdot b$, ומיחידות הנגדי ינבע ש-$(-a) \cdot b = -(a \cdot b)$.

$(-a) \cdot b + a \cdot b = ((-a) + a) \cdot b$ (חוק הפילוג הימני — או הימני המוכח)

$= 0 \cdot b$ (לפי איבר נגדי)

$= 0$ (משפט אפס בכפל).

לכן $(-a) \cdot b$ הוא הנגדי של $a \cdot b$, ומיחידות הנגדי $(-a) \cdot b = -(a \cdot b)$. $\blacksquare$
