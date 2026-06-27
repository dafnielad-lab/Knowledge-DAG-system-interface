---
id: prf_distance_point_to_line_3d
claim_id: thm_distance_point_to_line_3d
method: informal
status: reviewed
dependencies:
- def_cross_product
- thm_cross_product_magnitude
- def_vector_magnitude
is_canonical: true
date_added: '2026-06-27T18:26:22.743198Z'
schema_version: 1
---

המרחק מ-$P$ לישר הוא רכיב $\vec{P_0 P}$ המאונך ל-$\vec{v}$. גודל המכפלה הוקטורית $|\vec{P_0 P} \times \vec{v}| = |\vec{P_0 P}| \cdot |\vec{v}| \sin\theta$, ולכן $|\vec{P_0 P}| \sin\theta = \frac{|\vec{P_0 P} \times \vec{v}|}{|\vec{v}|}$ — זה המרחק. $\blacksquare$
