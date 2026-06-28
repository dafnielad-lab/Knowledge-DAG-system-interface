---
id: prf_integral_csc
claim_id: thm_integral_csc
method: informal
status: reviewed
dependencies:
- def_secant_cosecant_cotangent
- thm_integral_substitution
- thm_integral_one_over_x
- def_antiderivative
- thm_derivative_quotient
is_canonical: true
date_added: '2026-06-28T20:34:16.567708Z'
schema_version: 1
---

נכפול ונחלק את האינטגרנד ב-$\csc x + \cot x$:

$$\csc x = \csc x \cdot \frac{\csc x + \cot x}{\csc x + \cot x} = \frac{\csc^2 x + \csc x \cot x}{\csc x + \cot x}.$$

נגדיר $u = \csc x + \cot x$. לפי `def_secant_cosecant_cotangent`, $\csc x = (\sin x)^{-1}$ ו-$\cot x = (\tan x)^{-1}$. בעזרת `thm_derivative_quotient` (או גזירה ישירה) מקבלים $(\csc x)' = -\csc x \cot x$ ו-$(\cot x)' = -\csc^2 x$. לכן:

$$\frac{du}{dx} = -\csc x \cot x - \csc^2 x = -(\csc x \cot x + \csc^2 x),$$

כלומר $-du = (\csc^2 x + \csc x \cot x) \, dx$ — בדיוק המונה.

על פי `thm_integral_substitution`:

$$\int \csc x \, dx = \int \frac{-du}{u} = -\int \frac{1}{u} \, du.$$

לפי `thm_integral_one_over_x` נקבל $-\ln|u| + C = -\ln|\csc x + \cot x| + C$.

שקילות הצורה השנייה: $\frac{1}{\csc x + \cot x} = \frac{\csc x - \cot x}{\csc^2 x - \cot^2 x} = \csc x - \cot x$ (כי $\csc^2 x - \cot^2 x = 1$), ולכן $-\ln|\csc x + \cot x| = \ln|\csc x - \cot x|$.

בדיקה לפי `def_antiderivative`: $\left(-\ln|\csc x + \cot x|\right)' = -\frac{-\csc x \cot x - \csc^2 x}{\csc x + \cot x} = \frac{\csc x(\cot x + \csc x)}{\csc x + \cot x} = \csc x$. $\blacksquare$
