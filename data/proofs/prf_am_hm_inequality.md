---
id: prf_am_hm_inequality
claim_id: thm_am_hm_inequality
method: informal
status: reviewed
dependencies:
- thm_am_gm_n_variables
is_canonical: true
date_added: '2026-06-27T18:47:27.564532Z'
schema_version: 1
---

מ-AM-GM על $a_1, \ldots, a_n$: $\frac{\sum a_i}{n} \geq \sqrt[n]{\prod a_i}$.

ומ-AM-GM על $1/a_1, \ldots, 1/a_n$: $\frac{\sum 1/a_i}{n} \geq \sqrt[n]{1/\prod a_i} = 1/\sqrt[n]{\prod a_i}$.

חילוק/הפיכה: $\frac{n}{\sum 1/a_i} \leq \sqrt[n]{\prod a_i} \leq \frac{\sum a_i}{n}$. כלומר AM ≥ GM ≥ HM. $\blacksquare$
