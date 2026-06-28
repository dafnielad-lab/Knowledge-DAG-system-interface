---
id: prf_exp_equation_solution
claim_id: thm_exp_equation_solution
method: informal
status: reviewed
dependencies:
- def_exponential_function
- def_logarithm
- thm_exp_increasing
- thm_exp_decreasing
- thm_log_inverse_of_exp
is_canonical: true
date_added: '2026-06-28T15:49:27.912202Z'
schema_version: 1
---

נראה תחילה קיום ויחידות.

**קיום:** נציב $x = \log_a b$ במשוואה. לפי משפט "לוגריתם כהפוכה למעריכית" (thm_log_inverse_of_exp), מתקיים $a^{\log_a b} = b$ (זהו בדיוק הכיוון השני של הזהות, החל כאן עבור הבסיס $a$ והארגומנט $b > 0$). לכן $x = \log_a b$ הוא פתרון של המשוואה $a^x = b$.

**יחידות:** הפונקציה $f(x) = a^x$ (def_exponential_function) היא חד-חד-ערכית. אכן, אם $a > 1$ אז לפי thm_exp_increasing $f$ עולה ממש, ואם $0 < a < 1$ אז לפי thm_exp_decreasing $f$ יורדת ממש. במקרה $a = 1$ נשללה הנחה זו בתנאי המשפט. בשני המקרים הנותרים $f$ מונוטונית ממש, ולכן חד-חד-ערכית: אם $x_1 \neq x_2$ אז $a^{x_1} \neq a^{x_2}$. מכאן שאם $a^{x_1} = b = a^{x_2}$, בהכרח $x_1 = x_2$.

**הסקה:** קיים פתרון יחיד, והוא $x = \log_a b$. שים לב שהתנאי $b > 0$ הכרחי כי לפי def_exponential_function הטווח של $a^x$ הוא $(0, \infty)$, ולכן אם $b \leq 0$ אין פתרון כלל. ההגדרה $\log_a b$ עצמה (def_logarithm) דורשת $b > 0$, ולכן הביטוי $\log_a b$ מוגדר היטב בדיוק כאשר הפתרון קיים. $\blacksquare$
