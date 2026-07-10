---
id: prf_pl_eqv_excluded_middle
claim_id: pl_eqv_excluded_middle
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_clause_neg
- pl_sem_clause_disj
- pl_cls_tautology
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.298845Z'
schema_version: 1
---

תהי $v$ השמה שרירותית. לפי pl_sem_clause_neg, ערכיהם של $p$ ו־$\neg p$ הפוכים; כלומר בכל השמה בדיוק אחד משניהם מקבל את הערך $T$ והשני $F$.

לפי pl_sem_clause_disj, $v(p \vee \neg p) = T$ אם ורק אם לפחות אחד מהרכיבים אמת. מהניתוח לעיל, בדיוק אחד מהם אמת בכל השמה, לפיכך $v(p \vee \neg p) = T$ תמיד. מכאן ש־$p \vee \neg p$ היא טאוטולוגיה (pl_cls_tautology).

טבלת אמת:

| $p$ | $\neg p$ | $p \vee \neg p$ |
|---|---|---|
| $T$ | $F$ | $T$ |
| $F$ | $T$ | $T$ |

העמודה השלישית קבועה $T$. לפי pl_eqv_def, $p \vee \neg p \equiv T$.
