---
id: prf_log_equation_to_exponential
claim_id: thm_log_equation_to_exponential
method: informal
status: reviewed
dependencies:
- def_logarithm
- def_exponential_function
- thm_log_inverse_of_exp
- thm_exp_increasing
- thm_exp_decreasing
is_canonical: true
date_added: '2026-06-28T15:49:27.917705Z'
schema_version: 1
---

**קיום:** נציב $x = a^b$ ונבדוק. לפי def_logarithm, $\log_a x = y$ אם ורק אם $a^y = x$. כעת $a^b = a^b$ באופן טריוויאלי, ולכן $\log_a(a^b) = b$ — וזה גם בדיוק הכיוון הראשון של thm_log_inverse_of_exp. לכן $x = a^b$ מקיים את המשוואה $\log_a x = b$.

כמו כן, מהגדרת הפונקציה המעריכית (def_exponential_function), $a^b > 0$ לכל $b \in \mathbb{R}$ (הטווח של $a^x$ הוא $(0, \infty)$). לכן $x = a^b$ הוא ערך מותר (מקיים $x > 0$).

**יחידות:** נניח $x_1, x_2 > 0$ הם שני פתרונות, כלומר $\log_a x_1 = b = \log_a x_2$. מהגדרת הלוגריתם (def_logarithm), $\log_a x_i = b$ אם ורק אם $a^b = x_i$. לכן $x_1 = a^b = x_2$.

ניתן גם להראות זאת מתוך מונוטוניות: לפי thm_exp_increasing (כאשר $a > 1$) או thm_exp_decreasing (כאשר $0 < a < 1$), הפונקציה $a^y$ חד-חד-ערכית, ולכן הפונקציה ההפוכה $\log_a$ מוגדרת היטב כפונקציה חד-ערכית — מה שמבטיח שלמשוואה $\log_a x = b$ יש לכל היותר פתרון אחד.

**הסקה:** הפתרון היחיד הוא $x = a^b$. נציין שתנאי תחום ההגדרה $x > 0$ הכרחי לפי def_logarithm: הלוגריתם מוגדר רק עבור ארגומנט חיובי. $\blacksquare$
