---
id: prf_absolute_value_inequality_less
claim_id: thm_absolute_value_inequality_less
method: informal
status: reviewed
dependencies:
- def_absolute_value
- ax_order_trichotomy
- thm_negative_multiplication_flips_inequality
- thm_transitivity_of_strict_order
is_canonical: true
date_added: '2026-06-28T15:49:27.793204Z'
schema_version: 1
---

**כיוון 1 ($\Rightarrow$):** נניח $|a| < c$. לפי **ax_order_trichotomy** נחלק לשלושה מקרים:

- אם $a \geq 0$: לפי **def_absolute_value** $|a| = a$, ולכן $a < c$. בנוסף, $-c < 0 \leq a$ (שכן $c > 0$ נתון, ולכן $-c < 0$, ולפי **thm_transitivity_of_strict_order** אם $-c < 0$ ו-$0 \leq a$ אז $-c < a$). קיבלנו $-c < a < c$.

- אם $a < 0$: לפי **def_absolute_value** $|a| = -a$, ולכן $-a < c$. לפי **thm_negative_multiplication_flips_inequality** הכפלה ב-$-1$ הופכת את כיוון אי-השוויון, ומקבלים $a > -c$, כלומר $-c < a$. בנוסף, מ-$a < 0 < c$ ולפי **thm_transitivity_of_strict_order** נקבל $a < c$. שוב $-c < a < c$.

**כיוון 2 ($\Leftarrow$):** נניח $-c < a < c$. שוב נחלק לפי **ax_order_trichotomy**:

- אם $a \geq 0$: $|a| = a < c$ לפי **def_absolute_value**, כנדרש.

- אם $a < 0$: לפי **def_absolute_value** $|a| = -a$. מההנחה $-c < a$, נכפיל ב-$-1$ ולפי **thm_negative_multiplication_flips_inequality** נקבל $c > -a$, כלומר $-a < c$. לכן $|a| = -a < c$, כנדרש.

בשני הכיוונים קיבלנו את הטענה. $\blacksquare$
