---
id: prf_fraction_multiplication
claim_id: thm_fraction_multiplication
method: informal
status: reviewed
dependencies:
- def_fraction
- ax_multiplication_associativity
- ax_multiplication_commutativity
is_canonical: true
date_added: '2026-06-27T15:58:40.082207Z'
schema_version: 1
---

$\frac{a}{b} \cdot \frac{c}{d} = (a \cdot b^{-1}) \cdot (c \cdot d^{-1}) = (a \cdot c) \cdot (b^{-1} \cdot d^{-1}) = (a \cdot c) \cdot (b \cdot d)^{-1} = \frac{a \cdot c}{b \cdot d}$

(אסוציאטיביות וקומוטטיביות הכפל; $b^{-1} \cdot d^{-1} = (bd)^{-1}$ מההגדרה). $\blacksquare$
