---
id: prf_cramer_rule
claim_id: thm_cramer_rule
method: informal
status: reviewed
dependencies:
- def_determinant_2x2
- thm_determinant_product
- def_invertible_matrix
is_canonical: true
date_added: '2026-06-27T17:22:39.263705Z'
schema_version: 1
---

$A \vec{x} = \vec{b} \Rightarrow \vec{x} = A^{-1} \vec{b}$. הרכיב ה-$i$ של $A^{-1} \vec{b}$ הוא $\frac{1}{\det A}$ כפול הקופקטור של עמודה $i$, שווה ערך ל-$\frac{\det A_i}{\det A}$ (לפי פיתוח לפי עמודה $i$). $\blacksquare$
