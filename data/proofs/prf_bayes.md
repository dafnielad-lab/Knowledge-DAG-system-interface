---
id: prf_bayes
claim_id: thm_bayes
method: informal
status: reviewed
dependencies:
- def_conditional_probability
is_canonical: true
date_added: '2026-06-27T16:13:44.126814Z'
schema_version: 1
---

מההגדרה $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ ו-$P(B \mid A) = \frac{P(A \cap B)}{P(A)}$.

הצירוף נותן $P(A \cap B) = P(B \mid A) \cdot P(A)$, ולכן $P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}$. $\blacksquare$
