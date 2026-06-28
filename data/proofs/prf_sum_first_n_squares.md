---
id: prf_sum_first_n_squares
claim_id: thm_sum_first_n_squares
method: informal
status: reviewed
dependencies:
- ax_principle_of_mathematical_induction
- ax_addition_associativity
- ax_addition_commutativity
- ax_distributive_law
is_canonical: true
date_added: '2026-06-28T21:06:29.483677Z'
schema_version: 1
---

נסמן $Q(n) = 1^2 + 2^2 + \cdots + n^2$ ונוכיח באינדוקציה (לפי $ax\_principle\_of\_mathematical\_induction$) שעבור $n \geq 1$ מתקיים $Q(n) = \frac{n(n+1)(2n+1)}{6}$.

**בסיס $n = 1$:** $Q(1) = 1$ ו-$\frac{1 \cdot 2 \cdot 3}{6} = 1$. מתקיים.

**צעד:** נניח $Q(n) = \frac{n(n+1)(2n+1)}{6}$. אז:
$$Q(n+1) = Q(n) + (n+1)^2 = \frac{n(n+1)(2n+1)}{6} + (n+1)^2.$$
נוציא גורם משותף $(n+1)$ באמצעות $ax\_distributive\_law$:
$$= \frac{(n+1)\bigl[n(2n+1) + 6(n+1)\bigr]}{6} = \frac{(n+1)(2n^2 + 7n + 6)}{6}.$$
פירוק הריבועית: $2n^2 + 7n + 6 = (n+2)(2n+3)$ (בדיקה ישירה לפי $ax\_distributive\_law$ ו-$ax\_addition\_commutativity$: $(n+2)(2n+3) = 2n^2 + 3n + 4n + 6 = 2n^2 + 7n + 6$). לכן:
$$Q(n+1) = \frac{(n+1)(n+2)(2n+3)}{6} = \frac{(n+1)\bigl((n+1)+1\bigr)\bigl(2(n+1)+1\bigr)}{6},$$
וזו בדיוק הזהות עבור $n+1$. לפי $ax\_principle\_of\_mathematical\_induction$, הזהות תקפה לכל $n \geq 1$. $\blacksquare$
