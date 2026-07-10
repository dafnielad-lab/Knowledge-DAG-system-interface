---
id: prf_pl_eqv_contrapositive
claim_id: pl_eqv_contrapositive
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_valuation
- pl_sem_clause_neg
- pl_sem_clause_impl
- pl_sem_truth_table
is_canonical: true
date_added: '2026-07-10T20:18:36.307345Z'
schema_version: 1
---

לפי `pl_eqv_def` נראה שלכל השמה $v$ מתקיים $v(p \rightarrow q) = v(\neg q \rightarrow \neg p)$. מכיוון של־$p$ ול־$q$ ארבעה שילובי אמת אפשריים בלבד, נבחן טבלת אמת מלאה (`pl_sem_truth_table`) ונשתמש ב־`pl_sem_clause_neg` וב־`pl_sem_clause_impl` כדי לחשב את ערכי הנוסחאות.

**$v(p) = T, v(q) = T$:** $v(p \rightarrow q) = T$ (הנחה אמת ומסקנה אמת). $v(\neg q) = F$ ו־$v(\neg p) = F$, ולכן במותנה $\neg q \rightarrow \neg p$ ההנחה שקרית ומכאן שערכו $T$.

**$v(p) = T, v(q) = F$:** $v(p \rightarrow q) = F$ (המקרה היחיד שהמותנה שקרי). $v(\neg q) = T$ ו־$v(\neg p) = F$, ולכן $v(\neg q \rightarrow \neg p) = F$.

**$v(p) = F, v(q) = T$:** $v(p \rightarrow q) = T$. $v(\neg q) = F$, ומכאן שהנחת המותנה השני שקרית וערכו $T$.

**$v(p) = F, v(q) = F$:** $v(p \rightarrow q) = T$. $v(\neg q) = T$ ו־$v(\neg p) = T$, ולכן $v(\neg q \rightarrow \neg p) = T$.

בכל ארבע ההשמות שני האגפים מקבלים את אותו ערך אמת, ולכן על פי `pl_eqv_def` מתקיים $p \rightarrow q \equiv \neg q \rightarrow \neg p$.
