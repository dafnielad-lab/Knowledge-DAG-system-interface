---
id: prf_exp_multiplication
claim_id: thm_exp_multiplication
method: informal
status: reviewed
dependencies:
- def_exponential_function
- thm_log_of_power
- thm_log_inverse_of_exp
is_canonical: true
date_added: '2026-06-27T20:41:51.335588Z'
schema_version: 1
---

$(a^x)^y = e^{y \ln(a^x)}$ (לפי הגדרת חזקה כללית $z^t = e^{t \ln z}$, כאן עם $z = a^x$).

$= e^{y \cdot x \ln a}$ (לפי משפט לוגריתם של חזקה: $\ln(a^x) = x \ln a$).

$= e^{xy \ln a} = a^{xy}$ (לפי הגדרת חזקה שוב). $\blacksquare$
