---
id: prf_antiderivative_differ_by_constant
claim_id: thm_antiderivative_differ_by_constant
method: informal
status: reviewed
dependencies:
- def_antiderivative
- thm_mean_value_theorem
is_canonical: true
date_added: '2026-06-28T15:07:55.484052Z'
schema_version: 1
---

נגדיר $H := F_1 - F_2$. אז $H' = F_1' - F_2' = f - f = 0$ בכל הקטע.

לפי משפט הערך הממוצע, פונקציה עם נגזרת אפס בקטע היא קבועה (לכל $x_1 < x_2$ קיים $c$ עם $H(x_2) - H(x_1) = H'(c)(x_2 - x_1) = 0$). $\blacksquare$
