---
id: prf_increasing_test
claim_id: thm_increasing_test
method: informal
status: reviewed
dependencies:
- thm_mean_value_theorem
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

נניח $f'(x) > 0$ בכל הקטע $I$. לכל $x_1 < x_2$ ב-$I$, לפי משפט הערך הממוצע קיים $c \in (x_1, x_2)$ עם $\frac{f(x_2) - f(x_1)}{x_2 - x_1} = f'(c) > 0$.

לכן $f(x_2) - f(x_1) > 0$, כלומר $f(x_1) < f(x_2)$. $\blacksquare$
