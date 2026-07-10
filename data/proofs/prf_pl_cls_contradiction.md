---
id: prf_pl_cls_contradiction
claim_id: pl_cls_contradiction
method: informal
status: reviewed
dependencies:
- pl_cls_tautology
- pl_sem_clause_neg
- pl_sem_valuation
- pl_syn_wff
is_canonical: true
date_added: '2026-07-10T20:18:36.232844Z'
schema_version: 1
---

סתירה היא ההיפך הסמנטי של טאוטולוגיה: נוסחה שאיננה יכולה להיות אמיתית תחת שום השמה. יש להראות את השקילות הנטענת בהגדרה — '$\varphi$ סתירה' שקול ל-'$\neg\varphi$ טאוטולוגיה'. יהיו $v$ השמה שרירותית מעל $\varphi \in \mathrm{WFF}$ (`pl_syn_wff`, `pl_sem_valuation`). לפי סעיף הסמנטיקה של השלילה (`pl_sem_clause_neg`) מתקיים $v(\neg\varphi) = T \iff v(\varphi) = F$. לכן: 'לכל $v$, $v(\varphi) = F$' שקול ל-'לכל $v$, $v(\neg\varphi) = T$', שהוא בדיוק $\models \neg\varphi$ לפי `pl_cls_tautology`. בכיוון ההפוך, מ-$\models \neg\varphi$ נובע $v(\neg\varphi) = T$ לכל $v$, ולכן $v(\varphi) = F$ לכל $v$. דוגמאות: $p \land \neg p$, $\neg(p \rightarrow p)$, $(p \lor q) \land \neg p \land \neg q$. הסתירות ממלאות תפקיד מפתח בשיטת ההוכחה בדרך השלילה: אם מהנחה $H$ נובעת סתירה $\bot$, נסיק $\neg H$.
