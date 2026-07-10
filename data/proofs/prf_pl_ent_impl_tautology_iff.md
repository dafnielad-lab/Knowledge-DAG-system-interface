---
id: prf_pl_ent_impl_tautology_iff
claim_id: pl_ent_impl_tautology_iff
method: informal
status: reviewed
dependencies:
- pl_ent_def
- pl_cls_tautology
- pl_sem_clause_impl
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:41:42.959244Z'
schema_version: 1
---

המשפט הוא גשר בין הגרירה הסמנטית (יחס בין נוסחאות) לבין תכונה סטנדרטית של נוסחה יחידה (טאוטולוגיה).

**כיוון ראשון: אם $\varphi \models \psi$ אז $\varphi \to \psi$ טאוטולוגיה.** נניח $\varphi \models \psi$. לפי pl_ent_def פירושו: בכל ערכוב $v$ שבו $v(\varphi) = T$ מתקיים גם $v(\psi) = T$. נראה שבכל ערכוב $v$ מתקיים $v(\varphi \to \psi) = T$. לפי pl_sem_clause_impl, $v(\varphi \to \psi) = F$ אך ורק כאשר $v(\varphi) = T$ ו-$v(\psi) = F$. אך זה חסום על ידי ההנחה: אם $v(\varphi) = T$ מתחייב $v(\psi) = T$. לכן המקרה $v(\varphi \to \psi) = F$ בלתי אפשרי, ולפי pl_cls_tautology הנוסחה $\varphi \to \psi$ טאוטולוגיה.

**כיוון שני: אם $\varphi \to \psi$ טאוטולוגיה אז $\varphi \models \psi$.** נניח ש-$\varphi \to \psi$ טאוטולוגיה. יהי $v$ ערכוב שרירותי שבו $v(\varphi) = T$. מטאוטולוגיות $v(\varphi \to \psi) = T$, ולפי pl_sem_clause_impl אפשרי רק $v(\psi) = T$ (המקרה $v(\varphi) = T, v(\psi) = F$ ייתן $v(\varphi \to \psi) = F$). זה בדיוק תנאי הגרירה הסמנטית ב-pl_ent_def.

משני הכיוונים יחד, $\varphi \models \psi \Leftrightarrow \models (\varphi \to \psi)$. $\blacksquare$

**הכללה לקבוצה סופית של הנחות:** מן המשפט וממטריאליות הכפייה (הכללה מקורית של הקוראים) נובע: לקבוצה סופית $\{\varphi_1, \ldots, \varphi_n\}$ מתקיים $\{\varphi_1, \ldots, \varphi_n\} \models \psi$ אם ורק אם $(\varphi_1 \wedge \cdots \wedge \varphi_n) \to \psi$ טאוטולוגיה.
