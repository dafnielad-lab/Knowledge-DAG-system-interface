---
id: prf_pl_eqv_dist_disj_over_conj
claim_id: pl_eqv_dist_disj_over_conj
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_clause_conj
- pl_sem_clause_disj
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.273346Z'
schema_version: 1
---

תהי $v$ השמה שרירותית. נבנה טבלת אמת עבור שמונת הצירופים האפשריים של $p, q, r$:

| $p$ | $q$ | $r$ | $q \wedge r$ | $p \vee (q \wedge r)$ | $p \vee q$ | $p \vee r$ | $(p \vee q) \wedge (p \vee r)$ |
|---|---|---|---|---|---|---|---|
| $T$ | $T$ | $T$ | $T$ | $T$ | $T$ | $T$ | $T$ |
| $T$ | $T$ | $F$ | $F$ | $T$ | $T$ | $T$ | $T$ |
| $T$ | $F$ | $T$ | $F$ | $T$ | $T$ | $T$ | $T$ |
| $T$ | $F$ | $F$ | $F$ | $T$ | $T$ | $T$ | $T$ |
| $F$ | $T$ | $T$ | $T$ | $T$ | $T$ | $T$ | $T$ |
| $F$ | $T$ | $F$ | $F$ | $F$ | $T$ | $F$ | $F$ |
| $F$ | $F$ | $T$ | $F$ | $F$ | $F$ | $T$ | $F$ |
| $F$ | $F$ | $F$ | $F$ | $F$ | $F$ | $F$ | $F$ |

הערכים מבוססים על pl_sem_clause_conj ו־pl_sem_clause_disj. העמודות החמישית והשמינית זהות. באופן שקול: אם $v(p) = T$ אזי שני הצדדים אמת (הפיסקה השמאלית אמת ישירות; הימנית — כי כל דיסיונקציה עם רכיב אמת היא אמת). אם $v(p) = F$, שני הצדדים תלויים בערך של $q \wedge r$: $v(p \vee (q \wedge r)) = v(q \wedge r)$, ואילו $v((p \vee q) \wedge (p \vee r)) = v(q) \wedge v(r) = v(q \wedge r)$. לפי pl_eqv_def, $p \vee (q \wedge r) \equiv (p \vee q) \wedge (p \vee r)$.
