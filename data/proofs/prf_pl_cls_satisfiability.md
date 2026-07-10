---
id: prf_pl_cls_satisfiability
claim_id: pl_cls_satisfiability
method: informal
status: reviewed
dependencies:
- pl_sem_valuation
- pl_cls_contradiction
- pl_syn_wff
- pl_cls_tautology
- pl_cls_contingency
is_canonical: true
date_added: '2026-07-10T20:18:36.239845Z'
schema_version: 1
---

ספיקות היא דרישה חלשה מטאוטולוגיה: 'קיים עולם המאמת את $\varphi$' לעומת 'כל העולמות מאמתים את $\varphi$'. יש להוכיח את השקילות '$\varphi$ ספיקה $\iff$ $\varphi$ אינה סתירה'. לפי `pl_cls_contradiction`, $\varphi$ סתירה פירושו $\forall v.\; v(\varphi) = F$. שלילת פסוק זה היא בדיוק $\exists v.\; v(\varphi) = T$, שהיא הגדרת הספיקות. יחסי ההכלה בין המחלקות שהוגדרו קודם (`pl_cls_tautology`, `pl_cls_contradiction`, `pl_cls_contingency`) הם: כל טאוטולוגיה ספיקה (בחר $v$ כלשהי מהמשפחה הלא־ריקה של השמות מעל $\mathrm{WFF}$; ראו `pl_sem_valuation`, `pl_syn_wff`); כל קונטינגנציה ספיקה (מההגדרה יש $v_1$ עם $v_1(\varphi) = T$); סתירה אינה ספיקה. לכן אוסף הנוסחאות הספיקות הוא בדיוק האיחוד של הטאוטולוגיות והקונטינגנציות, ומחלקת הנוסחאות הבלתי־ספיקות זהה למחלקת הסתירות. בעיית ה־SAT — בהינתן $\varphi$, האם היא ספיקה — היא בעיה $\mathrm{NP}$־שלמה קלאסית ומהווה יעד מרכזי במדעי המחשב היישומיים והתיאורטיים.
