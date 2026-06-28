---
id: prf_power_of_quotient
claim_id: thm_power_of_quotient
method: informal
status: reviewed
dependencies:
- def_division
- def_natural_power
- thm_power_of_product
- ax_multiplicative_inverse
- ax_multiplication_associativity
- ax_multiplication_commutativity
- ax_multiplicative_identity
is_canonical: true
date_added: '2026-06-28T21:06:29.451183Z'
schema_version: 1
---

ההוכחה משתמשת בהגדרת החילוק במישור הממשי (לא בהגדרת השבר המוגבלת לשלמים), כך שהטענה תקפה לכל $a, b \in \mathbb{R}$ עם $b \neq 0$.

לפי הגדרת חילוק (def_division), $\dfrac{a}{b} = a \cdot b^{-1}$, כאשר $b^{-1}$ קיים מתוקף איבר הפכי לכפל (ax_multiplicative_inverse), שכן $b \neq 0$. שני המספרים $a$ ו-$b^{-1}$ הם ממשיים, ולכן $a \cdot b^{-1} \in \mathbb{R}$.

כעת נחשב את החזקה לפי thm_power_of_product (חזקה של מכפלה), המתקיימת לכל זוג מספרים ממשיים: עם $u = a$ ו-$v = b^{-1}$,
$\left(\dfrac{a}{b}\right)^n = (a \cdot b^{-1})^n = a^n \cdot (b^{-1})^n$.

נותר להראות ש-$(b^{-1})^n = (b^n)^{-1}$. נוכיח זאת באינדוקציה על $n$ (לפי הגדרת חזקה טבעית, def_natural_power):

**בסיס $n = 0$:** $(b^{-1})^0 = 1$ ו-$(b^0)^{-1} = 1^{-1} = 1$ (לפי def_natural_power ו-ax_multiplicative_identity). שוויון מתקיים.

**צעד אינדוקציה:** נניח $(b^{-1})^n = (b^n)^{-1}$. אז:
$(b^{-1})^{n+1} = (b^{-1})^n \cdot b^{-1} = (b^n)^{-1} \cdot b^{-1}$ (לפי הנחת האינדוקציה ו-def_natural_power).

נשים לב ש-$(b^n \cdot b) \cdot ((b^n)^{-1} \cdot b^{-1}) = (b^n \cdot (b^n)^{-1}) \cdot (b \cdot b^{-1}) = 1 \cdot 1 = 1$ (לפי קומוטטיביות ואסוציאטיביות הכפל, ax_multiplication_commutativity, ax_multiplication_associativity, ולפי ax_multiplicative_inverse). מכאן ש-$(b^n)^{-1} \cdot b^{-1}$ הוא ההפכי הכפלי של $b^n \cdot b = b^{n+1}$ (לפי def_natural_power), כלומר $(b^{-1})^{n+1} = (b^{n+1})^{-1}$ — נדרש שיהיה $b^{n+1} \neq 0$, וזה מתקיים כי $b \neq 0$ (אינדוקטיבית, מכפלת מספרים שונים מאפס שונה מאפס; הוכחה זו מוכלת במשתמע כשמשתמשים ב-$b^{-1}$ בשלב הקודם).

מצרפים:
$\left(\dfrac{a}{b}\right)^n = a^n \cdot (b^{-1})^n = a^n \cdot (b^n)^{-1} = \dfrac{a^n}{b^n}$
(השוויון האחרון לפי def_division). $\blacksquare$
