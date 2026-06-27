---
id: prf_triangle_inequality_vectors
claim_id: thm_triangle_inequality_vectors
method: informal
status: reviewed
dependencies:
- thm_cauchy_schwarz_inequality_vectors
- def_vector_magnitude
- def_dot_product
is_canonical: true
date_added: '2026-06-27T16:34:26.423690Z'
schema_version: 1
---

$|\vec{u} + \vec{v}|^2 = (\vec{u} + \vec{v}) \cdot (\vec{u} + \vec{v}) = |\vec{u}|^2 + 2 \vec{u} \cdot \vec{v} + |\vec{v}|^2$.

לפי קושי-שוורץ: $\vec{u} \cdot \vec{v} \leq |\vec{u}||\vec{v}|$. לכן $|\vec{u} + \vec{v}|^2 \leq (|\vec{u}| + |\vec{v}|)^2$, ובשורש: $|\vec{u} + \vec{v}| \leq |\vec{u}| + |\vec{v}|$. $\blacksquare$
