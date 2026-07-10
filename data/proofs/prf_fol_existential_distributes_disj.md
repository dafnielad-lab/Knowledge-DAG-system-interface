---
id: prf_fol_existential_distributes_disj
claim_id: fol_existential_distributes_disj
method: informal
status: reviewed
dependencies:
- fol_existential_quantifier
- fol_equivalence
- pl_sem_clause_disj
is_canonical: true
date_added: '2026-07-10T20:41:42.984745Z'
schema_version: 1
---

יהי $D$ תחום דיון.

**כיוון $\Rightarrow$:** נניח $\exists x \, (\varphi(x) \vee \psi(x)) = T$. אזי קיים $a \in D$ עם $\varphi(a) \vee \psi(a) = T$, ולפי pl_sem_clause_disj לפחות אחד מ-$\varphi(a) = T$ או $\psi(a) = T$. בלי הגבלת כלליות $\varphi(a) = T$. אז לפי fol_existential_quantifier, $\exists x \, \varphi(x) = T$, וממילא $(\exists x \, \varphi(x)) \vee (\exists x \, \psi(x)) = T$.

**כיוון $\Leftarrow$:** נניח $(\exists x \, \varphi(x)) \vee (\exists x \, \psi(x)) = T$. לפי pl_sem_clause_disj, לפחות אחד מהם אמת. בלי הגבלת כלליות $\exists x \, \varphi(x) = T$, ולפי fol_existential_quantifier קיים $a \in D$ עם $\varphi(a) = T$. אז $\varphi(a) \vee \psi(a) = T$, ושוב לפי fol_existential_quantifier $\exists x \, (\varphi(x) \vee \psi(x)) = T$.

לפי fol_equivalence, הצדדים שקולים לוגית. $\blacksquare$

**זהירות:** ההכללה 'הכמת הפרטי מתפלג על ה-AND' אינה תקפה: $\exists x \, (\varphi(x) \wedge \psi(x)) \not\equiv (\exists x \, \varphi(x)) \wedge (\exists x \, \psi(x))$ (השני יותר חלש — לא מבטיח אותו $x$ לשני הפרדיקטים).
