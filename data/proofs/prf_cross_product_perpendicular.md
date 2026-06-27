---
id: prf_cross_product_perpendicular
claim_id: thm_cross_product_perpendicular
method: informal
status: reviewed
dependencies:
- def_cross_product
- def_dot_product
is_canonical: true
date_added: '2026-06-27T16:34:26.423690Z'
schema_version: 1
---

$\vec{u} \cdot (\vec{u} \times \vec{v}) = u_1(u_2 v_3 - u_3 v_2) + u_2(u_3 v_1 - u_1 v_3) + u_3(u_1 v_2 - u_2 v_1)$

$= u_1 u_2 v_3 - u_1 u_3 v_2 + u_2 u_3 v_1 - u_2 u_1 v_3 + u_3 u_1 v_2 - u_3 u_2 v_1 = 0$ (זוגות מבטלים זה את זה).

באופן דומה $\vec{v} \cdot (\vec{u} \times \vec{v}) = 0$. $\blacksquare$
