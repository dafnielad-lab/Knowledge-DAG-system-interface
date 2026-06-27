---
id: prf_kinematic_no_time
claim_id: thm_kinematic_no_time
method: informal
status: reviewed
dependencies:
- def_motion_constant_acceleration
is_canonical: true
date_added: '2026-06-27T17:22:39.263705Z'
schema_version: 1
---

מ-$v = v_0 + at$ נבודד $t = (v - v_0)/a$. נציב ב-$x = x_0 + v_0 t + \tfrac{1}{2} a t^2$:

$x - x_0 = v_0 \cdot \frac{v - v_0}{a} + \frac{1}{2} a \cdot \frac{(v - v_0)^2}{a^2} = \frac{v^2 - v_0^2}{2a}$.

כפל ב-$2a$: $v^2 - v_0^2 = 2 a (x - x_0)$. $\blacksquare$
