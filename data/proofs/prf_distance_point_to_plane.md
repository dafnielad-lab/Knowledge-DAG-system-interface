---
id: prf_distance_point_to_plane
claim_id: thm_distance_point_to_plane
method: informal
status: reviewed
dependencies:
- def_equation_of_plane
- def_dot_product
- def_vector_magnitude
is_canonical: true
date_added: '2026-06-27T16:34:26.423690Z'
schema_version: 1
---

הנורמל למישור הוא $\vec{n} = (a, b, c)$. ההיטל של וקטור מנקודה במישור $\vec{P_0}$ לנקודה $\vec{P}$ על כיוון $\vec{n}$ נותן את המרחק:

$d = \frac{|\vec{n} \cdot (\vec{P} - \vec{P_0})|}{|\vec{n}|} = \frac{|a x_0 + b y_0 + c z_0 - d|}{\sqrt{a^2 + b^2 + c^2}}$. $\blacksquare$
