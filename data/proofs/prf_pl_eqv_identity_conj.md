---
id: prf_pl_eqv_identity_conj
claim_id: pl_eqv_identity_conj
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_clause_conj
- pl_cls_tautology
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.287347Z'
schema_version: 1
---

תהי $v$ השמה שרירותית. הסמל $T$ מייצג טאוטולוגיה (pl_cls_tautology), ולכן $v(T) = T$ בכל השמה.

לפי pl_sem_clause_conj, $v(p \wedge T) = T$ אם ורק אם $v(p) = T$ וגם $v(T) = T$. התנאי השני מתקיים תמיד, כך שהתנאי המצטבר מצטמצם ל־$v(p) = T$; לפיכך $v(p \wedge T) = v(p)$ בכל השמה.

טבלת אמת:

| $p$ | $T$ | $p \wedge T$ |
|---|---|---|
| $T$ | $T$ | $T$ |
| $F$ | $T$ | $F$ |

העמודה השלישית זהה לראשונה. לפי pl_eqv_def, $p \wedge T \equiv p$.
