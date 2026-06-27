---
id: prf_distance_point_to_line_2d
claim_id: thm_distance_point_to_line_2d
method: informal
status: reviewed
dependencies:
- thm_general_form_of_line
- def_dot_product
- def_vector_magnitude
is_canonical: true
date_added: '2026-06-27T17:14:35.074631Z'
schema_version: 1
---

הנורמל לישר $ax + by + c = 0$ הוא $\vec{n} = (a, b)$. עבור נקודה $P_0 = (x_0, y_0)$ ונקודה $Q$ על הישר: היטל $\vec{P_0 Q}$ על $\vec{n}$ נותן את המרחק.

חישוב: $d = \frac{|\vec{n} \cdot \vec{P_0 Q}|}{|\vec{n}|} = \frac{|a x_0 + b y_0 + c|}{\sqrt{a^2 + b^2}}$ (אחרי שמציבים שעל הישר $aQ_x + bQ_y + c = 0$). $\blacksquare$
