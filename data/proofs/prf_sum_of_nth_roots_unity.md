---
id: prf_sum_of_nth_roots_unity
claim_id: thm_sum_of_nth_roots_unity
method: informal
status: reviewed
dependencies:
- thm_nth_roots_of_complex
- thm_geometric_sum_finite
is_canonical: true
date_added: '2026-06-27T18:47:27.564532Z'
schema_version: 1
---

שורשי היחידה $\omega_k = e^{2\pi i k / n}$ הם $1, \omega, \omega^2, \ldots, \omega^{n-1}$ עם $\omega = e^{2\pi i / n}$.

סכום: $\sum \omega^k = \frac{\omega^n - 1}{\omega - 1} = \frac{1 - 1}{\omega - 1} = 0$ (כש-$\omega \neq 1$). $\blacksquare$
