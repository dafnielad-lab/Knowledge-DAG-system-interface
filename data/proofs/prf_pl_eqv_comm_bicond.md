---
id: prf_pl_eqv_comm_bicond
claim_id: pl_eqv_comm_bicond
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_clause_bicond
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.262346Z'
schema_version: 1
---

תהי $v$ השמה שרירותית. לפי pl_sem_clause_bicond, $v(p \leftrightarrow q) = T$ אם ורק אם $v(p) = v(q)$. יחס השוויון בין ערכי אמת סימטרי: $v(p) = v(q)$ אם ורק אם $v(q) = v(p)$, ולפיכך $v(q \leftrightarrow p) = T$ בדיוק באותם המקרים.

טבלת אמת:

| $p$ | $q$ | $p \leftrightarrow q$ | $q \leftrightarrow p$ |
|---|---|---|---|
| $T$ | $T$ | $T$ | $T$ |
| $T$ | $F$ | $F$ | $F$ |
| $F$ | $T$ | $F$ | $F$ |
| $F$ | $F$ | $T$ | $T$ |

העמודות השלישית והרביעית זהות. לפי pl_eqv_def, $p \leftrightarrow q \equiv q \leftrightarrow p$. יש להדגיש שהתכונה אינה נכונה עבור הגרירה $\rightarrow$, שאינה חילופית.
