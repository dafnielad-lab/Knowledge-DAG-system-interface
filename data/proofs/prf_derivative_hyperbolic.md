---
id: prf_derivative_hyperbolic
claim_id: thm_derivative_hyperbolic
method: informal
status: reviewed
dependencies:
- def_hyperbolic_sin_cos
- def_hyperbolic_tan
- thm_derivative_exp
- thm_derivative_chain
- thm_derivative_sum
- thm_derivative_constant_multiple
- thm_derivative_quotient
is_canonical: true
date_added: '2026-06-28T20:34:16.576718Z'
schema_version: 1
---

**נגזרת $\sinh x$:** לפי `def_hyperbolic_sin_cos`, $\sinh x = \frac{e^x - e^{-x}}{2}$. בעזרת `thm_derivative_exp` ($(e^x)' = e^x$), `thm_derivative_chain` ($(e^{-x})' = -e^{-x}$), `thm_derivative_sum` ו-`thm_derivative_constant_multiple`:

$$(\sinh x)' = \frac{1}{2}\left( e^x - (-e^{-x}) \right) = \frac{e^x + e^{-x}}{2} = \cosh x.$$

**נגזרת $\cosh x$:** $\cosh x = \frac{e^x + e^{-x}}{2}$, ובאותו אופן:

$$(\cosh x)' = \frac{1}{2}\left( e^x + (-e^{-x}) \right) = \frac{e^x - e^{-x}}{2} = \sinh x.$$

**נגזרת $\tanh x$:** לפי `def_hyperbolic_tan`, $\tanh x = \frac{\sinh x}{\cosh x}$. בעזרת `thm_derivative_quotient`:

$$(\tanh x)' = \frac{(\sinh x)' \cosh x - \sinh x \cdot (\cosh x)'}{\cosh^2 x} = \frac{\cosh^2 x - \sinh^2 x}{\cosh^2 x}.$$

מתוך ההגדרות:

$$\cosh^2 x - \sinh^2 x = \frac{(e^x+e^{-x})^2 - (e^x-e^{-x})^2}{4} = \frac{4 \cdot e^x \cdot e^{-x}}{4} = 1.$$

לכן $(\tanh x)' = \frac{1}{\cosh^2 x}$. $\blacksquare$
