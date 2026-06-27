---
id: prf_position_velocity_acceleration
claim_id: thm_position_velocity_acceleration
method: informal
status: reviewed
dependencies:
- def_derivative_at_point
- thm_ftc_part2
is_canonical: true
date_added: '2026-06-27T18:26:22.743198Z'
schema_version: 1
---

מהגדרת מהירות = שינוי מיקום ביחס לזמן: $v(t) = x'(t)$. תאוצה = שינוי מהירות: $a(t) = v'(t) = x''(t)$.

ההיפוך לפי FTC חלק 2: $v(t) - v_0 = \int_0^t a(s) ds$, ובדומה $x(t) - x_0 = \int_0^t v(s) ds$. $\blacksquare$
