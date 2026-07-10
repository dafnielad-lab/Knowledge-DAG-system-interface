---
id: prf_pl_eqv_identity_disj
claim_id: pl_eqv_identity_disj
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_clause_disj
- pl_cls_contradiction
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.290847Z'
schema_version: 1
---

תהי $v$ השמה שרירותית. הסמל $F$ מייצג סתירה (pl_cls_contradiction), ולכן $v(F) = F$ בכל השמה.

לפי pl_sem_clause_disj, $v(p \vee F) = T$ אם ורק אם $v(p) = T$ או $v(F) = T$. האפשרות השנייה אינה מתרחשת אף פעם, כך שהתנאי מצטמצם ל־$v(p) = T$; לפיכך $v(p \vee F) = v(p)$ בכל השמה.

טבלת אמת:

| $p$ | $F$ | $p \vee F$ |
|---|---|---|
| $T$ | $F$ | $T$ |
| $F$ | $F$ | $F$ |

העמודה השלישית זהה לראשונה. לפי pl_eqv_def, $p \vee F \equiv p$.
