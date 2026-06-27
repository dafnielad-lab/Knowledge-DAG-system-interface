---
id: prf_jensen_inequality
claim_id: thm_jensen_inequality
method: informal
status: reviewed
dependencies:
- def_convex_function
is_canonical: true
date_added: '2026-06-27T18:47:27.564532Z'
schema_version: 1
---

**הוכחה באינדוקציה על $n$.** $n=1$: טריוויאלי. $n=2$: בדיוק הגדרת קמירות.

צעד: נניח עבור $n$, נראה ל-$n+1$. נסמן $\Lambda = \sum_{i=1}^{n} \lambda_i = 1 - \lambda_{n+1}$. אז $\sum \lambda_i x_i = \Lambda \cdot \frac{\sum_{i \leq n} \lambda_i x_i}{\Lambda} + \lambda_{n+1} x_{n+1}$. נשתמש בקמירות (אגף ימין) ובהנחת האינדוקציה. $\blacksquare$
