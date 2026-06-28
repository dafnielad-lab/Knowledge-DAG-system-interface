---
id: prf_integer_power
claim_id: def_integer_power
method: informal
status: reviewed
dependencies:
- def_natural_power
- ax_multiplicative_inverse
- thm_multiplicative_inverse_uniqueness
is_canonical: true
date_added: '2026-06-28T15:49:27.758970Z'
schema_version: 1
---

מטרת ה'הוכחה' כאן היא לוודא שההגדרה היא **מוגדרת היטב** (well-defined) ועקבית עם ההגדרה הקודמת של חזקה טבעית.

**עקביות עם המקרה $n \geq 0$:** עבור $n \in \mathbb{N}$ מתקיים $|n| = n$ וההגדרה מתלכדת עם הגדרת החזקה הטבעית [def_natural_power] באמצעות הרקורסיה $a^0 = 1$ ו-$a^{n+1} = a^n \cdot a$. אין שום סתירה במקרה $n = 0$ כי $0 \geq 0$.

**הגדרה היטב במקרה $n < 0$:** נניח $n < 0$ ו-$a \neq 0$. אז $|n| \in \mathbb{N}$ ו-$|n| \geq 1$, ולכן $a^{|n|}$ הוא ביטוי מוגדר היטב כחזקה טבעית [def_natural_power]. נותר להראות ש-$a^{|n|} \neq 0$ כדי שהביטוי $\dfrac{1}{a^{|n|}}$ יהיה מוגדר היטב (כלומר, שקיים הפכי לכפל).

**טענה: אם $a \neq 0$ אז $a^k \neq 0$ לכל $k \in \mathbb{N}$.** באינדוקציה על $k$. בסיס: $a^0 = 1 \neq 0$. צעד: אם $a^k \neq 0$, אז $a^{k+1} = a^k \cdot a$. אילו היה $a^k \cdot a = 0$, אז מתכונת אי-קיום מחלקי אפס בשדה היה נובע ש-$a^k = 0$ או $a = 0$, בסתירה להנחות. לכן $a^{k+1} \neq 0$.

ממילא $a^{|n|} \neq 0$, ועל פי האקסיומה של ההפכי הכפלי [ax_multiplicative_inverse] קיים $(a^{|n|})^{-1}$, וההפכי הוא יחיד [thm_multiplicative_inverse_uniqueness]. הביטוי $\dfrac{1}{a^{|n|}}$ מוגדר באופן יחיד כאותו הפכי.

ההגדרה אכן מרחיבה את החזקה הטבעית למעריך שלם, באופן עקבי וחד-משמעי. $\blacksquare$
