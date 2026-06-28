---
id: prf_log_inequality_monotonicity
claim_id: thm_log_inequality_monotonicity
method: informal
status: reviewed
dependencies:
- def_logarithm
- thm_exp_increasing
- thm_exp_decreasing
- thm_log_inverse_of_exp
- thm_exp_inequality_monotonicity
is_canonical: true
date_added: '2026-06-28T15:49:27.920704Z'
schema_version: 1
---

נסמן $u = \log_a x$ ו-$v = \log_a y$. לפי def_logarithm זה שקול לכך ש-$a^u = x$ ו-$a^v = y$.

**מקרה 1: $a > 1$.**

כיוון $\Rightarrow$: נניח $\log_a x < \log_a y$, כלומר $u < v$. לפי thm_exp_inequality_monotonicity (או ישירות מ-thm_exp_increasing, שלפיו $a^x$ עולה ממש כאשר $a > 1$), מתקיים $a^u < a^v$, כלומר $x < y$.

כיוון $\Leftarrow$: נניח $x < y$, כלומר $a^u < a^v$. שוב לפי thm_exp_inequality_monotonicity (החל את כיוון $\Leftarrow$ של המשפט), מהיות $a > 1$ נובע $u < v$, כלומר $\log_a x < \log_a y$.

**מקרה 2: $0 < a < 1$.**

כיוון $\Rightarrow$: נניח $\log_a x < \log_a y$, כלומר $u < v$. לפי thm_exp_decreasing, $a^x$ יורדת ממש כאשר $0 < a < 1$, ולכן (לפי thm_exp_inequality_monotonicity במקרה השני) $a^u > a^v$, כלומר $x > y$.

כיוון $\Leftarrow$: נניח $x > y$, כלומר $a^u > a^v$. לפי כיוון $\Leftarrow$ של thm_exp_inequality_monotonicity במקרה $0 < a < 1$: אם $a^u > a^v$ אז $u < v$, כלומר $\log_a x < \log_a y$.

**הערה:** העובדה שהשקילויות נכונות (ולא רק כיוון אחד) מסתמכת על כך שהזיווג $x \leftrightarrow u$ הוא חד-חד-ערכי ועל. חד-חד-ערכיות נובעת מ-thm_log_inverse_of_exp, המבטיח שכל $x > 0$ מקבל $u$ יחיד ולהפך.

**מסקנה:** כיוון אי-השוויון נשמר כאשר $a > 1$ ומתהפך כאשר $0 < a < 1$, בדיוק כמו בפונקציה המעריכית. $\blacksquare$
