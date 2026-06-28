---
id: prf_cramer_rule
claim_id: thm_cramer_rule
method: informal
status: reviewed
dependencies:
- def_invertible_matrix
- thm_laplace_expansion
- thm_inverse_via_adjugate
is_canonical: true
date_added: '2026-06-28T15:07:55.492549Z'
schema_version: 1
---

$A \vec{x} = \vec{b} \Rightarrow \vec{x} = A^{-1} \vec{b}$. הרכיב ה-$i$ של $A^{-1} \vec{b}$ הוא $\frac{1}{\det A}$ כפול הקופקטור של עמודה $i$, שווה ערך ל-$\frac{\det A_i}{\det A}$ (לפי פיתוח לפי עמודה $i$). $\blacksquare$
