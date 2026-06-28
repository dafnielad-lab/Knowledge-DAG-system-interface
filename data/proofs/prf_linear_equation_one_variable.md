---
id: prf_linear_equation_one_variable
claim_id: def_linear_equation_one_variable
method: informal
status: reviewed
dependencies:
- def_natural_power
- thm_linear_equation_solution
is_canonical: true
date_added: '2026-06-28T20:34:16.484038Z'
schema_version: 1
---

**הערה על המבנה:** משוואה לינארית מאופיינת בכך שהמשתנה $x$ מופיע רק בחזקה ראשונה — אין $x^2$, אין $\sqrt{x}$, אין $\frac{1}{x}$ וכדומה. הדרישה $a \neq 0$ הכרחית: אם $a = 0$ אזי המשוואה מצטמצמת ל-$b = 0$, שאינה משוואה במשתנה $x$ אלא שוויון מספרי בלבד (תמיד נכון אם $b = 0$, ותמיד שקרי אחרת).

**הצדקת השקילות בין הצורות:** הצורה $a \cdot x + b = c$ ניתנת להבאה לצורה הסטנדרטית $a \cdot x + b' = 0$ על ידי הצבת $b' = b - c$ (אקסיומת חיבור איבר נגדי לשני האגפים). לכן שתי הצורות מתארות את אותה משפחת משוואות.

**קיום ויחידות הפתרון:** מ-`thm_linear_equation_solution` (פתרון משוואה לינארית) נובע שלמשוואה $a \cdot x + b = 0$ עם $a \neq 0$ קיים פתרון יחיד $x = -\frac{b}{a}$. זה מבסס שההגדרה אינה ריקה ושהפתרון מוגדר היטב.

**הקשר לחזקה ראשונה:** הביטוי $a \cdot x = a \cdot x^1$ הוא המקרה הפשוט ביותר של חזקה טבעית של $x$ — ראו `def_natural_power`. זוהי הסיבה לכינוי "משוואה ממעלה ראשונה". $\blacksquare$
