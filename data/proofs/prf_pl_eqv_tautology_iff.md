---
id: prf_pl_eqv_tautology_iff
claim_id: pl_eqv_tautology_iff
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_cls_tautology
- pl_sem_clause_bicond
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:41:42.954744Z'
schema_version: 1
---

המשפט הוא גשר בין המושג התחבירי-סמנטי של שקילות (זהות ערכי אמת בכל הצבה) לבין המושג היחיד של טאוטולוגיה (נכונות בכל הצבה).

**כיוון ראשון: אם $\varphi \equiv \psi$ אז $\varphi \leftrightarrow \psi$ טאוטולוגיה.** נניח $\varphi \equiv \psi$. לפי pl_eqv_def, זה אומר שלכל ערכוב $v$ מתקיים $v(\varphi) = v(\psi)$. לפי pl_sem_clause_bicond, $v(\varphi \leftrightarrow \psi) = T$ אם ורק אם $v(\varphi) = v(\psi)$. כלומר, לכל ערכוב $v$ מתקיים $v(\varphi \leftrightarrow \psi) = T$. לפי pl_cls_tautology, הנוסחה $\varphi \leftrightarrow \psi$ טאוטולוגיה.

**כיוון שני: אם $\varphi \leftrightarrow \psi$ טאוטולוגיה אז $\varphi \equiv \psi$.** נניח ש-$\varphi \leftrightarrow \psi$ טאוטולוגיה. אזי לכל ערכוב $v$ מתקיים $v(\varphi \leftrightarrow \psi) = T$, ולפי pl_sem_clause_bicond זה שקול ל-$v(\varphi) = v(\psi)$. אבל זהו בדיוק תנאי השקילות (pl_eqv_def), ולכן $\varphi \equiv \psi$.

משני הכיוונים יחד, $\varphi \equiv \psi \Leftrightarrow \models (\varphi \leftrightarrow \psi)$. $\blacksquare$
