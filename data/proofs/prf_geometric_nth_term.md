---
id: prf_geometric_nth_term
claim_id: thm_geometric_nth_term
method: informal
status: reviewed
dependencies:
- def_geometric_sequence
- thm_power_addition_rule
- def_proof_by_induction
is_canonical: true
date_added: '2026-06-28T15:07:55.513550Z'
schema_version: 1
---

אינדוקציה על $n$. בסיס $n = 1$: $a_1 = a_1 \cdot q^0$. ✓

צעד: אם $a_n = a_1 q^{n-1}$, אז $a_{n+1} = a_n \cdot q = a_1 q^{n-1} \cdot q = a_1 q^n$. $\blacksquare$
