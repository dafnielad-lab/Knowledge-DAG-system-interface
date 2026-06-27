---
id: prf_limit_quotient
claim_id: thm_limit_quotient
method: informal
status: reviewed
dependencies:
- thm_limit_product
- def_function_limit_formal
is_canonical: true
date_added: '2026-06-27T17:14:35.074631Z'
schema_version: 1
---

כי $M \neq 0$, $g$ אינה אפס בסביבה של $x_0$. אז $\frac{f}{g} = f \cdot \frac{1}{g}$, ולפי כלל המכפלה מספיק להראות $\lim \frac{1}{g(x)} = \frac{1}{M}$. זה נובע מ-$\left|\frac{1}{g(x)} - \frac{1}{M}\right| = \frac{|M - g(x)|}{|g(x) M|}$ וחסם תחתון על $|g|$ בסביבה. $\blacksquare$
