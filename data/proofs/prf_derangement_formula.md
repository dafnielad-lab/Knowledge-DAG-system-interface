---
id: prf_derangement_formula
claim_id: thm_derangement_formula
method: informal
status: reviewed
dependencies:
- def_derangement
- thm_inclusion_exclusion_three_sets
- thm_maclaurin_exp
is_canonical: true
date_added: '2026-06-27T17:22:39.263705Z'
schema_version: 1
---

**ע״י הכלה-הפרדה.** $A_i$ — סט הפרמוטציות שמקבעות את $i$. $|A_i| = (n-1)!$, $|A_i \cap A_j| = (n-2)!$, וכו'.

מספר הפרמוטציות שמקבעות לפחות נקודה אחת: $\sum (-1)^{k+1} \binom{n}{k}(n-k)!$. $D_n = n! - $ זה $= n! \sum_{k=0}^n \frac{(-1)^k}{k!}$.

כש-$n \to \infty$, הסכום הפנימי מתכנס ל-$e^{-1}$ (טור מקלורין של $e^{-1}$), ולכן $D_n \approx n!/e$. $\blacksquare$
