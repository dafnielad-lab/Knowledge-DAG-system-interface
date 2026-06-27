---
id: prf_geometric_series_convergence
claim_id: thm_geometric_series_convergence
method: informal
status: reviewed
dependencies:
- def_infinite_geometric_series
- thm_geometric_sum_finite
- def_limit_of_sequence
- def_convergent_sequence
is_canonical: true
date_added: '2026-06-27T16:13:44.126814Z'
schema_version: 1
---

מסכום סופי: $S_n = a_1 \cdot \frac{q^n - 1}{q - 1} = \frac{a_1}{1 - q} - \frac{a_1 q^n}{1 - q}$.

אם $|q| < 1$ אז $q^n \to 0$ כאשר $n \to \infty$, ולכן $S_n \to \frac{a_1}{1 - q}$.

אם $|q| \geq 1$, $q^n$ אינה שואפת ל-$0$, והטור מתבדר. $\blacksquare$
