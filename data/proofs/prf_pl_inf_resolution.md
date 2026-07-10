---
id: prf_pl_inf_resolution
claim_id: pl_inf_resolution
method: informal
status: reviewed
dependencies:
- pl_ent_def
- pl_sem_clause_disj
- pl_sem_clause_neg
is_canonical: true
date_added: '2026-07-10T20:18:36.339846Z'
schema_version: 1
---

לפי `pl_ent_def` יש להראות שכל הצבת אמת $v$ המספקת את שתי ההנחות מספקת את $q \lor r$. תהא $v$ הצבה עם $v(p \lor q) = 1$ ו־$v(\neg p \lor r) = 1$. נפצל לפי ערכו של $v(p)$:

- **מקרה $v(p) = 1$.** לפי `pl_sem_clause_neg` נקבל $v(\neg p) = 0$. לפי סעיף הדיסיונקציה (`pl_sem_clause_disj`), $v(\neg p \lor r) = 1$ אם ורק אם לפחות אחד מהצדדים אמת; הואיל ו־$v(\neg p) = 0$, חייב להיות $v(r) = 1$. שוב לפי `pl_sem_clause_disj` נקבל $v(q \lor r) = 1$.

- **מקרה $v(p) = 0$.** לפי `pl_sem_clause_disj`, $v(p \lor q) = 1$ אם ורק אם $v(p) = 1$ או $v(q) = 1$; מכיוון ש־$v(p) = 0$ חייב $v(q) = 1$, ומכאן $v(q \lor r) = 1$.

בשני המקרים $v(q \lor r) = 1$, ולכן $\{p \lor q, \neg p \lor r\} \models q \lor r$. חשיבותו של כלל זה: הוא כלל היסק יחיד שדי בו לבניית מערכת הוכחה שלמה לפסוקים בצורת CNF (`pl_nrm_cnf_def`), והוא הבסיס לרוב אלגוריתמי SAT ולהוכחות אוטומטיות.
