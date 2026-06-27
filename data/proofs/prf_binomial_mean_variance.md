---
id: prf_binomial_mean_variance
claim_id: thm_binomial_mean_variance
method: informal
status: reviewed
dependencies:
- def_binomial_distribution
- def_expected_value
- thm_expected_value_linearity
- thm_variance_sum_independent
- def_variance_rv
is_canonical: true
date_added: '2026-06-27T17:22:39.263705Z'
schema_version: 1
---

$X = X_1 + X_2 + \cdots + X_n$ כאשר $X_i \sim \text{Bernoulli}(p)$ בלתי-תלויים.

$E[X_i] = p$, $\text{Var}(X_i) = p(1 - p)$. לפי לינאריות התוחלת: $E[X] = np$. לפי שונות סכום בלתי-תלויים: $\text{Var}(X) = n p(1-p)$. $\blacksquare$
