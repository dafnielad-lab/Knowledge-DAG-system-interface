---
id: prf_fol_demorgan_existential
claim_id: fol_demorgan_existential
method: informal
status: reviewed
dependencies:
- fol_universal_quantifier
- fol_existential_quantifier
- fol_equivalence
- pl_sem_clause_neg
is_canonical: true
date_added: '2026-07-10T20:41:42.973245Z'
schema_version: 1
---

יהי $D$ תחום דיון וקבועה פרשנות. נסמן ב-$v$ את הערכוב.

$v(\neg \exists x \, \varphi(x)) = T$ אם ורק אם $v(\exists x \, \varphi(x)) = F$ (pl_sem_clause_neg).

לפי fol_existential_quantifier, $v(\exists x \, \varphi(x)) = F$ אם ורק אם לכל $a \in D$ מתקיים $v(\varphi(a)) = F$, כלומר לכל $a \in D$ מתקיים $v(\neg \varphi(a)) = T$.

לפי fol_universal_quantifier, זה בדיוק תנאי האמת של $\forall x \, \neg \varphi(x)$: $v(\forall x \, \neg \varphi(x)) = T$.

הראינו: $v(\neg \exists x \, \varphi(x)) = T \Leftrightarrow v(\forall x \, \neg \varphi(x)) = T$ עבור כל תחום ופרשנות. לפי fol_equivalence הנוסחאות שקולות. $\blacksquare$

**הערה:** ניתן לגזור משפט זה גם מ-fol_demorgan_universal על ידי הצבת $\neg \varphi$ במקום $\varphi$ ושימוש בשלילה כפולה, אך ההוכחה הישירה קצרה ומקבילה.
