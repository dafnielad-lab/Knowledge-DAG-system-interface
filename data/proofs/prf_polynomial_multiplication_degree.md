---
id: prf_polynomial_multiplication_degree
claim_id: thm_polynomial_multiplication_degree
method: informal
status: reviewed
dependencies:
- def_polynomial
- def_polynomial_degree
- thm_no_zero_divisors
is_canonical: true
date_added: '2026-06-27T16:03:56.114879Z'
schema_version: 1
---

נסמן $p(x) = a_m x^m + \ldots$ (עם $a_m \neq 0$), $q(x) = b_n x^n + \ldots$ (עם $b_n \neq 0$). 

במכפלה $p \cdot q$, המקדם של $x^{m+n}$ הוא $a_m \cdot b_n$, ולפי אי-קיום מחלקי אפס $a_m \cdot b_n \neq 0$. אין מקדם של חזקה גבוהה יותר. לכן $\deg(p \cdot q) = m + n$. $\blacksquare$
