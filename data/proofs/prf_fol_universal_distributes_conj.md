---
id: prf_fol_universal_distributes_conj
claim_id: fol_universal_distributes_conj
method: informal
status: reviewed
dependencies:
- fol_universal_quantifier
- fol_equivalence
- pl_sem_clause_conj
is_canonical: true
date_added: '2026-07-10T20:41:42.982246Z'
schema_version: 1
---

יהי $D$ תחום דיון.

**כיוון $\Rightarrow$:** נניח $\forall x \, (\varphi(x) \wedge \psi(x)) = T$. אזי לכל $a \in D$ מתקיים $\varphi(a) \wedge \psi(a) = T$, וממנו לפי pl_sem_clause_conj $\varphi(a) = T$ וגם $\psi(a) = T$. לפי fol_universal_quantifier, $\forall x \, \varphi(x) = T$ וגם $\forall x \, \psi(x) = T$, ולכן $(\forall x \, \varphi(x)) \wedge (\forall x \, \psi(x)) = T$.

**כיוון $\Leftarrow$:** נניח $(\forall x \, \varphi(x)) \wedge (\forall x \, \psi(x)) = T$. לפי pl_sem_clause_conj, $\forall x \, \varphi(x) = T$ וגם $\forall x \, \psi(x) = T$. לפי fol_universal_quantifier, לכל $a \in D$ מתקיימים $\varphi(a) = T$ ו-$\psi(a) = T$, ולכן לכל $a \in D$ מתקיים $\varphi(a) \wedge \psi(a) = T$. שוב לפי fol_universal_quantifier, $\forall x \, (\varphi(x) \wedge \psi(x)) = T$.

מכיוון ששני הכיוונים תקפים תחת כל תחום ופרשנות, קיבלנו שקילות לוגית לפי fol_equivalence. $\blacksquare$
