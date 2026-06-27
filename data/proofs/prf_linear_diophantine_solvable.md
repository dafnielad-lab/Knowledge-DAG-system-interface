---
id: prf_linear_diophantine_solvable
claim_id: thm_linear_diophantine_solvable
method: informal
status: reviewed
dependencies:
- thm_bezout_identity
- def_gcd
is_canonical: true
date_added: '2026-06-27T18:26:22.743198Z'
schema_version: 1
---

($\Leftarrow$) אם $\gcd(a, b) \mid c$, נכתב $c = \gcd(a,b) \cdot k$. מזהות בזו $\gcd(a, b) = a x_0 + b y_0$. כפל ב-$k$: $c = a(kx_0) + b(ky_0)$.

($\Rightarrow$) אם $ax + by = c$ עבור שלמים, אז כל מחלק משותף של $a, b$ מחלק את הצד השמאלי ולכן את $c$. בפרט $\gcd(a,b) \mid c$. $\blacksquare$
