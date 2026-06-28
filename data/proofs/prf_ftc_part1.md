---
id: prf_ftc_part1
claim_id: thm_ftc_part1
method: informal
status: reviewed
dependencies:
- def_definite_integral
- def_derivative_at_point
- thm_extreme_value_theorem
- thm_squeeze_theorem
is_canonical: true
date_added: '2026-06-28T15:02:41.618553Z'
schema_version: 1
---

$F(x + h) - F(x) = \int_x^{x+h} f(t) \, dt$.

כי $f$ רציפה ב-$[x, x+h]$, ויירשטראס מבטיח שיש בו ערכי מקסימום $M$ ומינימום $m$. לכן $mh \leq F(x+h) - F(x) \leq Mh$, כלומר $m \leq \frac{F(x+h) - F(x)}{h} \leq M$.

כש-$h \to 0$, $m, M \to f(x)$ (רציפות), ולפי סנדוויץ׳: $F'(x) = f(x)$. $\blacksquare$
