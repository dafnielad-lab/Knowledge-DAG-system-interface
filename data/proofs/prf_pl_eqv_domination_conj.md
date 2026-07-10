---
id: prf_pl_eqv_domination_conj
claim_id: pl_eqv_domination_conj
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_clause_conj
- pl_cls_contradiction
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.293346Z'
schema_version: 1
---

תהי $v$ השמה שרירותית. $F$ היא סתירה (pl_cls_contradiction) — $v(F) = F$ תמיד.

לפי pl_sem_clause_conj, $v(p \wedge F) = T$ אם ורק אם $v(p) = T$ וגם $v(F) = T$. התנאי השני לעולם אינו מתקיים, ולכן $v(p \wedge F) = F$ בכל השמה. כלומר $v(p \wedge F) = v(F)$ לכל $v$.

טבלת אמת:

| $p$ | $F$ | $p \wedge F$ |
|---|---|---|
| $T$ | $F$ | $F$ |
| $F$ | $F$ | $F$ |

העמודה השלישית זהה לעמודה השנייה. לפי pl_eqv_def, $p \wedge F \equiv F$.
