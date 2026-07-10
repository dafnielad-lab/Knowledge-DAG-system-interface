---
id: prf_pl_inf_conjunction
claim_id: pl_inf_conjunction
method: informal
status: reviewed
dependencies:
- pl_ent_def
- pl_sem_clause_conj
is_canonical: true
date_added: '2026-07-10T20:18:36.337347Z'
schema_version: 1
---

לפי `pl_ent_def` יש להראות שכל הצבת אמת $v$ המספקת את שתי ההנחות $p$ ו־$q$ מספקת גם את $p \land q$. תהא $v$ הצבה עם $v(p) = 1$ ו־$v(q) = 1$. לפי סעיף הקוניונקציה (`pl_sem_clause_conj`), $v(p \land q) = 1$ אם ורק אם $v(p) = 1$ וגם $v(q) = 1$. מהנחת השאלה שני התנאים בצד ימין של הביקונדיציונל מתקיימים, ולכן $v(p \land q) = 1$. הראנו שכל הצבה המספקת את שתי ההנחות מספקת את המסקנה, ולפיכך $\{p, q\} \models p \land q$. כלל זה הוא הדואלי של "פישוט" (`pl_inf_simplification`): הפישוט מפרק קוניונקציה לרכיביה, והצירוף מרכיב קוניונקציה מתוך הרכיבים שכבר הוסקו.
