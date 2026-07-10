---
id: prf_pl_eqv_absorption_conj
claim_id: pl_eqv_absorption_conj
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_clause_conj
- pl_sem_clause_disj
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.281846Z'
schema_version: 1
---

תהי $v$ השמה שרירותית. נפצל לפי הערך של $v(p)$:

**מקרה 1:** $v(p) = T$. לפי pl_sem_clause_disj, $v(p \vee q) = T$ (ללא תלות ב־$v(q)$). לפי pl_sem_clause_conj, $v(p \wedge (p \vee q)) = T$. לפיכך $v(p \wedge (p \vee q)) = T = v(p)$.

**מקרה 2:** $v(p) = F$. לפי pl_sem_clause_conj, $v(p \wedge (p \vee q)) = F$ (הרכיב הראשון שקר). לפיכך $v(p \wedge (p \vee q)) = F = v(p)$.

טבלת אמת:

| $p$ | $q$ | $p \vee q$ | $p \wedge (p \vee q)$ |
|---|---|---|---|
| $T$ | $T$ | $T$ | $T$ |
| $T$ | $F$ | $T$ | $T$ |
| $F$ | $T$ | $T$ | $F$ |
| $F$ | $F$ | $F$ | $F$ |

העמודה הרביעית זהה לעמודה של $p$. לפי pl_eqv_def, $p \wedge (p \vee q) \equiv p$.
