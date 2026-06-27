---
id: prf_limit_polynomial_continuous
claim_id: thm_limit_polynomial_continuous
method: informal
status: reviewed
dependencies:
- thm_limit_constant
- thm_limit_identity
- thm_limit_sum
- thm_limit_product
- def_polynomial
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

פולינום הוא סכום סופי של איברים מהצורה $a_k x^k$, שכל אחד הוא מכפלה של קבועים ו-$x$.

לכן ניתן לחשב את הגבול שלו לפי כללי גבול של סכום ומכפלה, החל מהגבולות היסודיים $\lim c = c$ ו-$\lim x = x_0$. כל אחד מהגבולות החלקיים שווה לערך באותה נקודה, ולכן $\lim p(x) = p(x_0)$. $\blacksquare$
