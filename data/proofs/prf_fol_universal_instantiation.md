---
id: prf_fol_universal_instantiation
claim_id: fol_universal_instantiation
method: informal
status: reviewed
dependencies:
- fol_universal_quantifier
- pl_ent_def
is_canonical: true
date_added: '2026-07-10T20:41:42.987737Z'
schema_version: 1
---

יהי $a \in D$ אבר קבוע כלשהו. נניח שנתונה $v$ עם $v(\forall x \, \varphi(x)) = T$. לפי fol_universal_quantifier זה אומר שלכל $b \in D$ מתקיים $v(\varphi(b)) = T$, ובפרט $v(\varphi(a)) = T$. הראינו שבכל ערכוב בו הצד השמאלי אמת, גם הימני אמת, ולפי pl_ent_def זו בדיוק הגדרת הגרירה הסמנטית $\forall x \, \varphi(x) \models \varphi(a)$. $\blacksquare$
