---
id: prf_pl_inf_disjunctive_syllogism
claim_id: pl_inf_disjunctive_syllogism
method: informal
status: reviewed
dependencies:
- pl_ent_def
- pl_sem_clause_disj
- pl_sem_clause_neg
is_canonical: true
date_added: '2026-07-10T20:18:36.328846Z'
schema_version: 1
---

לפי `pl_ent_def` יש להראות שכל הצבת אמת $v$ המספקת את $p \lor q$ ואת $\neg p$ מספקת גם את $q$. תהא $v$ הצבה כזו: $v(p \lor q) = 1$ ו־$v(\neg p) = 1$. לפי סעיף השלילה (`pl_sem_clause_neg`), $v(\neg p) = 1$ אם ורק אם $v(p) = 0$, ולכן $v(p) = 0$. לפי סעיף הדיסיונקציה (`pl_sem_clause_disj`), $v(p \lor q) = 1$ אם ורק אם $v(p) = 1$ או $v(q) = 1$ (לפחות אחד מהם). מכיוון ש־$v(p) = 0$, חייב להיות $v(q) = 1$, אחרת היינו מקבלים $v(p \lor q) = 0$, בסתירה להנחה. הראנו שכל הצבה המספקת את ההנחות מספקת את $q$, ולכן $\{p \lor q, \neg p\} \models q$. כלל זה מנסח את האינטואיציה של "פסילת אפשרות" בהוכחה במקרים.
