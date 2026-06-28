---
id: prf_absolute_value_squared
claim_id: thm_absolute_value_squared
method: informal
status: reviewed
dependencies:
- def_absolute_value
- thm_absolute_value_of_product
- thm_square_nonnegative
- thm_absolute_value_nonnegative
- def_square_root
is_canonical: true
date_added: '2026-06-28T20:34:16.454111Z'
schema_version: 1
---

**שלב 1 — $|a|^2 = a^2$.** לפי `thm_absolute_value_of_product` עם $b = a$ מקבלים

$$|a^2| = |a \cdot a| = |a| \cdot |a| = |a|^2.$$

כעת לפי `thm_square_nonnegative` מתקיים $a^2 \geq 0$, ולכן לפי `def_absolute_value` (ענף $\geq 0$) $|a^2| = a^2$. שילוב שתי השוויונות נותן

$$|a|^2 = |a^2| = a^2.$$

**שלב 2 — $|a| = \sqrt{a^2}$.** לפי `thm_absolute_value_nonnegative` מתקיים $|a| \geq 0$, ובשלב 1 הוכחנו $|a|^2 = a^2$. לפי `def_square_root` השורש הריבועי של מספר אי-שלילי הוא **המספר האי-שלילי היחיד** שריבועו שווה לאותו מספר. לכן

$$|a| = \sqrt{a^2}.$$

$\blacksquare$
