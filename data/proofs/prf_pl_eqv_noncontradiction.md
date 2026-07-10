---
id: prf_pl_eqv_noncontradiction
claim_id: pl_eqv_noncontradiction
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_clause_neg
- pl_sem_clause_conj
- pl_cls_contradiction
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.301345Z'
schema_version: 1
---

תהי $v$ השמה שרירותית. לפי pl_sem_clause_neg, ערכיהם של $p$ ו־$\neg p$ הפוכים בכל השמה — לעולם לא שניהם $T$.

לפי pl_sem_clause_conj, $v(p \wedge \neg p) = T$ אם ורק אם $v(p) = T$ וגם $v(\neg p) = T$. תנאי זה בלתי אפשרי, לפיכך $v(p \wedge \neg p) = F$ בכל השמה. מכאן ש־$p \wedge \neg p$ היא סתירה (pl_cls_contradiction).

טבלת אמת:

| $p$ | $\neg p$ | $p \wedge \neg p$ |
|---|---|---|
| $T$ | $F$ | $F$ |
| $F$ | $T$ | $F$ |

העמודה השלישית קבועה $F$. לפי pl_eqv_def, $p \wedge \neg p \equiv F$. זהות זו היא הבסיס להוכחה בדרך השלילה: אם נחזה שהנחה מובילה ל־$\alpha \wedge \neg \alpha$ עבור טענה כלשהי, אזי ההנחה שקולה ל־$F$ ואינה יכולה להתקיים.
