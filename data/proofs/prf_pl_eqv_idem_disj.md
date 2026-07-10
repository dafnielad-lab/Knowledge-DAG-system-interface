---
id: prf_pl_eqv_idem_disj
claim_id: pl_eqv_idem_disj
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_clause_disj
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.253845Z'
schema_version: 1
---

תהי $v$ השמה שרירותית. לפי pl_sem_clause_disj, $v(p \vee p) = T$ אם ורק אם $v(p) = T$ או $v(p) = T$ — תנאי חופף השקול לתנאי היחיד $v(p) = T$.

טבלת אמת:

| $p$ | $p \vee p$ |
|---|---|
| $T$ | $T$ |
| $F$ | $F$ |

בכל שורה $v(p \vee p) = v(p)$. לפי pl_eqv_def, $p \vee p \equiv p$.
