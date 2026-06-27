---
id: prf_arctan_sum_identity
claim_id: thm_arctan_sum_identity
method: informal
status: reviewed
dependencies:
- def_arctan
- thm_tan_addition_formula
is_canonical: true
date_added: '2026-06-27T18:47:27.564532Z'
schema_version: 1
---

עבור $x > 0$: נסמן $\alpha = \arctan x$, $\beta = \arctan(1/x)$. שניהם בקטע $(0, \pi/2)$.

$\tan(\alpha + \beta) = \frac{x + 1/x}{1 - 1} = \frac{x + 1/x}{0}$ — אינסופי. לכן $\alpha + \beta = \pi/2$. עבור $x < 0$ — הסימן הפוך, ומקבלים $-\pi/2$. $\blacksquare$
