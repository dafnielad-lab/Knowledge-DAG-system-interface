---
id: prf_derivative_log_natural
claim_id: thm_derivative_log_natural
method: informal
status: reviewed
dependencies:
- thm_derivative_inverse_function
- thm_derivative_exp
- def_logarithm
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

$\ln x$ היא הפונקציה ההפוכה של $e^y$. נגזרת ההפוכה: אם $y = \ln x$ אז $x = e^y$, ולכן $\frac{dy}{dx} = \frac{1}{dx/dy} = \frac{1}{e^y} = \frac{1}{x}$. $\blacksquare$
