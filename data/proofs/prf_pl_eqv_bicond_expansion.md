---
id: prf_pl_eqv_bicond_expansion
claim_id: pl_eqv_bicond_expansion
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_valuation
- pl_sem_clause_impl
- pl_sem_clause_conj
- pl_sem_clause_bicond
- pl_sem_truth_table
is_canonical: true
date_added: '2026-07-10T20:18:36.310346Z'
schema_version: 1
---

לפי `pl_eqv_def` יש להראות שלכל השמה $v$ מתקיים $v(p \leftrightarrow q) = v\big((p \rightarrow q) \wedge (q \rightarrow p)\big)$. נבנה טבלת אמת (`pl_sem_truth_table`) על שילובי הערכים של $p$ ו־$q$, כאשר $v(p \leftrightarrow q)$ נקבע לפי `pl_sem_clause_bicond` (אמת בדיוק כאשר לשני האגפים אותו ערך), ערכי המותנים לפי `pl_sem_clause_impl`, וערך הצירוף לפי `pl_sem_clause_conj` (אמת רק כשכל רכיביו אמת).

**$v(p) = T, v(q) = T$:** $v(p \leftrightarrow q) = T$. שני המותנים אמת, ולכן ערך הצירוף $T$.

**$v(p) = T, v(q) = F$:** $v(p \leftrightarrow q) = F$ (ערכים שונים). $v(p \rightarrow q) = F$, ולכן די בכך שהרכיב הראשון שקרי כדי שערך הצירוף יהיה $F$.

**$v(p) = F, v(q) = T$:** $v(p \leftrightarrow q) = F$. הפעם $v(q \rightarrow p) = F$, ולכן ערך הצירוף $F$.

**$v(p) = F, v(q) = F$:** $v(p \leftrightarrow q) = T$. שני המותנים אמת (הנחתם שקרית), ולכן ערך הצירוף $T$.

בכל ארבע ההשמות שני האגפים שווים, ומכאן $p \leftrightarrow q \equiv (p \rightarrow q) \wedge (q \rightarrow p)$.
