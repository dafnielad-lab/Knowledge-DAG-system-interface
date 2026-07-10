---
id: prf_pl_cmp_standard
claim_id: pl_cmp_standard
method: informal
status: reviewed
dependencies:
- pl_cmp_def
- pl_nrm_dnf_existence
- pl_nrm_dnf_def
- pl_nrm_literal
- pl_sem_truth_table
- pl_sem_clause_conj
- pl_sem_clause_neg
- pl_sem_clause_disj
is_canonical: true
date_added: '2026-07-10T20:18:36.368846Z'
schema_version: 1
---

נראה שעבור כל פונקציה בוליאנית קיימת נוסחה מייצגת שקשריה נלקחים מ־$\{\neg, \wedge, \vee\}$; לפי `pl_cmp_def` יקבע הדבר את שלמות הקבוצה.

תהי $f : \{T, F\}^n \to \{T, F\}$ פונקציה בוליאנית שרירותית. נתבונן בטבלת האמת שלה (`pl_sem_truth_table`), ונסמן ב־$V$ את קבוצת ההשמות $v$ ל־$p_1, \ldots, p_n$ שעבורן $f(v(p_1), \ldots, v(p_n)) = T$.

**מקרה 1:** $V = \emptyset$ ($f$ קבועה $F$). ניקח $\varphi := p_1 \wedge \neg p_1$. לפי `pl_sem_clause_conj` ו־`pl_sem_clause_neg` מתקיים $v(\varphi) = F$ בכל השמה, כדרוש. הנוסחה בנויה מ־$\{\neg, \wedge\} \subseteq \{\neg, \wedge, \vee\}$.

**מקרה 2:** $V \ne \emptyset$. נבנה נוסחה ב־DNF בדיוק כמו בהוכחת `pl_nrm_dnf_existence`: לכל $v \in V$ ניצור מונומיאל מלא
$$C_v := \bigwedge_{k=1}^{n} \ell_k^v,$$
כאשר $\ell_k^v = p_k$ אם $v(p_k) = T$ ו־$\ell_k^v = \neg p_k$ אם $v(p_k) = F$. כל ליטרל (`pl_nrm_literal`) בנוי בעזרת $\neg$ בלבד; המונומיאלים בעזרת $\wedge$; והדיסיונקציה $\varphi := \bigvee_{v \in V} C_v$ בעזרת $\vee$. ה־DNF (`pl_nrm_dnf_def`) שהתקבלה משתמשת אך ורק בקשרים $\{\neg, \wedge, \vee\}$.

מן ההוכחה של `pl_nrm_dnf_existence` נובע ש־$v'(\varphi) = T$ אם ורק אם $v' \in V$, כלומר אם ורק אם $f(v'(p_1), \ldots, v'(p_n)) = T$. לכן $\varphi$ מייצגת את $f$.

בשני המקרים בנינו עבור $f$ שרירותית נוסחה מייצגת ב־$\{\neg, \wedge, \vee\}$; לפי `pl_cmp_def` הקבוצה שלמה פונקציונלית. $\blacksquare$
