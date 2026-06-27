---
id: prf_fraction_equality
claim_id: thm_fraction_equality
method: informal
status: reviewed
dependencies:
- def_fraction
- ax_multiplicative_inverse
- ax_multiplication_associativity
- ax_multiplication_commutativity
is_canonical: true
date_added: '2026-06-27T15:58:40.082207Z'
schema_version: 1
---

($\Rightarrow$) אם $\frac{a}{b} = \frac{c}{d}$ אז $a \cdot b^{-1} = c \cdot d^{-1}$. נכפול שני האגפים ב-$b \cdot d$: $a \cdot d = c \cdot b$.

($\Leftarrow$) אם $a \cdot d = b \cdot c$ נכפול שני האגפים ב-$b^{-1} \cdot d^{-1}$: $a \cdot b^{-1} = c \cdot d^{-1}$, כלומר $\frac{a}{b} = \frac{c}{d}$. $\blacksquare$
