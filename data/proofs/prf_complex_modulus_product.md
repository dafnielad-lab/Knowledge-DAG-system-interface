---
id: prf_complex_modulus_product
claim_id: thm_complex_modulus_product
method: informal
status: reviewed
dependencies:
- def_modulus_complex
- thm_complex_multiplication
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

נסמן $z_1 = a + bi, z_2 = c + di$. $z_1 z_2 = (ac - bd) + (ad + bc) i$, אז $|z_1 z_2|^2 = (ac - bd)^2 + (ad + bc)^2$.

פתיחה: $= a^2 c^2 - 2abcd + b^2 d^2 + a^2 d^2 + 2abcd + b^2 c^2 = (a^2 + b^2)(c^2 + d^2) = |z_1|^2 |z_2|^2$.

שורש: $|z_1 z_2| = |z_1| \cdot |z_2|$. $\blacksquare$
