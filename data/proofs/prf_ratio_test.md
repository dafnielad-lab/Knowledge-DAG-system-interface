---
id: prf_ratio_test
claim_id: thm_ratio_test
method: informal
status: reviewed
dependencies:
- def_series_convergence
- thm_geometric_series_convergence
- thm_comparison_test
is_canonical: true
date_added: '2026-06-27T17:14:35.075131Z'
schema_version: 1
---

אם $L < 1$: נבחר $r$ עם $L < r < 1$. מסוים $N$, $\frac{a_{n+1}}{a_n} < r$, כלומר $a_n \leq a_N r^{n-N}$ — חסום ע״י טור הנדסי מתכנס. לפי מבחן ההשוואה $\sum a_n$ מתכנס.

אם $L > 1$: $a_n$ עולה החל מאיזשהו $N$, ולכן לא שואפת ל-$0$ — הטור מתבדר. $\blacksquare$
