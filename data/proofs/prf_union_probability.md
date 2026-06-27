---
id: prf_union_probability
claim_id: thm_union_probability
method: informal
status: reviewed
dependencies:
- ax_probability_additivity
is_canonical: true
date_added: '2026-06-27T16:13:44.126814Z'
schema_version: 1
---

נכתוב $A \cup B = A \cup (B \setminus A)$, איחוד זרים. וגם $B = (A \cap B) \cup (B \setminus A)$, זרים.

לפי אדיטיביות: $P(A \cup B) = P(A) + P(B \setminus A)$ ו-$P(B) = P(A \cap B) + P(B \setminus A)$.

חיסור: $P(B \setminus A) = P(B) - P(A \cap B)$. הצבה: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$. $\blacksquare$
