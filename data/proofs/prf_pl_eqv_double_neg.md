---
id: prf_pl_eqv_double_neg
claim_id: pl_eqv_double_neg
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_clause_neg
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.248346Z'
schema_version: 1
---

תהי $v$ השמה שרירותית. לפי pl_sem_clause_neg, $v(\neg p) = T$ אם ורק אם $v(p) = F$, ובאופן שקול $v(\neg p)$ הוא הערך ההפוך של $v(p)$. הפעלה שנייה של הכלל נותנת $v(\neg\neg p) = $ ההפוך של $v(\neg p) = $ ההפוך של ההפוך של $v(p) = v(p)$.

טבלת אמת (pl_sem_valuation):

| $p$ | $\neg p$ | $\neg\neg p$ |
|---|---|---|
| $T$ | $F$ | $T$ |
| $F$ | $T$ | $F$ |

בשתי השורות $v(\neg\neg p) = v(p)$. לפי pl_eqv_def, $\neg\neg p \equiv p$.
