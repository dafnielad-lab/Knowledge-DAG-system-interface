---
id: prf_divisibility_transitivity
claim_id: thm_divisibility_transitivity
method: informal
status: reviewed
dependencies:
- def_divisibility
- ax_multiplication_associativity
is_canonical: true
date_added: '2026-06-27T15:58:40.082207Z'
schema_version: 1
---

מ-$a \mid b$ קיים $k_1$ כך ש-$b = a \cdot k_1$. מ-$b \mid c$ קיים $k_2$ כך ש-$c = b \cdot k_2$.

אז $c = (a \cdot k_1) \cdot k_2 = a \cdot (k_1 \cdot k_2)$ (לפי אסוציאטיביות), ולכן $a \mid c$ (העד הוא $k_1 \cdot k_2$). $\blacksquare$
