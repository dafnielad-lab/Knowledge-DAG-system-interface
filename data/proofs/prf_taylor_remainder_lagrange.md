---
id: prf_taylor_remainder_lagrange
claim_id: thm_taylor_remainder_lagrange
method: informal
status: reviewed
dependencies:
- thm_cauchy_mean_value
- def_higher_order_derivative
is_canonical: true
date_added: '2026-06-27T18:47:27.564532Z'
schema_version: 1
---

**הוכחה.** נגדיר $R_n(x) = f(x) - P_n(x)$, כאשר $P_n$ פולינום טיילור מסדר $n$. $R_n$ ו-$(x-a)^{n+1}$ מתאפסים $n+1$ פעמים ב-$a$.

שימוש חוזר במשפט קושי לערך הממוצע: $\frac{R_n(x)}{(x-a)^{n+1}} = \frac{R_n^{(n+1)}(\xi)}{(n+1)!} = \frac{f^{(n+1)}(\xi)}{(n+1)!}$. $\blacksquare$
