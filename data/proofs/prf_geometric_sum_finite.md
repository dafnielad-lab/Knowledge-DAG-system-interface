---
id: prf_geometric_sum_finite
claim_id: thm_geometric_sum_finite
method: informal
status: reviewed
dependencies:
- def_geometric_sequence
- thm_geometric_nth_term
- ax_distributive_law
is_canonical: true
date_added: '2026-06-27T16:13:44.126814Z'
schema_version: 1
---

נסמן $S = a_1 + a_1 q + a_1 q^2 + \cdots + a_1 q^{n-1}$. נכפול ב-$q$: $qS = a_1 q + a_1 q^2 + \cdots + a_1 q^n$.

חיסור: $qS - S = a_1 q^n - a_1$, כלומר $S(q - 1) = a_1(q^n - 1)$.

עבור $q \neq 1$: $S = a_1 \cdot \frac{q^n - 1}{q - 1}$. עבור $q = 1$: כל איבר שווה ל-$a_1$, סכום $n \cdot a_1$. $\blacksquare$
