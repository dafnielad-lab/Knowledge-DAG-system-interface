---
id: prf_modular_arithmetic_properties
claim_id: thm_modular_arithmetic_properties
method: informal
status: reviewed
dependencies:
- def_congruence_mod
- def_divisibility
is_canonical: true
date_added: '2026-06-27T16:34:26.423690Z'
schema_version: 1
---

$a \equiv b$ פירושו $n \mid (a - b)$, ובאופן דומה $n \mid (c - d)$.

**חיבור:** $(a + c) - (b + d) = (a - b) + (c - d)$, סכום שני מספרים שמתחלקים ב-$n$, ולכן מתחלק ב-$n$ → $a + c \equiv b + d$.

**כפל:** $ac - bd = ac - bc + bc - bd = (a - b) c + b (c - d)$, צירוף לינארי של מספרים שמתחלקים ב-$n$. $\blacksquare$
