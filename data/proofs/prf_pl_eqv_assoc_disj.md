---
id: prf_pl_eqv_assoc_disj
claim_id: pl_eqv_assoc_disj
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_clause_disj
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.267345Z'
schema_version: 1
---

תהי $v$ השמה שרירותית. הפעלה כפולה של pl_sem_clause_disj נותנת:

$v((p \vee q) \vee r) = F$ אם ורק אם $v(p \vee q) = F$ וגם $v(r) = F$, כלומר $v(p) = F$ וגם $v(q) = F$ וגם $v(r) = F$.

$v(p \vee (q \vee r)) = F$ אם ורק אם $v(p) = F$ וגם $v(q \vee r) = F$, כלומר $v(p) = F$ וגם $v(q) = F$ וגם $v(r) = F$.

שני הביטויים שקר בדיוק כאשר כל שלושת הרכיבים שקר, ואמת בכל שאר שבע הצירופים. לפיכך $v((p \vee q) \vee r) = v(p \vee (q \vee r))$ לכל השמה. לפי pl_eqv_def, $(p \vee q) \vee r \equiv p \vee (q \vee r)$.
