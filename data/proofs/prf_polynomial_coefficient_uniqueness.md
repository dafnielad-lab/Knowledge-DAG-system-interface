---
id: prf_polynomial_coefficient_uniqueness
claim_id: thm_polynomial_coefficient_uniqueness
method: informal
status: reviewed
dependencies:
- def_polynomial
- def_polynomial_degree
- thm_factor_theorem
is_canonical: true
date_added: '2026-06-28T15:07:55.470549Z'
schema_version: 1
---

נגדיר את פולינום ההפרש
$$h(x) = p(x) - q(x) = (a_n - b_n) x^n + (a_{n-1} - b_{n-1}) x^{n-1} + \cdots + (a_1 - b_1) x + (a_0 - b_0).$$
לפי [def_polynomial], $h(x)$ הוא אכן פולינום (סכום של שני פולינומים בעלי אותה צורה), שמקדמיו הם $c_i = a_i - b_i$.

מן ההנחה $p(x) = q(x)$ לכל $x \in \mathbb{R}$ נובע ש-$h(x) = 0$ לכל $x \in \mathbb{R}$. בפרט, לכל $\alpha \in \mathbb{R}$ מתקיים $h(\alpha) = 0$, כלומר כל ממשי הוא שורש של $h$.

נניח בשלילה ש-$h$ אינו פולינום האפס. אזי, על-פי [def_polynomial_degree], קיימת לו דרגה $d \geq 0$, שכן יש לפחות מקדם אחד $c_k \neq 0$, ונבחר את $d$ הגדול ביותר כך ש-$c_d \neq 0$.

נראה באינדוקציה על $d$ שלפולינום מדרגה $d$ יש לכל היותר $d$ שורשים שונים. הבסיס: עבור $d = 0$, $h(x) = c_0 \neq 0$ קבוע, ואין לו שורשים כלל ($0 \leq 0$). צעד: יהי $h$ מדרגה $d \geq 1$. אם אין לו שורשים, סיימנו. אחרת, יהי $\alpha$ שורש שלו. לפי [thm_factor_theorem], $(x - \alpha)$ מחלק את $h$, כלומר $h(x) = (x - \alpha) \cdot g(x)$ עבור פולינום $g$ מדרגה $d - 1$. לפי הנחת האינדוקציה ל-$g$ יש לכל היותר $d - 1$ שורשים שונים, ולכן ל-$h$ יש לכל היותר $d$ שורשים שונים (השורש $\alpha$ ושורשי $g$).

אך הראינו לעיל שלכל $\alpha \in \mathbb{R}$ מתקיים $h(\alpha) = 0$, כלומר ל-$h$ אינסוף שורשים — סתירה לכך שיש לו לכל היותר $d$ שורשים סופיים.

מן הסתירה נובע ש-$h$ הוא פולינום האפס, כלומר $c_i = a_i - b_i = 0$ לכל $i$. לכן $a_i = b_i$ לכל $0 \leq i \leq n$, כנדרש. $\blacksquare$
