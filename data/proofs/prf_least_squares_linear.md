---
id: prf_least_squares_linear
claim_id: thm_least_squares_linear
method: informal
status: reviewed
dependencies:
- thm_fermat_extremum
is_canonical: true
date_added: '2026-06-28T15:07:55.526551Z'
schema_version: 1
---

מינימום $S(a, b) = \sum(y_i - ax_i - b)^2$ בעזרת נגזרות חלקיות:

$\partial S/\partial b = -2 \sum(y_i - ax_i - b) = 0 \Rightarrow b = \bar y - a \bar x$.

$\partial S/\partial a = -2 \sum x_i(y_i - ax_i - b) = 0$, הצבה של $b$ ופתרון: $a = \frac{\sum(x_i - \bar x)(y_i - \bar y)}{\sum(x_i - \bar x)^2}$. $\blacksquare$
