---
id: prf_triangle_area_cross_product
claim_id: thm_triangle_area_cross_product
method: informal
status: reviewed
dependencies:
- thm_cross_product_magnitude
- thm_triangle_area_sin
is_canonical: true
date_added: '2026-06-27T20:41:51.335588Z'
schema_version: 1
---

יהי $\triangle ABC$. נסמן $\vec u = \vec{AB}$ ו-$\vec v = \vec{AC}$, ויהי $\theta$ הזווית ב-$A$.

לפי משפט גודל המכפלה הוקטורית: $\|\vec u \times \vec v\| = \|\vec u\| \cdot \|\vec v\| \cdot \sin \theta = |AB| \cdot |AC| \cdot \sin \theta$.

לפי משפט שטח משולש לפי סינוס: $S(\triangle ABC) = \tfrac{1}{2} |AB| \cdot |AC| \cdot \sin \theta = \tfrac{1}{2} \|\vec u \times \vec v\| = \tfrac{1}{2} \|\vec{AB} \times \vec{AC}\|$. $\blacksquare$
