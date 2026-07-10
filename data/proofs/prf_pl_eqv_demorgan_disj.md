---
id: prf_pl_eqv_demorgan_disj
claim_id: pl_eqv_demorgan_disj
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_clause_neg
- pl_sem_clause_conj
- pl_sem_clause_disj
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.278847Z'
schema_version: 1
---

תהי $v$ השמה שרירותית. לפי pl_sem_clause_neg, $v(\neg(p \vee q)) = T$ אם ורק אם $v(p \vee q) = F$. לפי pl_sem_clause_disj, $v(p \vee q) = F$ אם ורק אם $v(p) = F$ וגם $v(q) = F$, כלומר $v(\neg p) = T$ וגם $v(\neg q) = T$. לפי pl_sem_clause_conj, תנאי זה שקול ל־$v(\neg p \wedge \neg q) = T$.

טבלת אמת:

| $p$ | $q$ | $p \vee q$ | $\neg(p \vee q)$ | $\neg p$ | $\neg q$ | $\neg p \wedge \neg q$ |
|---|---|---|---|---|---|---|
| $T$ | $T$ | $T$ | $F$ | $F$ | $F$ | $F$ |
| $T$ | $F$ | $T$ | $F$ | $F$ | $T$ | $F$ |
| $F$ | $T$ | $T$ | $F$ | $T$ | $F$ | $F$ |
| $F$ | $F$ | $F$ | $T$ | $T$ | $T$ | $T$ |

העמודות הרביעית והשביעית זהות. לפי pl_eqv_def, $\neg(p \vee q) \equiv \neg p \wedge \neg q$.
