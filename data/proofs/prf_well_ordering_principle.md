---
id: prf_well_ordering_principle
claim_id: thm_well_ordering_principle
method: informal
status: reviewed
dependencies:
- def_natural_numbers
- def_proof_by_induction
is_canonical: true
date_added: '2026-06-27T18:47:27.564532Z'
schema_version: 1
---

**שקול לאינדוקציה.** נניח קבוצה $S \subseteq \mathbb{N}$ ללא איבר מינימלי. נראה ש-$S = \emptyset$.

נגדיר $T = \{n : \forall m \leq n, m \notin S\}$. $0 \in T$ (אחרת $0 \in S$ והיה מינימום). אם $n \in T$ ו-$n+1 \in S$, אז $n+1$ מינימלי. אז $n+1 \notin S$ ולכן $n+1 \in T$. באינדוקציה $T = \mathbb{N}$, אז $S = \emptyset$. $\blacksquare$
