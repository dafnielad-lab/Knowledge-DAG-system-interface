---
id: prf_sum_to_product_sin
claim_id: thm_sum_to_product_sin
method: informal
status: reviewed
dependencies:
- thm_sin_addition_formula
- thm_sin_subtraction_formula
is_canonical: true
date_added: '2026-06-27T16:34:26.423690Z'
schema_version: 1
---

נסמן $\alpha = A + B$, $\beta = A - B$ (כך ש-$A = \frac{\alpha+\beta}{2}$, $B = \frac{\alpha-\beta}{2}$).

$\sin(A+B) + \sin(A-B) = (\sin A \cos B + \cos A \sin B) + (\sin A \cos B - \cos A \sin B) = 2 \sin A \cos B$.

כלומר $\sin\alpha + \sin\beta = 2 \sin\frac{\alpha+\beta}{2} \cos\frac{\alpha-\beta}{2}$. $\blacksquare$
