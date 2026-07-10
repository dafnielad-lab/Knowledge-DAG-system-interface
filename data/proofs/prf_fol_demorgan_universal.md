---
id: prf_fol_demorgan_universal
claim_id: fol_demorgan_universal
method: informal
status: reviewed
dependencies:
- fol_universal_quantifier
- fol_existential_quantifier
- fol_equivalence
- pl_sem_clause_neg
is_canonical: true
date_added: '2026-07-10T20:41:42.970745Z'
schema_version: 1
---

יהי $D$ תחום דיון וקבועה פרשנות כלשהי של $\varphi$. נסמן ב-$v$ את הערכוב. נראה שלכל תחום ופרשנות, ערך שתי הנוסחאות זהה.

$v(\neg \forall x \, \varphi(x)) = T$ אם ורק אם $v(\forall x \, \varphi(x)) = F$ (לפי pl_sem_clause_neg).

לפי fol_universal_quantifier, $v(\forall x \, \varphi(x)) = F$ אם ורק אם קיים $a \in D$ עם $v(\varphi(a)) = F$, כלומר $v(\neg \varphi(a)) = T$ (שוב pl_sem_clause_neg).

לפי fol_existential_quantifier, קיום כזה של $a \in D$ עם $v(\neg \varphi(a)) = T$ הוא בדיוק תנאי האמת של $\exists x \, \neg \varphi(x)$: $v(\exists x \, \neg \varphi(x)) = T$.

הראינו: $v(\neg \forall x \, \varphi(x)) = T \Leftrightarrow v(\exists x \, \neg \varphi(x)) = T$. שני האגפים מקבלים אותו ערך תחת כל תחום ופרשנות, ולפי fol_equivalence הם שקולים לוגית. $\blacksquare$
