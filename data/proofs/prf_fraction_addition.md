---
id: prf_fraction_addition
claim_id: thm_fraction_addition
method: informal
status: reviewed
dependencies:
- def_fraction
- ax_distributive_law
- ax_multiplication_associativity
- ax_multiplication_commutativity
- ax_multiplicative_inverse
is_canonical: true
date_added: '2026-06-27T15:58:40.082207Z'
schema_version: 1
---

$\frac{a}{b} + \frac{c}{d} = a \cdot b^{-1} + c \cdot d^{-1}$. נכפול ונחלק במכנה משותף $b \cdot d$:

$= \frac{a \cdot d}{b \cdot d} + \frac{c \cdot b}{d \cdot b} = \frac{a \cdot d + b \cdot c}{b \cdot d}$

(לפי שוויון שברים וחוק הפילוג). $\blacksquare$
