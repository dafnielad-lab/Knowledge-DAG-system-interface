---
id: prf_geometric_distribution_mean
claim_id: thm_geometric_distribution_mean
method: informal
status: reviewed
dependencies:
- def_geometric_distribution
- def_expected_value
- thm_maclaurin_geometric
is_canonical: true
date_added: '2026-06-27T18:47:27.564532Z'
schema_version: 1
---

$E[X] = \sum_{k=1}^{\infty} k (1-p)^{k-1} p = p \sum k q^{k-1}$ (עם $q = 1-p$).

$\sum_{k=1}^{\infty} k q^{k-1} = \frac{1}{(1-q)^2} = \frac{1}{p^2}$ (גזירה של הטור הגיאומטרי). לכן $E[X] = \frac{p}{p^2} = \frac{1}{p}$. $\blacksquare$
