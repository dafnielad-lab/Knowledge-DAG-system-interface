---
id: prf_pl_eqv_idem_conj
claim_id: pl_eqv_idem_conj
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_clause_conj
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.250846Z'
schema_version: 1
---

תהי $v$ השמה שרירותית. לפי pl_sem_clause_conj, $v(p \wedge p) = T$ אם ורק אם $v(p) = T$ וגם $v(p) = T$. שני התנאים זהים, ולפיכך הצירוף שקול לתנאי היחיד $v(p) = T$.

טבלת אמת:

| $p$ | $p \wedge p$ |
|---|---|
| $T$ | $T$ |
| $F$ | $F$ |

בכל שורה $v(p \wedge p) = v(p)$. לפי pl_eqv_def, $p \wedge p \equiv p$.
