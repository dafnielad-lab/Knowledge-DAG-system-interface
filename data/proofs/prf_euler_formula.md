---
id: prf_euler_formula
claim_id: thm_euler_formula
method: informal
status: reviewed
dependencies:
- thm_maclaurin_exp
- thm_maclaurin_sin
- thm_maclaurin_cos
- def_imaginary_unit
is_canonical: true
date_added: '2026-06-27T18:47:27.564532Z'
schema_version: 1
---

מטור מקלורין של $e^x$: $e^{i\theta} = \sum \frac{(i\theta)^n}{n!}$. חזקות $i$: $i^0=1, i^1=i, i^2=-1, i^3=-i$, מחזור 4.

הפרדה לפי זוגיות: איברים זוגיים (חזקות $i^{2k} = (-1)^k$) → $\sum \frac{(-1)^k \theta^{2k}}{(2k)!} = \cos\theta$. איברים אי-זוגיים → $i \sum \frac{(-1)^k \theta^{2k+1}}{(2k+1)!} = i \sin\theta$.

סכום: $e^{i\theta} = \cos\theta + i \sin\theta$. $\blacksquare$
