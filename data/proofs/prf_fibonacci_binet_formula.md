---
id: prf_fibonacci_binet_formula
claim_id: thm_fibonacci_binet_formula
method: informal
status: reviewed
dependencies:
- thm_linear_recurrence_characteristic
- def_recurrence_relation
is_canonical: true
date_added: '2026-06-27T18:47:27.564532Z'
schema_version: 1
---

פיבונאצ׳י: $F_{n+1} = F_n + F_{n-1}$, $F_0=0, F_1=1$.

משוואה אופיינית $x^2 = x + 1$, שורשים $\varphi = (1+\sqrt 5)/2$, $\psi = (1-\sqrt 5)/2$.

פתרון כללי $F_n = A\varphi^n + B\psi^n$. מתנאי התחלה: $A = 1/\sqrt 5$, $B = -1/\sqrt 5$. אז $F_n = \frac{\varphi^n - \psi^n}{\sqrt 5}$. $\blacksquare$
