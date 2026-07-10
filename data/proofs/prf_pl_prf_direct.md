---
id: prf_pl_prf_direct
claim_id: pl_prf_direct
method: informal
status: reviewed
dependencies:
- pl_inf_modus_ponens
- pl_inf_hypothetical_syllogism
- pl_sem_clause_impl
- pl_ent_def
is_canonical: true
date_added: '2026-07-10T20:18:36.342845Z'
schema_version: 1
---

נצדיק את תקפות השיטה. נניח שברשותנו סדרה סופית של נוסחאות $\varphi = \chi_0, \chi_1, \dots, \chi_n = \psi$, כך שבכל שלב $\chi_i$ מתקבל מ־$\chi_{i-1}$ (ומנוסחאות שהוכחו קודם) על ידי כלל היסק תקף. במקרה הפרוטוטיפי, בכל שלב מסיקים את $\chi_i$ מתוך $\chi_{i-1}$ בעזרת גרירה $\chi_{i-1} \to \chi_i$ ויישום של `pl_inf_modus_ponens`. שרשור של הגרירות המקומיות $\chi_0 \to \chi_1$, $\chi_1 \to \chi_2$, …, $\chi_{n-1} \to \chi_n$ מוליד לפי `pl_inf_hypothetical_syllogism` את הגרירה $\chi_0 \to \chi_n$, כלומר $\varphi \to \psi$. סמנטית, נבחן כל השמת אמת $v$: אם $v(\varphi) = T$ אזי לאורך השרשרת מקבלים גם $v(\psi) = T$; אם $v(\varphi) = F$ אזי לפי `pl_sem_clause_impl` הגרירה $\varphi \to \psi$ מקבלת ערך $T$ ממילא. בשני המקרים $v(\varphi \to \psi) = T$, ולפי `pl_ent_def` הנוסחה $\varphi \to \psi$ אכן נובעת מן ההנחות התחיליות.
