---
id: prf_linear_inequality_solution
claim_id: thm_linear_inequality_solution
method: informal
status: reviewed
dependencies:
- def_linear_inequality
- ax_addition_preserves_order
- ax_positive_multiplication_preserves_order
- thm_negative_multiplication_flips_inequality
- ax_additive_inverse
- ax_additive_identity
- ax_multiplicative_inverse
- ax_multiplicative_identity
is_canonical: true
date_added: '2026-06-28T15:49:27.800694Z'
schema_version: 1
---

נתון האי-שוויון $a \cdot x + b < c$ (לפי def_linear_inequality) עם $a \neq 0$.

**שלב 1 — בידוד $a \cdot x$:** נוסיף $-b$ לשני האגפים. לפי ax_addition_preserves_order, הוספת קבוע לשני אגפי אי-שוויון שומרת על כיוונו, ולכן:
$$a \cdot x + b + (-b) < c + (-b).$$
לפי ax_additive_inverse ו-ax_additive_identity, $b + (-b) = 0$ ולכן האגף השמאלי שווה ל-$a \cdot x$. נקבל:
$$a \cdot x < c - b.$$

**שלב 2 — מקרה $a > 0$:** נכפול את שני האגפים ב-$\frac{1}{a}$. מ-$a > 0$ נובע ש-$\frac{1}{a} > 0$ (לפי ax_multiplicative_inverse, ההופכי של חיובי הוא חיובי). לפי ax_positive_multiplication_preserves_order, כפל שני אגפים בחיובי שומר על כיוון אי-השוויון:
$$a \cdot x \cdot \frac{1}{a} < (c - b) \cdot \frac{1}{a}.$$
לפי ax_multiplicative_inverse ו-ax_multiplicative_identity, $a \cdot \frac{1}{a} = 1$ ולכן $a \cdot x \cdot \frac{1}{a} = x$. נקבל:
$$x < \frac{c - b}{a}.$$

**שלב 3 — מקרה $a < 0$:** נכפול שוב את שני האגפים ב-$\frac{1}{a}$, אך כעת $\frac{1}{a} < 0$ (הופכי של שלילי הוא שלילי). לפי thm_negative_multiplication_flips_inequality, כפל בשלילי הופך את כיוון האי-שוויון:
$$a \cdot x \cdot \frac{1}{a} > (c - b) \cdot \frac{1}{a},$$
כלומר $x > \frac{c - b}{a}$.

שני המקרים מכסים את כל האפשרויות שכן $a \neq 0$. $\blacksquare$
