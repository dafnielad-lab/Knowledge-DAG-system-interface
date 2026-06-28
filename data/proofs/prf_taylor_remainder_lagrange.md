---
id: prf_taylor_remainder_lagrange
claim_id: thm_taylor_remainder_lagrange
method: informal
status: reviewed
dependencies:
- thm_cauchy_mean_value
- def_higher_order_derivative
- def_proof_by_induction
- thm_derivative_power
is_canonical: true
date_added: '2026-06-28T15:07:55.561550Z'
schema_version: 1
---

**הוכחה.** נגדיר $R_n(x) = f(x) - P_n(x)$, כאשר $P_n$ פולינום טיילור מסדר $n$ של $f$ סביב $a$. כמו כן נגדיר $g(x) = (x-a)^{n+1}$.

**עובדות מקדימות.** לפי הגדרת $P_n$ מתקיים $R_n^{(k)}(a) = 0$ עבור $k = 0, 1, \ldots, n$, וכן $R_n^{(n+1)} = f^{(n+1)}$ (כי הנגזרת $(n+1)$-ית של פולינום ממעלה $n$ היא אפס). גזירה חוזרת של $g$ נותנת $g^{(k)}(t) = \frac{(n+1)!}{(n+1-k)!}(t-a)^{n+1-k}$ עבור $k \le n+1$. בפרט $g^{(k)}(a) = 0$ עבור $k \le n$, $g^{(n+1)}(t) \equiv (n+1)!$, ולכל $k \le n$ ו-$t \neq a$ מתקיים $g^{(k)}(t) \neq 0$.

**טענת אינדוקציה.** בהינתן $x \neq a$, נוכיח באינדוקציה על $k = 0, 1, \ldots, n$ כי קיימת נקודה $\xi_k$ בין $a$ ל-$x$ עם
$$\frac{R_n(x)}{g(x)} = \frac{R_n^{(k)}(\xi_k)}{g^{(k)}(\xi_k)}.$$

**בסיס** ($k=0$): טריוויאלי עם $\xi_0 = x$.

**צעד** ($k \Rightarrow k+1$, עבור $k < n+1$): נתון $\xi_k$ בין $a$ ל-$x$. מאחר ש-$R_n^{(k)}(a) = g^{(k)}(a) = 0$ (כאן $k \le n$), הפונקציות $R_n^{(k)}$ ו-$g^{(k)}$ רציפות וגזירות בקטע שבין $a$ ל-$\xi_k$, ו-$g^{(k+1)}$ אינה מתאפסת שם. מהפעלת משפט קושי לערך הממוצע על קטע זה קיים $\xi_{k+1}$ ביניהם (ולכן בין $a$ ל-$x$) עם
$$\frac{R_n^{(k)}(\xi_k)}{g^{(k)}(\xi_k)} = \frac{R_n^{(k)}(\xi_k) - 0}{g^{(k)}(\xi_k) - 0} = \frac{R_n^{(k+1)}(\xi_{k+1})}{g^{(k+1)}(\xi_{k+1})}.$$

**סיום.** עבור $k = n+1$ קיבלנו $\xi = \xi_{n+1}$ בין $a$ ל-$x$ עם
$$\frac{R_n(x)}{(x-a)^{n+1}} = \frac{R_n^{(n+1)}(\xi)}{g^{(n+1)}(\xi)} = \frac{f^{(n+1)}(\xi)}{(n+1)!}.$$

הכפלה ב-$(x-a)^{n+1}$ נותנת את הצורה הנדרשת. $\blacksquare$
