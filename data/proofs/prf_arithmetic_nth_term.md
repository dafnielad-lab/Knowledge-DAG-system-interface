---
id: prf_arithmetic_nth_term
claim_id: thm_arithmetic_nth_term
method: informal
status: reviewed
dependencies:
- def_arithmetic_sequence
is_canonical: true
date_added: '2026-06-27T16:13:44.126814Z'
schema_version: 1
---

אינדוקציה על $n$. בסיס $n = 1$: $a_1 = a_1 + 0 \cdot d$. ✓

צעד: אם $a_n = a_1 + (n-1)d$, אז $a_{n+1} = a_n + d = a_1 + (n-1)d + d = a_1 + n \cdot d$. $\blacksquare$
