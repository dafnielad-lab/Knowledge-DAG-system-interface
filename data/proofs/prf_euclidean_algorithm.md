---
id: prf_euclidean_algorithm
claim_id: thm_euclidean_algorithm
method: informal
status: reviewed
dependencies:
- def_gcd
- thm_division_algorithm
- thm_divisibility_linear_combinations
is_canonical: true
date_added: '2026-06-27T16:34:26.423690Z'
schema_version: 1
---

מאלגוריתם החילוק $a = b q + r$, כל מחלק משותף של $a$ ו-$b$ מחלק גם את $r = a - b q$. ובאותו אופן כל מחלק משותף של $b$ ו-$r$ מחלק את $a$.

לכן קבוצת המחלקים המשותפים של $(a, b)$ זהה לקבוצת המחלקים המשותפים של $(b, r)$, ובפרט ה-GCD שווה. $\blacksquare$
