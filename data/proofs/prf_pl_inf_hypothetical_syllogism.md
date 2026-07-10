---
id: prf_pl_inf_hypothetical_syllogism
claim_id: pl_inf_hypothetical_syllogism
method: informal
status: reviewed
dependencies:
- pl_ent_def
- pl_sem_clause_impl
is_canonical: true
date_added: '2026-07-10T20:18:36.325845Z'
schema_version: 1
---

יש להראות, לפי `pl_ent_def`, שכל הצבת אמת $v$ המספקת את שתי ההנחות מספקת את $p \to r$. תהא $v$ הצבה כזו: $v(p \to q) = 1$ ו־$v(q \to r) = 1$. לפי סעיף התנאי (`pl_sem_clause_impl`), די להראות שאם $v(p) = 1$ אזי $v(r) = 1$; אם $v(p) = 0$, המותנה $p \to r$ מקבל אוטומטית ערך $1$ ואין מה להוכיח. נניח אפוא $v(p) = 1$. מ־$v(p \to q) = 1$ ומ־$v(p) = 1$ — לפי סעיף התנאי — נקבל $v(q) = 1$ (שכן אחרת המותנה היה שקר). כעת, מ־$v(q) = 1$ ומ־$v(q \to r) = 1$ — שוב לפי `pl_sem_clause_impl` — נקבל $v(r) = 1$. הראנו שבכל הצבה המספקת את ההנחות, כאשר $v(p) = 1$ מתקיים $v(r) = 1$; ובכל מקרה $v(p \to r) = 1$. לפיכך $\{p \to q, q \to r\} \models p \to r$. כלל זה הוא היסוד לבניית שרשראות של גרירות בהוכחות ישירות.
