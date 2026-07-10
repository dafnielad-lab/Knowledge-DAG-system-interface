---
id: prf_pl_cmp_neg_disj
claim_id: pl_cmp_neg_disj
method: informal
status: reviewed
dependencies:
- pl_cmp_def
- pl_cmp_standard
- pl_eqv_demorgan_disj
- pl_eqv_double_neg
- pl_eqv_substitution
- pl_eqv_def
is_canonical: true
date_added: '2026-07-10T20:18:36.374846Z'
schema_version: 1
---

ההוכחה דואלית להוכחת `pl_cmp_neg_conj`.

**שלב 1: ביטוי $\wedge$ בעזרת $\{\neg, \vee\}$.** לפי דה מורגן על דיסיונקציה (`pl_eqv_demorgan_disj`), $\neg(a \vee b) \equiv \neg a \wedge \neg b$. מציבים $a := \neg p$ ו־$b := \neg q$ ומקבלים
$$\neg(\neg p \vee \neg q) \equiv \neg \neg p \wedge \neg \neg q.$$
לפי כפילות השלילה (`pl_eqv_double_neg`) $\neg \neg p \equiv p$ ו־$\neg \neg q \equiv q$, ולפי `pl_eqv_substitution` הצד הימני שקול ל־$p \wedge q$. לכן
$$p \wedge q \equiv \neg(\neg p \vee \neg q). \qquad (**)$$

**שלב 2: שלמות פונקציונלית.** תהי $f$ פונקציה בוליאנית שרירותית. לפי `pl_cmp_standard` קיימת נוסחה $\varphi$ המייצגת את $f$ שקשריה מ־$\{\neg, \wedge, \vee\}$. מחליפים באופן איטרטיבי בכל תת־נוסחה מהצורה $\alpha \wedge \beta$ את הביטוי $\neg(\neg \alpha \vee \neg \beta)$; לפי (**) ולפי `pl_eqv_substitution`, כל צעד שומר על שקילות. התהליך מסתיים כי כל צעד מוריד מופע $\wedge$ אחד.

התוצאה $\varphi^*$ שקולה ל־$\varphi$ (`pl_eqv_def`) ומשתמשת אך ורק בקשרים $\{\neg, \vee\}$. לכן היא מייצגת את $f$ עם קשרים אלה בלבד.

הראנו קיום נוסחה מתאימה עבור כל $f$; לפי `pl_cmp_def` הקבוצה $\{\neg, \vee\}$ שלמה פונקציונלית. $\blacksquare$
