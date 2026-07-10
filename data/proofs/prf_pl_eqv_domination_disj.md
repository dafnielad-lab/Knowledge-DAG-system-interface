---
id: prf_pl_eqv_domination_disj
claim_id: pl_eqv_domination_disj
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_clause_disj
- pl_cls_tautology
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.296346Z'
schema_version: 1
---

תהי $v$ השמה שרירותית. $T$ היא טאוטולוגיה (pl_cls_tautology) — $v(T) = T$ תמיד.

לפי pl_sem_clause_disj, $v(p \vee T) = T$ אם ורק אם $v(p) = T$ או $v(T) = T$. הרכיב השני מתקיים תמיד, לפיכך $v(p \vee T) = T$ בכל השמה. כלומר $v(p \vee T) = v(T)$ לכל $v$.

טבלת אמת:

| $p$ | $T$ | $p \vee T$ |
|---|---|---|
| $T$ | $T$ | $T$ |
| $F$ | $T$ | $T$ |

העמודה השלישית זהה לעמודה השנייה. לפי pl_eqv_def, $p \vee T \equiv T$.
