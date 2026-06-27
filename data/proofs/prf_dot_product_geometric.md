---
id: prf_dot_product_geometric
claim_id: thm_dot_product_geometric
method: informal
status: reviewed
dependencies:
- def_dot_product
- def_vector_magnitude
- thm_law_of_cosines
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

במשולש שנוצר מ-$\vec{u}, \vec{v}, \vec{u} - \vec{v}$, לפי משפט הקוסינוסים: $|\vec{u} - \vec{v}|^2 = |\vec{u}|^2 + |\vec{v}|^2 - 2|\vec{u}||\vec{v}|\cos\theta$.

מצד שני, $|\vec{u} - \vec{v}|^2 = (\vec{u} - \vec{v}) \cdot (\vec{u} - \vec{v}) = |\vec{u}|^2 - 2 \vec{u} \cdot \vec{v} + |\vec{v}|^2$.

השוואה: $\vec{u} \cdot \vec{v} = |\vec{u}||\vec{v}|\cos\theta$. $\blacksquare$
