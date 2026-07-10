---
id: prf_pl_eqv_impl_as_disj
claim_id: pl_eqv_impl_as_disj
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_sem_valuation
- pl_sem_clause_neg
- pl_sem_clause_disj
- pl_sem_clause_impl
is_canonical: true
date_added: '2026-07-10T20:18:36.304346Z'
schema_version: 1
---

לפי `pl_eqv_def` מספיק להראות שלכל השמה $v$ מתקיים $v(p \rightarrow q) = v(\neg p \vee q)$. נסתמך על `pl_sem_valuation` להגדרת השמה, ונבחן שני מקרים לפי הערך של $v(p)$.

**מקרה א׳: $v(p) = T$.** לפי `pl_sem_clause_impl` הערך $v(p \rightarrow q)$ הוא $F$ בדיוק כאשר $v(p) = T$ ו־$v(q) = F$; אחרת הוא $T$. במקרה שלנו לכן $v(p \rightarrow q) = v(q)$. מצד שני, לפי `pl_sem_clause_neg` מתקיים $v(\neg p) = F$, ולפי `pl_sem_clause_disj` הדיסיונקציה מקבלת את הערך $T$ בדיוק כאשר לפחות אחד מרכיביה $T$; מאחר ש־$v(\neg p) = F$, ערך הדיסיונקציה נקבע על ידי $v(q)$: $v(\neg p \vee q) = v(q)$. שני האגפים שווים.

**מקרה ב׳: $v(p) = F$.** לפי `pl_sem_clause_impl`, כאשר ההנחה שקרית המותנה אמיתי, ולכן $v(p \rightarrow q) = T$. לפי `pl_sem_clause_neg` מתקיים $v(\neg p) = T$, ומכיוון שרכיב אחד של הדיסיונקציה כבר $T$, מ־`pl_sem_clause_disj` נובע $v(\neg p \vee q) = T$. שוב שני האגפים שווים.

מאחר שהערכים שווים בכל השמה, $p \rightarrow q \equiv \neg p \vee q$.
