---
id: prf_expected_value_of_function
claim_id: thm_expected_value_of_function
method: informal
status: reviewed
dependencies:
- def_expected_value
- def_discrete_random_variable
- def_continuous_random_variable
is_canonical: true
date_added: '2026-06-27T17:23:25.498539Z'
schema_version: 1
---

**מקרה בדיד.** $g(X)$ הוא משתנה מקרי חדש. ערכיו האפשריים: $\{g(x_i)\}$ עם הסתברויות $P(X = x_i)$. לפי הגדרת תוחלת: $E[g(X)] = \sum_i g(x_i) P(X = x_i)$ (במידה שאין שני $x_i$ שונים שמעבירים לאותו ערך — אז יש לאחד הסתברויות, אבל הסכום נשאר אותו דבר).

**מקרה רציף.** באופן דומה אבל עם אינטגרל וצפיפות: $E[g(X)] = \int g(x) f(x) dx$. $\blacksquare$
