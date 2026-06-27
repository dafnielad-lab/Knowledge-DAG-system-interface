---
id: prf_variance_alternative_formula
claim_id: thm_variance_alternative_formula
method: informal
status: reviewed
dependencies:
- def_variance
- def_mean
- ax_distributive_law
is_canonical: true
date_added: '2026-06-27T16:34:26.423690Z'
schema_version: 1
---

$\sigma^2 = \frac{1}{n}\sum (x_i - \bar{x})^2 = \frac{1}{n}\sum (x_i^2 - 2 x_i \bar{x} + \bar{x}^2)$

$= \frac{1}{n}\sum x_i^2 - 2\bar{x} \cdot \frac{1}{n}\sum x_i + \frac{1}{n} \cdot n \cdot \bar{x}^2 = \frac{1}{n}\sum x_i^2 - 2 \bar{x}^2 + \bar{x}^2 = \frac{1}{n}\sum x_i^2 - \bar{x}^2$. $\blacksquare$
