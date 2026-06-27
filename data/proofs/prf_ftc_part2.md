---
id: prf_ftc_part2
claim_id: thm_ftc_part2
method: informal
status: reviewed
dependencies:
- thm_ftc_part1
- thm_antiderivative_differ_by_constant
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

נגדיר $G(x) := \int_a^x f(t) \, dt$. לפי החלק הראשון, $G' = f$, ולכן $G$ קדומה של $f$.

כל קדומה $F$ שונה מ-$G$ בקבוע: $F(x) = G(x) + c$.

אז $F(b) - F(a) = G(b) - G(a) = \int_a^b f \, dt - 0 = \int_a^b f \, dt$. $\blacksquare$
