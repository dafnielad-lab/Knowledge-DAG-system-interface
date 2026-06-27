---
id: prf_divisibility_linear_combinations
claim_id: thm_divisibility_linear_combinations
method: informal
status: reviewed
dependencies:
- def_divisibility
- ax_distributive_law
- ax_multiplication_associativity
- ax_multiplication_commutativity
is_canonical: true
date_added: '2026-06-27T15:58:40.082207Z'
schema_version: 1
---

$a \mid b$ נותן $b = a \cdot k_1$, ו-$a \mid c$ נותן $c = a \cdot k_2$. אז:

$m \cdot b + n \cdot c = m \cdot (a \cdot k_1) + n \cdot (a \cdot k_2) = a \cdot (m \cdot k_1) + a \cdot (n \cdot k_2) = a \cdot (m \cdot k_1 + n \cdot k_2)$

(אסוציאטיביות, קומוטטיביות, פילוג). לכן $a \mid (mb + nc)$. $\blacksquare$
