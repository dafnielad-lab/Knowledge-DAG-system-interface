---
id: prf_pl_ent_tautology_iff
claim_id: pl_ent_tautology_iff
method: informal
status: reviewed
dependencies:
- pl_ent_def
- pl_cls_tautology
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.317347Z'
schema_version: 1
---

נוכיח את שני הכיוונים על סמך הגדרת יחס הנביעה ב־`pl_ent_def` והגדרת הטאוטולוגיה ב־`pl_cls_tautology`, כאשר הרעיון המרכזי הוא ריקנות התנאי המוצב על ההשמות.

**כיוון $\Rightarrow$:** נניח $\emptyset \models \varphi$. לפי `pl_ent_def`, לכל השמה $v$ (במובן של `pl_sem_valuation`) המקיימת $v(\psi) = T$ עבור כל $\psi \in \emptyset$ מתקיים $v(\varphi) = T$. אולם בקבוצה הריקה אין כלל נוסחאות, ולכן התנאי "$v(\psi) = T$ לכל $\psi \in \emptyset$" מתקיים באופן ריק לכל השמה $v$. משמע, לכל השמה $v$ מתקיים $v(\varphi) = T$. לפי `pl_cls_tautology`, נוסחה שערכה $T$ תחת כל השמה היא טאוטולוגיה, ולכן $\varphi$ טאוטולוגיה.

**כיוון $\Leftarrow$:** נניח ש־$\varphi$ טאוטולוגיה. לפי `pl_cls_tautology`, לכל השמה $v$ מתקיים $v(\varphi) = T$. בפרט, זה נכון גם לכל השמה $v$ שמספקת את כל נוסחאות $\emptyset$ — וכפי שראינו, כל השמה עונה על תנאי ריק זה. לכן לפי `pl_ent_def` מתקיים $\emptyset \models \varphi$.

משילוב שני הכיוונים: $\emptyset \models \varphi$ אם ורק אם $\varphi$ טאוטולוגיה.
