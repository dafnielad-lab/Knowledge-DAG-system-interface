---
id: prf_pl_nrm_dnf_def
claim_id: pl_nrm_dnf_def
method: informal
status: reviewed
dependencies:
- pl_nrm_literal
- pl_syn_connectives
- pl_syn_wff
- pl_sem_clause_conj
- pl_sem_clause_disj
is_canonical: true
date_added: '2026-07-10T20:18:36.354346Z'
schema_version: 1
---

הצורה בנויה בשתי שכבות: השכבה הפנימית היא קוניונקציה של ליטרלים (`pl_nrm_literal`) בעזרת הקשר $\wedge$ (`pl_syn_connectives`), ומכונה לעיתים _מונומיאל_. השכבה החיצונית היא דיסיונקציה של המונומיאלים הללו בעזרת $\vee$. שני מקרי קצה נחשבים אף הם ל־DNF: קוניונקציה בודדת של ליטרלים היא DNF (עם $m=1$), וליטרל בודד הוא DNF (עם $m=1$ ו־$k_1=1$). המשמעות הסמנטית ברורה מסמנטיקת הקשרים (`pl_sem_clause_conj`, `pl_sem_clause_disj`): הערכת השמה $v$ נותנת $v(\varphi) = T$ אם ורק אם קיים לפחות אינדקס $i$ שעבורו כל הליטרלים $\ell_{i,1}, \ldots, \ell_{i, k_i}$ מקבלים $T$ תחת $v$. כלומר כל מונומיאל מתאר קבוצה של שורות בטבלת האמת שבהן הוא מסופק, וה־DNF מסופקת כאשר לפחות אחד מהם מסופק.
