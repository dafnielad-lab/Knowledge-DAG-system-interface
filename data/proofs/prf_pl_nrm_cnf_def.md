---
id: prf_pl_nrm_cnf_def
claim_id: pl_nrm_cnf_def
method: informal
status: reviewed
dependencies:
- pl_nrm_literal
- pl_syn_connectives
- pl_syn_wff
- pl_sem_clause_conj
- pl_sem_clause_disj
is_canonical: true
date_added: '2026-07-10T20:18:36.357346Z'
schema_version: 1
---

זו הצורה הדואלית ל־DNF (`pl_nrm_dnf_def`): השכבה הפנימית מדברת ב־$\vee$ והחיצונית ב־$\wedge$. כל דיסיונקציה של ליטרלים $\bigvee_{j} \ell_{i,j}$ נקראת _פסוקית_, וב־SAT ובאלגוריתמי רזולוציה זהו האובייקט המרכזי. הבנייה משתמשת בליטרלים (`pl_nrm_literal`) ובקשרים $\wedge, \vee$ (`pl_syn_connectives`), והתוצאה היא נוסחה תקינה (`pl_syn_wff`). מקרי הקצה מקבילים ל־DNF: פסוקית בודדת היא CNF, וליטרל בודד הוא CNF. סמנטית (`pl_sem_clause_conj`, `pl_sem_clause_disj`), הערכה $v$ נותנת $v(\varphi) = T$ אם ורק אם בכל אחת מהפסוקיות $\bigvee_{j} \ell_{i,j}$ יש לפחות ליטרל אחד ש־$v$ מספק. במילים אחרות, כל פסוקית מוציאה "אזור אסור" בטבלת האמת (השורות שבהן כל הליטרלים בפסוקית מקבלים $F$), וה־CNF מסופקת בדיוק בהשמות שנשארות אחרי חיתוך כל האזורים המותרים.
