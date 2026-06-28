---
id: prf_absolute_value_equation
claim_id: thm_absolute_value_equation
method: informal
status: reviewed
dependencies:
- def_absolute_value
- thm_double_negation
- ax_order_trichotomy
is_canonical: true
date_added: '2026-06-28T15:49:27.790703Z'
schema_version: 1
---

ההוכחה היא בשני כיוונים.

**כיוון 1 ($\Leftarrow$):** נניח $a = c$ או $a = -c$.

אם $a = c$: כיוון ש-$c \geq 0$, מתקיים $a \geq 0$, ולפי **def_absolute_value** (מקרה אי-שלילי) $|a| = a = c$.

אם $a = -c$: יש שני תת-מקרים. אם $c = 0$ אז $a = 0$ והוכחה כמו לעיל ($|a| = 0 = c$). אם $c > 0$ אז $-c < 0$ ולכן $a < 0$, ולפי **def_absolute_value** (מקרה שלילי) $|a| = -a = -(-c)$. לפי **thm_double_negation** $-(-c) = c$, ולכן $|a| = c$.

בשני התת-מקרים קיבלנו $|a| = c$, כנדרש.

**כיוון 2 ($\Rightarrow$):** נניח $|a| = c$. לפי **ax_order_trichotomy** מתקיים בדיוק אחד משלושה: $a > 0$, $a = 0$, $a < 0$.

- אם $a > 0$: לפי **def_absolute_value** $|a| = a$, ולכן $a = c$.

- אם $a = 0$: לפי **def_absolute_value** $|a| = 0$, ולכן $c = 0$. במקרה זה $a = 0 = c = -c$, כך ש-$a = c$ (וגם $a = -c$).

- אם $a < 0$: לפי **def_absolute_value** $|a| = -a$, ולכן $-a = c$. נוסיף $a$ לשני האגפים ונקבל $0 = c + a$, כלומר $a = -c$.

בכל אחד מהמקרים $a = c$ או $a = -c$, כנדרש. $\blacksquare$
