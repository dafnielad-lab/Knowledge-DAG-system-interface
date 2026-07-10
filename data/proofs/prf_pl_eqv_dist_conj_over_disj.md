---
id: prf_pl_eqv_dist_conj_over_disj
claim_id: pl_eqv_dist_conj_over_disj
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_clause_conj
- pl_sem_clause_disj
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.270346Z'
schema_version: 1
---

תהי $v$ השמה שרירותית. נראה שערכי שני הצדדים זהים בכל אחת משמונה השורות של טבלת האמת ל־$p, q, r$:

| $p$ | $q$ | $r$ | $q \vee r$ | $p \wedge (q \vee r)$ | $p \wedge q$ | $p \wedge r$ | $(p \wedge q) \vee (p \wedge r)$ |
|---|---|---|---|---|---|---|---|
| $T$ | $T$ | $T$ | $T$ | $T$ | $T$ | $T$ | $T$ |
| $T$ | $T$ | $F$ | $T$ | $T$ | $T$ | $F$ | $T$ |
| $T$ | $F$ | $T$ | $T$ | $T$ | $F$ | $T$ | $T$ |
| $T$ | $F$ | $F$ | $F$ | $F$ | $F$ | $F$ | $F$ |
| $F$ | $T$ | $T$ | $T$ | $F$ | $F$ | $F$ | $F$ |
| $F$ | $T$ | $F$ | $T$ | $F$ | $F$ | $F$ | $F$ |
| $F$ | $F$ | $T$ | $T$ | $F$ | $F$ | $F$ | $F$ |
| $F$ | $F$ | $F$ | $F$ | $F$ | $F$ | $F$ | $F$ |

הערכים חושבו לפי pl_sem_clause_conj ו־pl_sem_clause_disj. העמודות החמישית והשמינית זהות בכל שורה. באופן קונספטואלי: $v(p \wedge (q \vee r)) = T$ אם ורק אם $v(p) = T$ ולפחות אחד מ־$v(q), v(r)$ הוא $T$, אם ורק אם לפחות אחד מ־$v(p \wedge q), v(p \wedge r)$ הוא $T$. לפי pl_eqv_def, $p \wedge (q \vee r) \equiv (p \wedge q) \vee (p \wedge r)$.
