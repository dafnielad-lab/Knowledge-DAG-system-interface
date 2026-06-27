---
id: prf_log_of_product
claim_id: thm_log_of_product
method: informal
status: reviewed
dependencies:
- def_logarithm
- thm_exp_addition
is_canonical: true
date_added: '2026-06-27T16:13:44.126814Z'
schema_version: 1
---

יהיו $u = \log_b x$, $v = \log_b y$. אז $b^u = x$, $b^v = y$.

$xy = b^u \cdot b^v = b^{u+v}$, ולכן $\log_b(xy) = u + v = \log_b x + \log_b y$. $\blacksquare$
