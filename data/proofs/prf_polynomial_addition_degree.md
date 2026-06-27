---
id: prf_polynomial_addition_degree
claim_id: thm_polynomial_addition_degree
method: informal
status: reviewed
dependencies:
- def_polynomial
- def_polynomial_degree
is_canonical: true
date_added: '2026-06-27T16:03:56.114879Z'
schema_version: 1
---

נסמן $\deg p = m$, $\deg q = n$, ובלי הגבלת כלליות $m \geq n$.

בסכום $p + q$, מקדם $x^k$ עבור $k > m$ הוא $0$ (כי $p$ ו-$q$ אינן מכילות חזקות גבוהות מ-$m$). לכן $\deg(p+q) \leq m$.

שוויון מתקיים כאשר $m > n$ (המקדם המוביל של $p$ נשמר), או כאשר $m = n$ והמקדמים המובילים לא מתבטלים בסכום. $\blacksquare$
