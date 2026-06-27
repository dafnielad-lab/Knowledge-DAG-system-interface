---
id: prf_rational_exponent_addition
claim_id: thm_rational_exponent_addition
method: informal
status: reviewed
dependencies:
- def_rational_exponent
- def_nth_root
- thm_power_addition_rule
- thm_power_multiplication_rule
is_canonical: true
date_added: '2026-06-27T16:03:56.114879Z'
schema_version: 1
---

נסמן $r = p/q$ ו-$s = m/n$. נחבר במכנה משותף: $r + s = (pn + qm)/(qn)$.

$a^r \cdot a^s = \sqrt[qn]{a^{pn}} \cdot \sqrt[qn]{a^{qm}} = \sqrt[qn]{a^{pn} \cdot a^{qm}} = \sqrt[qn]{a^{pn + qm}} = a^{(pn+qm)/(qn)} = a^{r+s}$

(תוך שימוש בחוקי חזקות הטבעיים והגדרת השורש מסדר $n$). $\blacksquare$
