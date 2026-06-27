---
id: prf_derivative_quotient
claim_id: thm_derivative_quotient
method: informal
status: reviewed
dependencies:
- thm_derivative_product
- thm_derivative_chain
- thm_derivative_power
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

$\frac{f}{g} = f \cdot g^{-1}$. לפי כלל המכפלה והשרשרת:

$\left(\frac{f}{g}\right)' = f' \cdot g^{-1} + f \cdot (g^{-1})' = \frac{f'}{g} + f \cdot \left(-\frac{g'}{g^2}\right) = \frac{f' g - f g'}{g^2}$. $\blacksquare$
