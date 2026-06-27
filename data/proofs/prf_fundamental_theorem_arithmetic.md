---
id: prf_fundamental_theorem_arithmetic
claim_id: thm_fundamental_theorem_arithmetic
method: informal
status: reviewed
dependencies:
- def_prime
- def_divisibility
- thm_division_algorithm
is_canonical: true
date_added: '2026-06-27T15:58:40.082207Z'
schema_version: 1
---

**קיום הפירוק:** באינדוקציה חזקה על $n$. אם $n$ ראשוני, סיימנו. אחרת קיים מחלק $1 < d < n$, ולכן $n = d \cdot (n/d)$ כאשר שני הגורמים קטנים מ-$n$. לפי הנחת האינדוקציה לכל אחד מהם פירוק לראשוניים — נצרף ונקבל פירוק ל-$n$.

**יחידות:** משתמשים בלמת אוקלידס (אם $p \mid ab$ ו-$p$ ראשוני, אז $p \mid a$ או $p \mid b$), ומראים שכל פירוק שונה היה מוביל לסתירה עם הלמה. $\blacksquare$
