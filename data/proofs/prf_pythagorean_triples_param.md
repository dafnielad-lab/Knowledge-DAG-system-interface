---
id: prf_pythagorean_triples_param
claim_id: thm_pythagorean_triples_param
method: informal
status: reviewed
dependencies:
- def_pythagorean_triple
- def_divisibility
is_canonical: true
date_added: '2026-06-28T15:07:55.545551Z'
schema_version: 1
---

**הוכחה (אוקלידס).** $a^2 + b^2 = c^2$ עם $\gcd(a, b, c) = 1$. מהזוגיות אחת מ-$a, b$ זוגית והאחרת אי-זוגית; נניח $b$ זוגי.

$b^2 = c^2 - a^2 = (c-a)(c+a)$. שני הגורמים $c \pm a$ זוגיים (כי $c, a$ אי-זוגיים), נכתבם $c-a = 2u, c+a = 2v$.

$\left(\frac{b}{2}\right)^2 = uv$. כי $\gcd(u, v) = 1$, שניהם ריבועים: $u = n^2, v = m^2$.

אז $a = m^2 - n^2$, $c = m^2 + n^2$, $b = 2mn$. $\blacksquare$
