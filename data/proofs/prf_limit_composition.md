---
id: prf_limit_composition
claim_id: thm_limit_composition
method: informal
status: reviewed
dependencies:
- def_function_limit_formal
- def_continuity_at_point
is_canonical: true
date_added: '2026-06-27T17:14:35.074631Z'
schema_version: 1
---

מרציפות של $f$ ב-$M$: לכל $\epsilon > 0$ קיים $\eta > 0$ כך ש-$|y - M| < \eta \Rightarrow |f(y) - f(M)| < \epsilon$.

מ-$\lim g(x) = M$: עבור אותו $\eta$ קיים $\delta > 0$ כך ש-$0 < |x - x_0| < \delta \Rightarrow |g(x) - M| < \eta$, ולכן $|f(g(x)) - f(M)| < \epsilon$. $\blacksquare$
