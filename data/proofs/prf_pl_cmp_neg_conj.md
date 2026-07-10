---
id: prf_pl_cmp_neg_conj
claim_id: pl_cmp_neg_conj
method: informal
status: reviewed
dependencies:
- pl_cmp_def
- pl_cmp_standard
- pl_eqv_demorgan_conj
- pl_eqv_double_neg
- pl_eqv_substitution
- pl_eqv_def
is_canonical: true
date_added: '2026-07-10T20:18:36.371848Z'
schema_version: 1
---

**שלב 1: ביטוי $\vee$ בעזרת $\{\neg, \wedge\}$.** לפי דה מורגן על קוניונקציה (`pl_eqv_demorgan_conj`) $\neg(a \wedge b) \equiv \neg a \vee \neg b$. מציבים $a := \neg p$ ו־$b := \neg q$ ומקבלים
$$\neg(\neg p \wedge \neg q) \equiv \neg \neg p \vee \neg \neg q.$$
לפי כפילות השלילה (`pl_eqv_double_neg`) $\neg \neg p \equiv p$ ו־$\neg \neg q \equiv q$, ולפי החלפת שקילויות (`pl_eqv_substitution`) הצד הימני שקול ל־$p \vee q$. לכן
$$p \vee q \equiv \neg(\neg p \wedge \neg q). \qquad (*)$$

**שלב 2: שלמות פונקציונלית.** תהי $f$ פונקציה בוליאנית שרירותית. לפי `pl_cmp_standard` קיימת נוסחה $\varphi$ המייצגת את $f$ שקשריה מ־$\{\neg, \wedge, \vee\}$. נבנה מ־$\varphi$ נוסחה $\varphi^*$ שקשריה מ־$\{\neg, \wedge\}$ בלבד באמצעות התהליך הבא: כל עוד ב־$\varphi$ מופיע $\vee$, נבחר תת־נוסחה מהצורה $\alpha \vee \beta$ ונחליף אותה ב־$\neg(\neg \alpha \wedge \neg \beta)$. לפי (*) ולפי `pl_eqv_substitution`, כל צעד החלפה שומר על שקילות. התהליך מסתיים לאחר מספר סופי של צעדים, כי כל צעד מוריד מופע $\vee$ אחד.

התוצאה $\varphi^*$ שקולה ל־$\varphi$ (`pl_eqv_def`, טרנזיטיביות של השקילויות), ולפיכך מייצגת את $f$; קשריה נלקחים כולם מ־$\{\neg, \wedge\}$.

הראנו קיום נוסחה מתאימה עבור כל $f$; לפי `pl_cmp_def` הקבוצה $\{\neg, \wedge\}$ שלמה פונקציונלית. $\blacksquare$
