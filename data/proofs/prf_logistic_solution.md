---
id: prf_logistic_solution
claim_id: thm_logistic_solution
method: informal
status: reviewed
dependencies:
- def_logistic_growth
- thm_integral_substitution
- thm_integral_one_over_x
is_canonical: true
date_added: '2026-06-27T17:22:39.263705Z'
schema_version: 1
---

המשוואה $\frac{dP}{dt} = rP(1 - P/K)$ ניתנת לפתרון בהפרדת משתנים: $\int \frac{dP}{P(1 - P/K)} = \int r \, dt$.

פיצול לשברים חלקיים: $\frac{1}{P(1-P/K)} = \frac{1}{P} + \frac{1/K}{1 - P/K}$.

אינטגרציה ופתרון ל-$P(t)$ נותנים את הנוסחה הלוגיסטית. $\blacksquare$
