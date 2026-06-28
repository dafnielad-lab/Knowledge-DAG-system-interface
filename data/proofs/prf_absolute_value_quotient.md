---
id: prf_absolute_value_quotient
claim_id: thm_absolute_value_quotient
method: informal
status: reviewed
dependencies:
- def_absolute_value
- thm_absolute_value_of_product
- thm_absolute_value_nonnegative
- thm_absolute_value_zero_iff
- ax_multiplicative_inverse
is_canonical: true
date_added: '2026-06-28T20:34:16.451602Z'
schema_version: 1
---

נסמן $q = \dfrac{a}{b} = a \cdot b^{-1}$, כך ש-$a = q \cdot b$.

**שלב 1 — שימוש בכפליות הערך המוחלט.** לפי `thm_absolute_value_of_product`,

$$|a| = |q \cdot b| = |q| \cdot |b|.$$

**שלב 2 — חלוקה ב-$|b|$.** מ-$b \neq 0$ נובע לפי `thm_absolute_value_zero_iff` (היפוך: ערך מוחלט אפס אם ורק אם המספר אפס) ש-$|b| \neq 0$, ולפי `thm_absolute_value_nonnegative` ש-$|b| > 0$. לכן ההפכי $|b|^{-1}$ קיים לפי `ax_multiplicative_inverse`, ונכפול את שני האגפים בו:

$$|q| = \frac{|a|}{|b|}.$$

ומכיוון ש-$q = \dfrac{a}{b}$, קיבלנו $\left|\dfrac{a}{b}\right| = \dfrac{|a|}{|b|}$ כנדרש (לפי `def_absolute_value` הביטוי בצד ימין מוגדר היטב). $\blacksquare$
