---
id: prf_derivative_exp
claim_id: thm_derivative_exp
method: informal
status: reviewed
dependencies:
- def_derivative_at_point
- thm_exp_addition
- thm_limit_one_plus_inv_n_to_e
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

$(e^x)' = \lim_{h \to 0} \frac{e^{x+h} - e^x}{h} = e^x \cdot \lim_{h \to 0} \frac{e^h - 1}{h}$.

הגבול $\lim_{h \to 0} \frac{e^h - 1}{h} = 1$ הוא תכונה מאפיינת של $e$ (ניתן להוכיח מהגדרת $e$ כגבול).

לכן $(e^x)' = e^x$. $\blacksquare$
