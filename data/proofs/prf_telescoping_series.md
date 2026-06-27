---
id: prf_telescoping_series
claim_id: thm_telescoping_series
method: informal
status: reviewed
dependencies:
- def_partial_sum
- def_series_convergence
is_canonical: true
date_added: '2026-06-27T16:34:26.423690Z'
schema_version: 1
---

$S_n = (b_1 - b_2) + (b_2 - b_3) + \cdots + (b_n - b_{n+1}) = b_1 - b_{n+1}$ (קנצלציה ביניים).

אם $\lim b_n = L$ אז $\lim S_n = b_1 - L$, וזה סכום הטור. אחרת הטור מתבדר. $\blacksquare$
