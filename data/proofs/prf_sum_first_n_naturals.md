---
id: prf_sum_first_n_naturals
claim_id: thm_sum_first_n_naturals
method: informal
status: reviewed
dependencies:
- ax_principle_of_mathematical_induction
- ax_addition_associativity
- ax_addition_commutativity
- ax_distributive_law
is_canonical: true
date_added: '2026-06-28T21:06:29.480679Z'
schema_version: 1
---

נסמן $S(n) = 1 + 2 + \cdots + n$ ונוכיח באינדוקציה (לפי האקסיומה ax_principle_of_mathematical_induction) שעבור כל $n \geq 1$ מתקיים $S(n) = \frac{n(n+1)}{2}$.

**בסיס $n = 1$:** $S(1) = 1$ ו-$\frac{1 \cdot 2}{2} = 1$, ולכן הטענה תקפה.

**צעד:** נניח $S(n) = \frac{n(n+1)}{2}$ (הנחת אינדוקציה) ונראה $S(n+1) = \frac{(n+1)(n+2)}{2}$. מהגדרת הסכום ומ-ax_addition_associativity ו-ax_addition_commutativity:
$$S(n+1) = S(n) + (n+1) = \frac{n(n+1)}{2} + (n+1).$$
נוציא גורם משותף $(n+1)$ באמצעות ax_distributive_law:
$$\frac{n(n+1)}{2} + (n+1) = (n+1)\left(\frac{n}{2} + 1\right) = (n+1) \cdot \frac{n + 2}{2} = \frac{(n+1)(n+2)}{2}.$$
זה משלים את הצעד. לפי ax_principle_of_mathematical_induction, הזהות תקפה לכל $n \geq 1$. $\blacksquare$
