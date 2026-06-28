---
id: prf_newton_cooling_law
claim_id: thm_newton_cooling_law
method: informal
status: reviewed
dependencies:
- thm_exponential_ode_solution
is_canonical: true
date_added: '2026-06-28T15:07:55.534051Z'
schema_version: 1
---

נסמן $u = T - T_\text{env}$, אז $u' = T' = -k(T - T_\text{env}) = -ku$. לפי פתרון המעריכי: $u(t) = u_0 e^{-kt}$.

החזרה ל-$T$: $T(t) = T_\text{env} + (T_0 - T_\text{env}) e^{-kt}$. $\blacksquare$
