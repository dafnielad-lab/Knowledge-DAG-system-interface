---
id: prf_chebyshev_inequality_prob
claim_id: thm_chebyshev_inequality_prob
method: informal
status: reviewed
dependencies:
- def_variance_rv
- def_expected_value
is_canonical: true
date_added: '2026-06-27T18:47:27.564532Z'
schema_version: 1
---

$\sigma^2 = E[(X - \mu)^2] \geq E[(X - \mu)^2 \cdot \mathbb{1}_{|X-\mu| \geq k\sigma}] \geq (k\sigma)^2 \cdot P(|X - \mu| \geq k\sigma)$.

חלוקה ב-$\sigma^2 k^2$: $P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}$. $\blacksquare$
