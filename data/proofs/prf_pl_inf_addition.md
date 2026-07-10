---
id: prf_pl_inf_addition
claim_id: pl_inf_addition
method: informal
status: reviewed
dependencies:
- pl_ent_def
- pl_sem_clause_disj
is_canonical: true
date_added: '2026-07-10T20:18:36.331345Z'
schema_version: 1
---

לפי `pl_ent_def` יש להראות שכל הצבת אמת $v$ המספקת את $p$ מספקת גם את $p \lor q$, לכל פסוק $q$ שהוא. תהא $v$ הצבה עם $v(p) = 1$. לפי סעיף הדיסיונקציה (`pl_sem_clause_disj`), $v(p \lor q) = 1$ אם ורק אם $v(p) = 1$ או $v(q) = 1$. מכיוון ש־$v(p) = 1$, התנאי מתקיים ללא תלות בערכו של $v(q)$, ולכן $v(p \lor q) = 1$. הראנו שלכל הצבה שמספקת את $p$ מסופק גם $p \lor q$, ולפיכך $\{p\} \models p \lor q$. זהו כלל "החלשה" — הוא מאפשר להוסיף דיסיונקט שרירותי לטענה קיימת, ומשמש להתאמת נוסחאות לצורה הנחוצה בהוכחות (למשל לצורך יישום סילוגיזם דיסיונקטיבי או רזולוציה).
