---
id: prf_absolute_value_inequality_greater
claim_id: thm_absolute_value_inequality_greater
method: informal
status: reviewed
dependencies:
- def_absolute_value
- ax_order_trichotomy
- thm_negative_multiplication_flips_inequality
- thm_transitivity_of_strict_order
is_canonical: true
date_added: '2026-06-28T15:49:27.796195Z'
schema_version: 1
---

**כיוון 1 ($\Rightarrow$):** נניח $|a| > c$. שים לב שמכיוון ש-$c > 0$ ו-$|a| > c$, לפי **thm_transitivity_of_strict_order** מקבלים $|a| > 0$, ובפרט $a \neq 0$ (אחרת היה $|a| = 0$ לפי **def_absolute_value**, בסתירה).

לפי **ax_order_trichotomy** נחלק לשני מקרים:

- אם $a > 0$: לפי **def_absolute_value** $|a| = a$, ולכן $a > c$.

- אם $a < 0$: לפי **def_absolute_value** $|a| = -a$, ולכן $-a > c$. נכפיל את שני האגפים ב-$-1$ ולפי **thm_negative_multiplication_flips_inequality** כיוון אי-השוויון מתהפך: $a < -c$.

בשני המקרים, $a > c$ או $a < -c$, כנדרש.

**כיוון 2 ($\Leftarrow$):** נניח $a > c$ או $a < -c$.

- אם $a > c$: מכיוון ש-$c > 0$ ו-$a > c$, לפי **thm_transitivity_of_strict_order** $a > 0$. לפי **def_absolute_value** $|a| = a > c$, כנדרש.

- אם $a < -c$: מכיוון ש-$c > 0$ מתקיים $-c < 0$, ולפי **thm_transitivity_of_strict_order** מ-$a < -c < 0$ מקבלים $a < 0$. לפי **def_absolute_value** $|a| = -a$. נכפיל את ההנחה $a < -c$ ב-$-1$ ולפי **thm_negative_multiplication_flips_inequality** נקבל $-a > c$, כלומר $|a| > c$, כנדרש.

בשני הכיוונים הראינו את שקילות הטענות. $\blacksquare$
