---
id: prf_pl_cls_contingency
claim_id: pl_cls_contingency
method: informal
status: reviewed
dependencies:
- pl_cls_tautology
- pl_cls_contradiction
- pl_syn_wff
- pl_sem_valuation
is_canonical: true
date_added: '2026-07-10T20:18:36.236346Z'
schema_version: 1
---

ההגדרה מבוססת על שלילת שתי המחלקות הקודמות. לפי `pl_cls_tautology`, $\varphi$ טאוטולוגיה פירושו $\forall v.\; v(\varphi) = T$; שלילת פסוק זה היא $\exists v_2.\; v_2(\varphi) = F$. לפי `pl_cls_contradiction`, $\varphi$ סתירה פירושו $\forall v.\; v(\varphi) = F$; שלילת פסוק זה היא $\exists v_1.\; v_1(\varphi) = T$. הצירוף של שתי השלילות נותן בדיוק את התנאי המופיע בהגדרה. שלוש המחלקות — טאוטולוגיה, סתירה, קונטינגנציה — מהוות חלוקה ממצה וזרה של $\mathrm{WFF}$ (`pl_syn_wff`): לכל נוסחה $\varphi$, אוסף הערכים $\{v(\varphi) : v \text{ השמה}\}$ הוא תת־קבוצה לא ריקה של $\{T, F\}$, ולכן חייב להיות בדיוק אחד מבין $\{T\}$ (טאוטולוגיה), $\{F\}$ (סתירה), או $\{T, F\}$ (קונטינגנציה). בטבלת האמת: הטור המסכם של קונטינגנציה מכיל לפחות $T$ אחד ולפחות $F$ אחד. דוגמאות טיפוסיות: $p$, $p \rightarrow q$, $p \land q$, $p \lor q$. רוב הנוסחאות בעלות התוכן העובדתי בפועל הן קונטינגנציות: ערך האמת שלהן תלוי בפרטי העולם.
