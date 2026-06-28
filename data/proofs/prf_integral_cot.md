---
id: prf_integral_cot
claim_id: thm_integral_cot
method: informal
status: reviewed
dependencies:
- def_secant_cosecant_cotangent
- thm_integral_substitution
- thm_derivative_sin
- thm_integral_one_over_x
- def_antiderivative
is_canonical: true
date_added: '2026-06-28T20:34:16.562173Z'
schema_version: 1
---

לפי `def_secant_cosecant_cotangent`: $\cot x = \frac{\cos x}{\sin x}$.

נציב $u = \sin x$. לפי `thm_derivative_sin`: $\frac{du}{dx} = \cos x$, ולכן $du = \cos x \, dx$.

על פי `thm_integral_substitution`:

$$\int \cot x \, dx = \int \frac{\cos x}{\sin x} \, dx = \int \frac{du}{u}.$$

לפי `thm_integral_one_over_x` נקבל $\ln|u| + C = \ln|\sin x| + C$.

בדיקה לפי `def_antiderivative`: $\left(\ln|\sin x|\right)' = \frac{\cos x}{\sin x} = \cot x$. $\blacksquare$
