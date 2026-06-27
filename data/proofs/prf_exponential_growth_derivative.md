---
id: prf_exponential_growth_derivative
claim_id: thm_exponential_growth_derivative
method: informal
status: reviewed
dependencies:
- thm_derivative_exp
- thm_derivative_chain
- def_exponential_growth_model
is_canonical: true
date_added: '2026-06-27T16:34:26.423690Z'
schema_version: 1
---

אם $y = y_0 e^{kt}$ אז $y' = y_0 e^{kt} \cdot k = k \cdot y$, ו-$y(0) = y_0$.

יחידות: אם $z$ פתרון אחר של $z' = kz$ עם $z(0) = y_0$, נגדיר $w = z/y$. אז $w' = (z' y - z y')/y^2 = (kzy - kzy)/y^2 = 0$, ולכן $w$ קבוע. ערך התחלתי $w(0) = 1$, אז $z = y$. $\blacksquare$
