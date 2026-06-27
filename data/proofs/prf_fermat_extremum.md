---
id: prf_fermat_extremum
claim_id: thm_fermat_extremum
method: informal
status: reviewed
dependencies:
- def_derivative_at_point
- def_local_extremum
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

נניח $f$ מקבלת מקסימום מקומי ב-$x_0$ פנימית. אז קיימת סביבה שבה $f(x_0 + h) \leq f(x_0)$ לכל $h$ קטן.

גבול מימין: $f'(x_0^+) = \lim_{h \to 0^+} \frac{f(x_0+h) - f(x_0)}{h} \leq 0$ (מונה אי-חיובי, מכנה חיובי).

גבול משמאל: $f'(x_0^-) = \lim_{h \to 0^-} \frac{f(x_0+h) - f(x_0)}{h} \geq 0$.

כי $f$ גזירה, שני הגבולות שווים, ולכן $f'(x_0) = 0$. $\blacksquare$
