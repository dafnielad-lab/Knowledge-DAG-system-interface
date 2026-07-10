---
id: prf_pl_eqv_assoc_conj
claim_id: pl_eqv_assoc_conj
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_clause_conj
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.264846Z'
schema_version: 1
---

תהי $v$ השמה שרירותית. הפעלה כפולה של pl_sem_clause_conj נותנת:

$v((p \wedge q) \wedge r) = T$ אם ורק אם $v(p \wedge q) = T$ וגם $v(r) = T$, כלומר $v(p) = T$ וגם $v(q) = T$ וגם $v(r) = T$.

$v(p \wedge (q \wedge r)) = T$ אם ורק אם $v(p) = T$ וגם $v(q \wedge r) = T$, כלומר $v(p) = T$ וגם $v(q) = T$ וגם $v(r) = T$.

שני הביטויים אמת בדיוק כאשר שלושת הרכיבים $p, q, r$ מקבלים את הערך $T$, ובכל שאר שבע הצירופים בטבלה בת שמונה השורות שניהם שקר. לפיכך $v((p \wedge q) \wedge r) = v(p \wedge (q \wedge r))$ לכל השמה. לפי pl_eqv_def, $(p \wedge q) \wedge r \equiv p \wedge (q \wedge r)$.
