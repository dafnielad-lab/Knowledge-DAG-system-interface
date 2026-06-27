---
id: prf_cos_addition_formula
claim_id: thm_cos_addition_formula
method: informal
status: reviewed
dependencies:
- def_cos
- def_sin
- def_unit_circle
- thm_law_of_cosines
is_canonical: true
date_added: '2026-06-27T16:13:44.126814Z'
schema_version: 1
---

**גישה גאומטרית:** ניקח שתי נקודות במעגל היחידה — $A = (\cos\alpha, \sin\alpha)$ ו-$B = (\cos\beta, \sin\beta)$.

המרחק בריבוע $|AB|^2 = (\cos\alpha - \cos\beta)^2 + (\sin\alpha - \sin\beta)^2 = 2 - 2(\cos\alpha\cos\beta + \sin\alpha\sin\beta)$.

מצד שני, לפי משפט הקוסינוסים במשולש המכיל את הזווית $\alpha - \beta$: $|AB|^2 = 1 + 1 - 2\cos(\alpha - \beta)$.

השוואה: $\cos(\alpha - \beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta$, ולכן $\cos(\alpha + \beta) = \cos(\alpha - (-\beta)) = \cos\alpha\cos(-\beta) + \sin\alpha\sin(-\beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta$. $\blacksquare$
