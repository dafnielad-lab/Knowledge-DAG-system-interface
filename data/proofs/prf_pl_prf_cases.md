---
id: prf_pl_prf_cases
claim_id: pl_prf_cases
method: informal
status: reviewed
dependencies:
- pl_sem_clause_disj
- pl_sem_clause_impl
- pl_ent_def
is_canonical: true
date_added: '2026-07-10T20:18:36.345845Z'
schema_version: 1
---

נצדיק את השיטה סמנטית. תהי $v$ השמת אמת המספקת את כל ההנחות של ההוכחה, ובפרט $v(p_1 \vee p_2 \vee \dots \vee p_n) = T$. לפי `pl_sem_clause_disj`, ערך הדיסיונקציה הוא $T$ אם ורק אם קיים לפחות אינדקס אחד $j \in \{1, \dots, n\}$ שעבורו $v(p_j) = T$. הנחת השיטה קובעת שהוכחנו את כל הגרירות $p_i \to \psi$; לפי `pl_sem_clause_impl`, המשמעות היא שבכל השמה שבה $v(p_i) = T$ מתקיים גם $v(\psi) = T$. בפרט בהשמה $v$ שלנו, האינדקס $j$ הנ״ל מקיים $v(p_j) = T$, ולכן $v(\psi) = T$. הראנו אפוא שבכל השמה המקיימת את ההנחות מתקיים $v(\psi) = T$, וזו בדיוק הגרירה הלוגית המבוקשת לפי `pl_ent_def`. הצדקה שקולה נובעת מהשקילות $(p \vee q) \to \psi \;\equiv\; (p \to \psi) \land (q \to \psi)$ ומהכללתה: כל הוכחת מקרים ניתנת לפירוק לאוסף של הוכחות ישירות, אחת עבור כל דיסיונקט.
