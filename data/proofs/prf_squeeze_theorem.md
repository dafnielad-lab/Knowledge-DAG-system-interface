---
id: prf_squeeze_theorem
claim_id: thm_squeeze_theorem
method: informal
status: reviewed
dependencies:
- def_limit_of_sequence
is_canonical: true
date_added: '2026-06-27T17:14:35.075131Z'
schema_version: 1
---

מ-$\lim a_n = L$: לכל $\epsilon > 0$ קיים $N_1$ כך שלכל $n > N_1$, $L - \epsilon < a_n$. דומה ל-$c_n < L + \epsilon$ עבור $n > N_2$.

ל-$n > \max(N_1, N_2)$: $L - \epsilon < a_n \leq b_n \leq c_n < L + \epsilon$, כלומר $|b_n - L| < \epsilon$. לכן $\lim b_n = L$. $\blacksquare$
