---
id: prf_pl_eqv_comm_conj
claim_id: pl_eqv_comm_conj
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_clause_conj
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.256847Z'
schema_version: 1
---

תהי $v$ השמה שרירותית. לפי pl_sem_clause_conj, $v(p \wedge q) = T$ אם ורק אם $v(p) = T$ וגם $v(q) = T$. תנאי זה סימטרי בשני הרכיבים, לפיכך גם $v(q \wedge p) = T$ בדיוק באותם המקרים.

טבלת אמת מלאה:

| $p$ | $q$ | $p \wedge q$ | $q \wedge p$ |
|---|---|---|---|
| $T$ | $T$ | $T$ | $T$ |
| $T$ | $F$ | $F$ | $F$ |
| $F$ | $T$ | $F$ | $F$ |
| $F$ | $F$ | $F$ | $F$ |

העמודות השלישית והרביעית זהות. לפי pl_eqv_def, $p \wedge q \equiv q \wedge p$.
