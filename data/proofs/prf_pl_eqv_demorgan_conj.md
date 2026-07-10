---
id: prf_pl_eqv_demorgan_conj
claim_id: pl_eqv_demorgan_conj
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_clause_neg
- pl_sem_clause_conj
- pl_sem_clause_disj
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.276345Z'
schema_version: 1
---

תהי $v$ השמה שרירותית. לפי pl_sem_clause_neg, $v(\neg(p \wedge q)) = T$ אם ורק אם $v(p \wedge q) = F$. לפי pl_sem_clause_conj, $v(p \wedge q) = F$ אם ורק אם $v(p) = F$ או $v(q) = F$, כלומר $v(\neg p) = T$ או $v(\neg q) = T$. לפי pl_sem_clause_disj, תנאי זה שקול ל־$v(\neg p \vee \neg q) = T$.

טבלת אמת:

| $p$ | $q$ | $p \wedge q$ | $\neg(p \wedge q)$ | $\neg p$ | $\neg q$ | $\neg p \vee \neg q$ |
|---|---|---|---|---|---|---|
| $T$ | $T$ | $T$ | $F$ | $F$ | $F$ | $F$ |
| $T$ | $F$ | $F$ | $T$ | $F$ | $T$ | $T$ |
| $F$ | $T$ | $F$ | $T$ | $T$ | $F$ | $T$ |
| $F$ | $F$ | $F$ | $T$ | $T$ | $T$ | $T$ |

העמודות הרביעית והשביעית זהות. לפי pl_eqv_def, $\neg(p \wedge q) \equiv \neg p \vee \neg q$.
