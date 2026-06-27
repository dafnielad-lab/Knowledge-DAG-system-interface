---
id: prf_mean_value_for_integrals
claim_id: thm_mean_value_for_integrals
method: informal
status: reviewed
dependencies:
- thm_extreme_value_theorem
- thm_intermediate_value
- def_definite_integral
is_canonical: true
date_added: '2026-06-27T16:34:26.423690Z'
schema_version: 1
---

כי $f$ רציפה ב-$[a, b]$, לפי ויירשטראס יש לה מינימום $m$ ומקסימום $M$.

אז $m(b - a) \leq \int_a^b f \leq M(b - a)$, כלומר $m \leq \frac{1}{b-a}\int_a^b f \leq M$.

לפי משפט ערך הביניים, יש $c \in [a, b]$ עם $f(c) = \frac{1}{b-a}\int_a^b f$. $\blacksquare$
