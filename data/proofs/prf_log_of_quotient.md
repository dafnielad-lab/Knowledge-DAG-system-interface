---
id: prf_log_of_quotient
claim_id: thm_log_of_quotient
method: informal
status: reviewed
dependencies:
- def_logarithm
- thm_exp_addition
- thm_exp_negative
is_canonical: true
date_added: '2026-06-28T15:07:55.528049Z'
schema_version: 1
---

יהיו $x, y > 0$. לפי הגדרת הלוגריתם, נסמן $u = \log_b x$ ו-$v = \log_b y$, כך ש-$x = b^u$ ו-$y = b^v$. לפי תכונת החזקה השלילית, $y^{-1} = b^{-v}$. לכן $\frac{x}{y} = x \cdot y^{-1} = b^u \cdot b^{-v}$, ולפי תכונת החזקות הסכומית, $b^u \cdot b^{-v} = b^{u-v}$. מהגדרת הלוגריתם נובע ש-$\log_b(x/y) = u - v = \log_b x - \log_b y$. $\blacksquare$
