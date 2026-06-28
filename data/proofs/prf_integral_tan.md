---
id: prf_integral_tan
claim_id: thm_integral_tan
method: informal
status: reviewed
dependencies:
- def_tan
- thm_integral_substitution
- thm_derivative_cos
- thm_integral_one_over_x
- def_antiderivative
is_canonical: true
date_added: '2026-06-28T20:34:16.559662Z'
schema_version: 1
---

נכתוב $\tan x = \frac{\sin x}{\cos x}$ לפי `def_tan`.

נציב $u = \cos x$. לפי `thm_derivative_cos`: $\frac{du}{dx} = -\sin x$, ולכן $du = -\sin x \, dx$, כלומר $\sin x \, dx = -du$.

על פי `thm_integral_substitution`:

$$\int \tan x \, dx = \int \frac{\sin x}{\cos x} \, dx = \int \frac{-du}{u} = -\int \frac{1}{u} \, du.$$

לפי `thm_integral_one_over_x` נקבל $-\ln|u| + C = -\ln|\cos x| + C$.

בדיקה לפי `def_antiderivative`: $\left(-\ln|\cos x|\right)' = -\frac{1}{\cos x} \cdot (-\sin x) = \frac{\sin x}{\cos x} = \tan x$. $\blacksquare$
