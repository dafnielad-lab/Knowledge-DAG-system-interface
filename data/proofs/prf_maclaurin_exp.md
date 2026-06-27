---
id: prf_maclaurin_exp
claim_id: thm_maclaurin_exp
method: informal
status: reviewed
dependencies:
- def_maclaurin_series
- thm_derivative_exp
is_canonical: true
date_added: '2026-06-27T17:22:39.263705Z'
schema_version: 1
---

$f(x) = e^x$ מקיים $f^{(n)}(x) = e^x$ לכל $n$, ולכן $f^{(n)}(0) = 1$.

הצבה בנוסחת מקלורין: $e^x = \sum_{n=0}^{\infty} \frac{1}{n!} x^n$. (התכנסות בכל $\mathbb{R}$ מובטחת לפי מבחן המנה.) $\blacksquare$
