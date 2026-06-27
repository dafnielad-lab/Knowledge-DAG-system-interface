---
id: prf_law_of_total_probability
claim_id: thm_law_of_total_probability
method: informal
status: reviewed
dependencies:
- ax_probability_additivity
- def_conditional_probability
is_canonical: true
date_added: '2026-06-27T17:22:39.263705Z'
schema_version: 1
---

$\{B_i\}$ חלוקה של $\Omega$, אז $\{A \cap B_i\}$ חלוקה של $A$ (זרים בזוגות). לפי אדיטיביות:

$P(A) = \sum_i P(A \cap B_i) = \sum_i P(A \mid B_i) P(B_i)$ (לפי הגדרת הסתברות מותנית). $\blacksquare$
