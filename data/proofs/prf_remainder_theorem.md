---
id: prf_remainder_theorem
claim_id: thm_remainder_theorem
method: informal
status: reviewed
dependencies:
- def_polynomial
- thm_polynomial_division_algorithm
is_canonical: true
date_added: '2026-06-27T20:41:51.335588Z'
schema_version: 1
---

יהי $p(x)$ פולינום ו-$a \in \mathbb{R}$. נחלק את $p(x)$ ב-$(x - a)$ לפי אלגוריתם החילוק לפולינומים: קיימים $q(x), r(x)$ יחידים עם $p(x) = q(x)(x - a) + r(x)$ ו-$\deg r < \deg(x - a) = 1$.

$\deg r < 1$ אומר ש-$r(x)$ הוא קבוע — נסמן $r(x) \equiv r$.

נציב $x = a$: $p(a) = q(a) \cdot (a - a) + r = q(a) \cdot 0 + r = r$.

לכן השארית בחלוקת $p(x)$ ב-$(x - a)$ היא $r = p(a)$. $\blacksquare$
