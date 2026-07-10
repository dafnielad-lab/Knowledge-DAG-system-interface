---
id: prf_pl_nrm_dnf_existence
claim_id: pl_nrm_dnf_existence
method: informal
status: reviewed
dependencies:
- pl_nrm_dnf_def
- pl_nrm_literal
- pl_sem_truth_table
- pl_sem_valuation
- pl_sem_clause_conj
- pl_sem_clause_disj
- pl_sem_clause_neg
- pl_eqv_def
- pl_cls_contradiction
is_canonical: true
date_added: '2026-07-10T20:18:36.360346Z'
schema_version: 1
---

תהי $\varphi$ נוסחה במשתנים $p_1, \ldots, p_n$. נבנה את $\varphi'$ מתוך טבלת האמת של $\varphi$ (`pl_sem_truth_table`). נסמן ב־$V$ את קבוצת ההשמות $v : \{p_1, \ldots, p_n\} \to \{T, F\}$ (`pl_sem_valuation`) שעבורן $v(\varphi) = T$.

**מקרה 1:** $V = \emptyset$. אזי $\varphi$ סתירה (`pl_cls_contradiction`). ניקח $\varphi' := p_1 \wedge \neg p_1$, שהיא נוסחה ב־DNF (`pl_nrm_dnf_def`, עם $m = 1$ וקוניונקציה של שני ליטרלים) המקבלת $F$ בכל השמה, ולכן שקולה ל־$\varphi$ לפי `pl_eqv_def`.

**מקרה 2:** $V \ne \emptyset$. לכל $v \in V$ נגדיר את המונומיאל המלא
$$C_v := \bigwedge_{k=1}^{n} \ell_k^v, \qquad \ell_k^v := \begin{cases} p_k & v(p_k) = T \\ \neg p_k & v(p_k) = F \end{cases}$$
כל $\ell_k^v$ הוא ליטרל (`pl_nrm_literal`), אז $C_v$ קוניונקציה של ליטרלים. מסמנטיקת השלילה והקוניונקציה (`pl_sem_clause_neg`, `pl_sem_clause_conj`) מקבלים שלכל השמה $u$: $u(C_v) = T$ אם ורק אם $u$ מסכימה עם $v$ בכל המשתנים, כלומר $u = v$.

נגדיר $\varphi' := \bigvee_{v \in V} C_v$. זו נוסחה ב־DNF (`pl_nrm_dnf_def`). לפי סמנטיקת הדיסיונקציה (`pl_sem_clause_disj`) עבור השמה שרירותית $u$:
$$u(\varphi') = T \iff \exists v \in V : u(C_v) = T \iff u \in V \iff u(\varphi) = T.$$
לכן לפי `pl_eqv_def` מתקיים $\varphi \equiv \varphi'$, כדרוש. $\blacksquare$
