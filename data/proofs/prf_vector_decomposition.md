---
id: prf_vector_decomposition
claim_id: thm_vector_decomposition
method: informal
status: reviewed
dependencies:
- def_vector_projection
- def_dot_product
is_canonical: true
date_added: '2026-06-27T18:26:22.743198Z'
schema_version: 1
---

נגדיר $\vec{u}_\perp := \vec{u} - \text{proj}_{\vec{v}} \vec{u}$.

אזי $\vec{u}_\perp \cdot \vec{v} = \vec{u} \cdot \vec{v} - \frac{\vec{u}\cdot\vec{v}}{|\vec{v}|^2} \vec{v} \cdot \vec{v} = \vec{u}\cdot\vec{v} - \vec{u}\cdot\vec{v} = 0$.

לכן $\vec{u}_\perp \perp \vec{v}$, ו-$\vec{u} = \text{proj}_{\vec{v}} \vec{u} + \vec{u}_\perp$ כפי שדרוש. $\blacksquare$
