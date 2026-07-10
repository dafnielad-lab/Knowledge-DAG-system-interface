---
id: prf_pl_inf_modus_ponens
claim_id: pl_inf_modus_ponens
method: informal
status: reviewed
dependencies:
- pl_ent_def
- pl_sem_clause_impl
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.320347Z'
schema_version: 1
---

לפי הגדרת הנביעה הסמנטית (`pl_ent_def`), עלינו להראות שכל הצבת אמת $v$ המספקת את שתי ההנחות מספקת גם את $q$. תהא $v$ הצבה כזו — כלומר $v(p) = 1$ וגם $v(p \to q) = 1$. לפי סעיף התנאי במשפט חישוב האמת (`pl_sem_clause_impl`), הביטוי $p \to q$ מקבל את הערך $0$ אם ורק אם $v(p) = 1$ ו־$v(q) = 0$; בכל מצב אחר ערכו $1$. אילו היה $v(q) = 0$, אזי מ־$v(p) = 1$ ומהסעיף הנ"ל היינו מקבלים $v(p \to q) = 0$, בסתירה להנחה $v(p \to q) = 1$. לכן $v(q) = 1$. הראנו שלכל הצבה $v$ שמספקת את שתי ההנחות, ערך $q$ תחתיה הוא $1$, ולפיכך $\{p, p \to q\} \models q$ כנדרש. זהו כלל ההיסק הבסיסי ביותר, המשמש כאבן פינה לכל שרשרת הוכחה פורמלית.
