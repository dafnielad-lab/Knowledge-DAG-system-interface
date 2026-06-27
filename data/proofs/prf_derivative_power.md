---
id: prf_derivative_power
claim_id: thm_derivative_power
method: informal
status: reviewed
dependencies:
- def_derivative_at_point
- thm_binomial_theorem
- thm_derivative_constant
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

**עבור $n$ טבעי:** $\frac{(x+h)^n - x^n}{h} = \frac{\sum_{k=0}^n \binom{n}{k} x^{n-k} h^k - x^n}{h} = \sum_{k=1}^n \binom{n}{k} x^{n-k} h^{k-1}$ (בינום ניוטון).

כאשר $h \to 0$, נשארים רק האיברים עם $k = 1$: $\binom{n}{1} x^{n-1} = n x^{n-1}$. שאר האיברים מכילים $h$ חיובי ושואפים ל-$0$.

**עבור $n$ כללי**: ההכללה נעשית באמצעות לוגריתם ונגזרת לוגריתמית. $\blacksquare$
