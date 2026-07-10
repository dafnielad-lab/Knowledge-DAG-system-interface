---
id: prf_pl_inf_simplification
claim_id: pl_inf_simplification
method: informal
status: reviewed
dependencies:
- pl_ent_def
- pl_sem_clause_conj
is_canonical: true
date_added: '2026-07-10T20:18:36.334347Z'
schema_version: 1
---

יש להוכיח שתי נביעות. לפי `pl_ent_def`, די להראות שלכל הצבת אמת $v$ המספקת את $p \land q$ מתקיים גם $v(p) = 1$ וגם $v(q) = 1$. תהא $v$ הצבה עם $v(p \land q) = 1$. לפי סעיף הקוניונקציה (`pl_sem_clause_conj`), $v(p \land q) = 1$ אם ורק אם $v(p) = 1$ וגם $v(q) = 1$. מכיוון שההנחה נותנת $v(p \land q) = 1$, מסקנה מיידית משמעו של "אם ורק אם" היא ש־$v(p) = 1$ ובאותה מידה $v(q) = 1$. לכן כל הצבה המספקת את ההנחה מספקת את שני הרכיבים, ומכאן שתי הנביעות $\{p \land q\} \models p$ ו־$\{p \land q\} \models q$. כלל זה הוא הדואלי של "צירוף" (`pl_inf_conjunction`) — צירוף מרכיב קוניונקציה, ופישוט מפרק אותה.
