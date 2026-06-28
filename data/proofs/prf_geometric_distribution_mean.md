---
id: prf_geometric_distribution_mean
claim_id: thm_geometric_distribution_mean
method: informal
status: reviewed
dependencies:
- def_geometric_distribution
- def_expected_value
- thm_maclaurin_geometric
- thm_power_series_term_differentiation
is_canonical: true
date_added: '2026-06-28T15:07:55.511550Z'
schema_version: 1
---

$E[X] = \sum_{k=1}^{\infty} k (1-p)^{k-1} p = p \sum_{k=1}^{\infty} k q^{k-1}$ (עם $q = 1-p$).

מהטור הגיאומטרי $\sum_{k=0}^{\infty} q^k = \frac{1}{1-q}$ (תקף עבור $|q|<1$), ובאמצעות גזירה איבר-איבר של טור חזקות (מותרת בתוך רדיוס ההתכנסות) נקבל $\sum_{k=1}^{\infty} k q^{k-1} = \frac{1}{(1-q)^2} = \frac{1}{p^2}$. לכן $E[X] = \frac{p}{p^2} = \frac{1}{p}$.

**שונות:** נחשב $E[X(X-1)] = \sum_{k=1}^{\infty} k(k-1) q^{k-1} p = pq \sum_{k=2}^{\infty} k(k-1) q^{k-2}$. גזירה נוספת איבר-איבר נותנת $\sum_{k=2}^{\infty} k(k-1) q^{k-2} = \frac{2}{(1-q)^3} = \frac{2}{p^3}$, ולכן $E[X(X-1)] = \frac{2q}{p^2}$.

מכאן $E[X^2] = E[X(X-1)] + E[X] = \frac{2q}{p^2} + \frac{1}{p} = \frac{2q + p}{p^2} = \frac{2-p}{p^2}$, ולבסוף $\text{Var}(X) = E[X^2] - (E[X])^2 = \frac{2-p}{p^2} - \frac{1}{p^2} = \frac{1-p}{p^2}$. $\blacksquare$
