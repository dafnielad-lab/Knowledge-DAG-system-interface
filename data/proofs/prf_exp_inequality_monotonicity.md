---
id: prf_exp_inequality_monotonicity
claim_id: thm_exp_inequality_monotonicity
method: informal
status: reviewed
dependencies:
- def_exponential_function
- thm_exp_increasing
- thm_exp_decreasing
- def_increasing_function
- def_decreasing_function
is_canonical: true
date_added: '2026-06-28T15:49:27.915213Z'
schema_version: 1
---

ההוכחה נובעת ישירות מהמונוטוניות של הפונקציה המעריכית $f(x) = a^x$ (def_exponential_function).

**מקרה 1: $a > 1$.** לפי thm_exp_increasing, $f(x) = a^x$ עולה ממש על כל $\mathbb{R}$. לפי הגדרת פונקציה עולה ממש (def_increasing_function), $x < y \Rightarrow f(x) < f(y)$, כלומר $x < y \Rightarrow a^x < a^y$.

לכיוון ההפוך: נניח $a^x < a^y$. נראה $x < y$ בדרך השלילה. אם $x = y$ אז $a^x = a^y$ — סתירה. אם $x > y$, אז מהיות $f$ עולה ממש $a^x > a^y$ — סתירה. נשאר רק $x < y$.

**מקרה 2: $0 < a < 1$.** לפי thm_exp_decreasing, $f(x) = a^x$ יורדת ממש על כל $\mathbb{R}$. לפי הגדרת פונקציה יורדת ממש (def_decreasing_function), $x > y \Rightarrow f(x) < f(y)$, כלומר $x > y \Rightarrow a^x < a^y$.

לכיוון ההפוך: נניח $a^x < a^y$. בדרך השלילה: אם $x = y$ אז $a^x = a^y$ — סתירה. אם $x < y$, אז מהיות $f$ יורדת ממש $a^x > a^y$ — סתירה. נשאר רק $x > y$.

המסקנה: כיוון אי-השוויון בין $x$ ל-$y$ נשמר כאשר $a > 1$ ומתהפך כאשר $0 < a < 1$. $\blacksquare$
