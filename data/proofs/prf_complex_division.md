---
id: prf_complex_division
claim_id: thm_complex_division
method: informal
status: reviewed
dependencies:
- def_complex_conjugate
- def_modulus_complex
- thm_complex_multiplication
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

$\frac{z_1}{z_2} = \frac{z_1 \cdot \bar{z_2}}{z_2 \cdot \bar{z_2}}$. 

$z_2 \cdot \bar{z_2} = (c + di)(c - di) = c^2 + d^2 = |z_2|^2$ (ממשי וחיובי).

לכן $\frac{z_1}{z_2} = \frac{z_1 \bar{z_2}}{|z_2|^2}$. $\blacksquare$
