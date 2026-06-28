---
id: prf_inverse_proportion
claim_id: def_inverse_proportion
method: informal
status: reviewed
dependencies:
- def_division
- ax_multiplicative_inverse
- ax_multiplication_associativity
- ax_multiplication_commutativity
is_canonical: true
date_added: '2026-06-28T20:34:16.493056Z'
schema_version: 1
---

**שקילות שתי הצורות $y = \frac{k}{x}$ ו-$x \cdot y = k$:**

מ-`def_division` נזכיר ש-$\frac{k}{x} = k \cdot x^{-1}$ (כאשר $x \neq 0$ ולכן $x^{-1}$ קיים לפי `ax_multiplicative_inverse`).

- אם $y = \frac{k}{x} = k \cdot x^{-1}$, אז כפל ב-$x$:
$$x \cdot y = x \cdot (k \cdot x^{-1}) = k \cdot (x \cdot x^{-1}) = k \cdot 1 = k,$$
כאשר השתמשנו ב-`ax_multiplication_commutativity` ו-`ax_multiplication_associativity` כדי לסדר מחדש, ובהגדרת ההופכי $x \cdot x^{-1} = 1$.
- בכיוון ההפוך: אם $x \cdot y = k$ ו-$x \neq 0$, כפל ב-$x^{-1}$ נותן $y = k \cdot x^{-1} = \frac{k}{x}$.

**תכונת ההקטנה היחסית:** נניח ש-$x$ עובר ל-$x' = \lambda \cdot x$ עם $\lambda \neq 0$. אזי הערך החדש של $y$ הוא:
$$y' = \frac{k}{x'} = \frac{k}{\lambda \cdot x} = \frac{1}{\lambda} \cdot \frac{k}{x} = \frac{y}{\lambda}.$$
כלומר, גידול ב-$x$ פי $\lambda$ גורר הקטנת $y$ פי $\lambda$ — זוהי המהות של "יחס הפוך".

**הניגוד עם פרופורציה ישירה:**
- בפרופורציה ישירה, היחס $\frac{y}{x}$ קבוע ("כמה $y$ מקבלים על כל יחידת $x$").
- בפרופורציה הפוכה, המכפלה $x \cdot y$ קבועה ("כמה $y$ ביחד עם כמה $x$ נותנים סך-קבוע").

שני המקרים שונים מהותית: בפרופורציה ישירה, הגרף בקואורדינטות הוא ישר דרך הראשית; בפרופורציה הפוכה, הגרף הוא היפרבולה $y = \frac{k}{x}$ עם אסימפטוטות צירי המערכת.

**דוגמה אינטואיטיבית:** מספר העובדים $x$ והזמן $y$ לסיום עבודה קבועה הם בפרופורציה הפוכה — הכפלת מספר העובדים מקצרת את הזמן בחצי (בהנחות פשטניות), כי המכפלה (סך שעות-עבודה) קבועה.

**הדרישה $k \neq 0$:** אם $k = 0$ אז $y \equiv 0$ עבור כל $x \neq 0$, וזה מקרה מנוון. $\blacksquare$
