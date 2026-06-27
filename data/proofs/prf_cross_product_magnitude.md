---
id: prf_cross_product_magnitude
claim_id: thm_cross_product_magnitude
method: informal
status: reviewed
dependencies:
- def_cross_product
- def_vector_magnitude
- thm_sin_cos_pythagorean
- thm_dot_product_geometric
is_canonical: true
date_added: '2026-06-27T16:34:26.423690Z'
schema_version: 1
---

$|\vec{u} \times \vec{v}|^2 = |\vec{u}|^2 |\vec{v}|^2 - (\vec{u} \cdot \vec{v})^2$ (זהות לגראנז׳, מתקבלת מפתיחה ישירה של הגדרת המכפלה הוקטורית).

$= |\vec{u}|^2 |\vec{v}|^2 - |\vec{u}|^2 |\vec{v}|^2 \cos^2\theta = |\vec{u}|^2 |\vec{v}|^2 \sin^2\theta$.

שורש: $|\vec{u} \times \vec{v}| = |\vec{u}| |\vec{v}| |\sin\theta| = |\vec{u}| |\vec{v}| \sin\theta$ (זווית $\theta \in [0, \pi]$ מבטיחה $\sin \geq 0$). $\blacksquare$
