---
id: prf_remainder_theorem
claim_id: thm_remainder_theorem
method: informal
status: reviewed
dependencies:
- def_polynomial
- thm_polynomial_multiplication_degree
is_canonical: true
date_added: '2026-06-27T16:03:56.115377Z'
schema_version: 1
---

מאלגוריתם החילוק של פולינומים: $p(x) = (x - a) \cdot Q(x) + R(x)$ עם $\deg R < \deg(x - a) = 1$, כלומר $R$ הוא קבוע $r$.

נציב $x = a$: $p(a) = (a - a) \cdot Q(a) + r = 0 + r = r$. 

לכן השארית $r = p(a)$. $\blacksquare$
