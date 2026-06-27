---
id: prf_ratio_test_radius
claim_id: thm_ratio_test_radius
method: informal
status: reviewed
dependencies:
- thm_ratio_test
- def_radius_of_convergence
is_canonical: true
date_added: '2026-06-27T18:48:38.235747Z'
schema_version: 1
---

מבחן המנה על הטור $\sum a_n x^n$: $\lim |a_{n+1} x^{n+1} / (a_n x^n)| = |x| \lim |a_{n+1}/a_n|$.

מתכנס כש $|x| \lim |a_{n+1}/a_n| < 1$, כלומר $|x| < 1/\lim |a_{n+1}/a_n| = \lim |a_n/a_{n+1}|$. וזה $R$. $\blacksquare$
