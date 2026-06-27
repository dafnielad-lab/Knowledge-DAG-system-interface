---
id: prf_qm_am_inequality
claim_id: thm_qm_am_inequality
method: informal
status: reviewed
dependencies:
- thm_squared_inequality
- thm_cauchy_schwarz_inequality_vectors
is_canonical: true
date_added: '2026-06-27T18:47:27.564532Z'
schema_version: 1
---

מ-קושי-שוורץ: $(\sum a_i \cdot 1)^2 \leq (\sum a_i^2)(\sum 1^2) = n \sum a_i^2$.

לכן $\left(\frac{\sum a_i}{n}\right)^2 \leq \frac{\sum a_i^2}{n}$, ובשורש: AM $\leq$ QM. $\blacksquare$
