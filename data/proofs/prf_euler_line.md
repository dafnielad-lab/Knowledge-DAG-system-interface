---
id: prf_euler_line
claim_id: thm_euler_line
method: informal
status: reviewed
dependencies:
- def_centroid
- def_circumcenter
- def_orthocenter
- thm_medians_meet_at_centroid
- def_vector_2d
is_canonical: true
date_added: '2026-06-27T17:22:39.263705Z'
schema_version: 1
---

**הוכחה וקטורית.** סדר $O$ בראשית. אז $\vec{G} = \frac{1}{3}(\vec{A} + \vec{B} + \vec{C})$ ולפי תכונה ידועה $\vec{H} = \vec{A} + \vec{B} + \vec{C}$.

לכן $\vec{H} = 3\vec{G}$, כלומר $O, G, H$ קולינאריים עם $\vec{OH} = 3 \vec{OG}$, ובמיוחד $\vec{HG} = -2 \vec{OG}$, $|HG| = 2 |GO|$. $\blacksquare$
