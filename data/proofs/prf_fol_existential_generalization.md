---
id: prf_fol_existential_generalization
claim_id: fol_existential_generalization
method: informal
status: reviewed
dependencies:
- fol_existential_quantifier
- pl_ent_def
is_canonical: true
date_added: '2026-07-10T20:41:42.990745Z'
schema_version: 1
---

יהי $a \in D$. נניח שנתונה ערכוב $v$ עם $v(\varphi(a)) = T$. אזי בפרט קיים אבר בתחום הדיון (הוא $a$ עצמו) שמקיים את הפרדיקט, ולפי fol_existential_quantifier מתקיים $v(\exists x \, \varphi(x)) = T$. בכל ערכוב בו הצד השמאלי אמת גם הימני אמת, ולפי pl_ent_def זו הגדרת הגרירה הסמנטית. $\blacksquare$
