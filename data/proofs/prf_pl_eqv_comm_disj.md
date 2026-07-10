---
id: prf_pl_eqv_comm_disj
claim_id: pl_eqv_comm_disj
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_clause_disj
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.259346Z'
schema_version: 1
---

תהי $v$ השמה שרירותית. לפי pl_sem_clause_disj, $v(p \vee q) = T$ אם ורק אם $v(p) = T$ או $v(q) = T$. הקשר "או" (הכולל) סימטרי, לפיכך התנאי מתקיים בדיוק כשמתקיים $v(q) = T$ או $v(p) = T$, שהוא בדיוק $v(q \vee p) = T$.

טבלת אמת:

| $p$ | $q$ | $p \vee q$ | $q \vee p$ |
|---|---|---|---|
| $T$ | $T$ | $T$ | $T$ |
| $T$ | $F$ | $T$ | $T$ |
| $F$ | $T$ | $T$ | $T$ |
| $F$ | $F$ | $F$ | $F$ |

העמודות השלישית והרביעית זהות. לפי pl_eqv_def, $p \vee q \equiv q \vee p$.
