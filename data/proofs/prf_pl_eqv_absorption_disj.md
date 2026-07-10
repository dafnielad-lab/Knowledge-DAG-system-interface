---
id: prf_pl_eqv_absorption_disj
claim_id: pl_eqv_absorption_disj
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_clause_conj
- pl_sem_clause_disj
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.284846Z'
schema_version: 1
---

תהי $v$ השמה שרירותית. נפצל לפי הערך של $v(p)$:

**מקרה 1:** $v(p) = T$. לפי pl_sem_clause_disj, $v(p \vee (p \wedge q)) = T$ (הרכיב הראשון אמת). לפיכך $v(p \vee (p \wedge q)) = T = v(p)$.

**מקרה 2:** $v(p) = F$. לפי pl_sem_clause_conj, $v(p \wedge q) = F$ (הרכיב הראשון שקר). לפי pl_sem_clause_disj, $v(p \vee (p \wedge q)) = F \vee F = F = v(p)$.

טבלת אמת:

| $p$ | $q$ | $p \wedge q$ | $p \vee (p \wedge q)$ |
|---|---|---|---|
| $T$ | $T$ | $T$ | $T$ |
| $T$ | $F$ | $F$ | $T$ |
| $F$ | $T$ | $F$ | $F$ |
| $F$ | $F$ | $F$ | $F$ |

העמודה הרביעית זהה לעמודה של $p$. לפי pl_eqv_def, $p \vee (p \wedge q) \equiv p$.
