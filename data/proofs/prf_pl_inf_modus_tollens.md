---
id: prf_pl_inf_modus_tollens
claim_id: pl_inf_modus_tollens
method: informal
status: reviewed
dependencies:
- pl_ent_def
- pl_sem_clause_impl
- pl_sem_clause_neg
is_canonical: true
date_added: '2026-07-10T20:18:36.323346Z'
schema_version: 1
---

לפי `pl_ent_def` יש להראות שכל הצבת אמת $v$ המספקת את $\neg q$ ואת $p \to q$ מספקת גם את $\neg p$. תהא $v$ הצבה כזו: $v(\neg q) = 1$ ו־$v(p \to q) = 1$. מסעיף השלילה במשפט חישוב האמת (`pl_sem_clause_neg`) נקבל ש־$v(\neg q) = 1$ אם ורק אם $v(q) = 0$, ולכן $v(q) = 0$. נניח בשלילה ש־$v(p) = 1$. אז לפי סעיף התנאי (`pl_sem_clause_impl`), מ־$v(p) = 1$ ו־$v(q) = 0$ נובע $v(p \to q) = 0$, בסתירה להנחה $v(p \to q) = 1$. לכן $v(p) = 0$, ולפי `pl_sem_clause_neg` נקבל $v(\neg p) = 1$. הראנו שלכל הצבה המספקת את ההנחות מסופקת גם המסקנה, ולפיכך $\{\neg q, p \to q\} \models \neg p$. כלל זה מהווה את הבסיס הסמנטי לשיטת ההוכחה בהיפוך־נגדי.
