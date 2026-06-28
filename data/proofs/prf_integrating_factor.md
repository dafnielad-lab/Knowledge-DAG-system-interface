---
id: prf_integrating_factor
claim_id: thm_integrating_factor
method: informal
status: reviewed
dependencies:
- def_linear_first_order_ode
- thm_derivative_product
is_canonical: true
date_added: '2026-06-28T15:07:55.521049Z'
schema_version: 1
---

כפל ב-$\mu(x) = e^{\int p \, dx}$ נותן $\mu y' + \mu p y = \mu q$.

צד שמאל הוא בדיוק $(\mu y)'$ (לפי כלל מכפלה: $(\mu y)' = \mu' y + \mu y' = \mu p y + \mu y'$).

אז $(\mu y)' = \mu q$, אינטגרציה: $\mu y = \int \mu q \, dx + C$. חלוקה ב-$\mu$ נותנת את $y$. $\blacksquare$
