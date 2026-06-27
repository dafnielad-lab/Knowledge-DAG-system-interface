---
id: prf_integrating_factor
claim_id: thm_integrating_factor
method: informal
status: reviewed
dependencies:
- def_linear_first_order_ode
- thm_derivative_product
- thm_derivative_exp
- thm_integral_substitution
is_canonical: true
date_added: '2026-06-27T18:26:22.743198Z'
schema_version: 1
---

כפל ב-$\mu(x) = e^{\int p \, dx}$ נותן $\mu y' + \mu p y = \mu q$.

צד שמאל הוא בדיוק $(\mu y)'$ (לפי כלל מכפלה: $(\mu y)' = \mu' y + \mu y' = \mu p y + \mu y'$).

אז $(\mu y)' = \mu q$, אינטגרציה: $\mu y = \int \mu q \, dx + C$. חלוקה ב-$\mu$ נותנת את $y$. $\blacksquare$
