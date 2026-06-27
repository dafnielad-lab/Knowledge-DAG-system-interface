---
id: prf_exponential_ode_solution
claim_id: thm_exponential_ode_solution
method: informal
status: reviewed
dependencies:
- def_separable_ode
- thm_integral_one_over_x
- thm_derivative_exp
is_canonical: true
date_added: '2026-06-27T18:26:22.743198Z'
schema_version: 1
---

המשוואה $y' = k y$ ניתנת להפרדה: $\frac{dy}{y} = k \, dt$.

אינטגרציה: $\ln|y| = kt + C_0$, ולכן $y = \pm e^{C_0} e^{kt} = C e^{kt}$ (הקבוע $C$ סופג את הסימן).

תנאי התחלה $y(0) = y_0$: $C = y_0$. ייחודיות נובעת מתורת ה-ODE הקלאסית. $\blacksquare$
