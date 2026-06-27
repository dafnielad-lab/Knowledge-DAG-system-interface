---
id: prf_p_series_convergence
claim_id: thm_p_series_convergence
method: informal
status: reviewed
dependencies:
- def_series_convergence
- thm_integral_power
- thm_integral_one_over_x
- def_improper_integral
- thm_comparison_test
is_canonical: true
date_added: '2026-06-27T17:14:35.075131Z'
schema_version: 1
---

**מבחן האינטגרל.** הפונקציה $f(x) = 1/x^p$ חיובית ויורדת ב-$[1, \infty)$ עבור $p > 0$. השוואת המלבן בקטע $[n, n+1]$ ל-$f$:

$\frac{1}{(n+1)^p} \leq \int_n^{n+1} \frac{1}{x^p} dx \leq \frac{1}{n^p}$

**מקרה $p > 1$:** $\int_1^\infty x^{-p} dx = \left[\frac{x^{1-p}}{1-p}\right]_1^\infty = \frac{1}{p-1}$ סופי. סכימת המלבנים: $\sum 1/n^p \leq 1 + \int_1^\infty x^{-p} dx$ — חסום, אז הטור (עולה וחסום) מתכנס.

**מקרה $p = 1$:** $\int_1^N x^{-1} dx = \ln N \to \infty$. הטור $\sum 1/n$ ($p=1$) חסום מלמטה ע״י אינטגרל זה, אז מתבדר.

**מקרה $p < 1$:** $1/n^p \geq 1/n$, ולפי מבחן ההשוואה (לטור ההרמוני המתבדר) — הטור מתבדר. $\blacksquare$
