---
id: prf_sum_first_n_cubes
claim_id: thm_sum_first_n_cubes
method: informal
status: reviewed
dependencies:
- ax_principle_of_mathematical_induction
- thm_sum_first_n_naturals
- ax_addition_associativity
- ax_distributive_law
is_canonical: true
date_added: '2026-06-28T21:06:29.486179Z'
schema_version: 1
---

נסמן $C(n) = 1^3 + 2^3 + \cdots + n^3$ ונוכיח באינדוקציה (לפי $ax\_principle\_of\_mathematical\_induction$) שעבור $n \geq 1$ מתקיים $C(n) = \left(\frac{n(n+1)}{2}\right)^2$.

**בסיס $n = 1$:** $C(1) = 1$ ו-$\left(\frac{1 \cdot 2}{2}\right)^2 = 1$. מתקיים.

**צעד:** נניח $C(n) = \left(\frac{n(n+1)}{2}\right)^2 = \frac{n^2(n+1)^2}{4}$. אז:
$$C(n+1) = C(n) + (n+1)^3 = \frac{n^2(n+1)^2}{4} + (n+1)^3.$$
נוציא גורם משותף $(n+1)^2$ באמצעות $ax\_distributive\_law$:
$$= \frac{(n+1)^2 \bigl[n^2 + 4(n+1)\bigr]}{4} = \frac{(n+1)^2 (n^2 + 4n + 4)}{4} = \frac{(n+1)^2 (n+2)^2}{4}.$$
זה שווה ל-$\left(\frac{(n+1)(n+2)}{2}\right)^2$, שזו בדיוק הזהות עבור $n+1$.

**הערה — הקשר ל-$thm\_sum\_first\_n\_naturals$:** אפשר לכתוב את הזהות כ-$C(n) = \bigl(S(n)\bigr)^2$ כאשר $S(n) = 1 + 2 + \cdots + n = \frac{n(n+1)}{2}$ (לפי $thm\_sum\_first\_n\_naturals$), ולכן הטענה היא $\sum_{k=1}^n k^3 = \bigl(\sum_{k=1}^n k\bigr)^2$.

לפי $ax\_principle\_of\_mathematical\_induction$, הזהות תקפה לכל $n \geq 1$. $\blacksquare$
