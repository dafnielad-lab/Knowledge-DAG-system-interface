---
id: prf_pl_cmp_nand
claim_id: pl_cmp_nand
method: informal
status: reviewed
dependencies:
- pl_cmp_def
- pl_cmp_neg_conj
- pl_eqv_idem_conj
- pl_eqv_double_neg
- pl_eqv_substitution
- pl_eqv_def
is_canonical: true
date_added: '2026-07-10T20:18:36.377846Z'
schema_version: 1
---

האסטרטגיה: נביע את $\neg$ ואת $\wedge$ בעזרת $\uparrow$ בלבד; משלמות $\{\neg, \wedge\}$ (`pl_cmp_neg_conj`) תנבע שלמות $\{\uparrow\}$.

**שלב 1: ביטוי השלילה.** מהגדרת שרביט שפר, $p \uparrow p \equiv \neg(p \wedge p)$. לפי אידמפוטנטיות של קוניונקציה (`pl_eqv_idem_conj`) $p \wedge p \equiv p$, ולפי החלפת שקילויות (`pl_eqv_substitution`) $\neg(p \wedge p) \equiv \neg p$. לכן
$$p \uparrow p \equiv \neg p. \qquad (\dagger)$$

**שלב 2: ביטוי הקוניונקציה.** מהגדרת שרביט שפר, $(p \uparrow q) \uparrow (p \uparrow q) \equiv \neg\bigl((p \uparrow q) \wedge (p \uparrow q)\bigr)$. לפי `pl_eqv_idem_conj` מתקיים $(p \uparrow q) \wedge (p \uparrow q) \equiv (p \uparrow q)$, ולפי `pl_eqv_substitution`
$$(p \uparrow q) \uparrow (p \uparrow q) \equiv \neg(p \uparrow q) \equiv \neg \neg(p \wedge q) \equiv p \wedge q,$$
כאשר הצעד האחרון משתמש בכפילות השלילה (`pl_eqv_double_neg`) ו־`pl_eqv_substitution`. לכן
$$(p \uparrow q) \uparrow (p \uparrow q) \equiv p \wedge q. \qquad (\ddagger)$$

**שלב 3: שלמות פונקציונלית.** תהי $f$ פונקציה בוליאנית שרירותית. לפי `pl_cmp_neg_conj` קיימת נוסחה $\varphi$ המייצגת את $f$ שקשריה מ־$\{\neg, \wedge\}$ בלבד. מחליפים באופן איטרטיבי:
- כל תת־נוסחה מהצורה $\neg \alpha$ ב־$\alpha \uparrow \alpha$ (מוצדק על ידי $(\dagger)$ ו־`pl_eqv_substitution`);
- כל תת־נוסחה מהצורה $\alpha \wedge \beta$ ב־$(\alpha \uparrow \beta) \uparrow (\alpha \uparrow \beta)$ (מוצדק על ידי $(\ddagger)$ ו־`pl_eqv_substitution`).

התהליך מסתיים כי כל צעד מסלק לפחות מופע אחד של $\neg$ או $\wedge$. התוצאה $\varphi^*$ שקולה ל־$\varphi$ (`pl_eqv_def`, טרנזיטיביות), ולכן מייצגת את $f$; קשריה נלקחים כולם מ־$\{\uparrow\}$.

הראנו קיום נוסחה מתאימה עבור כל $f$; לפי `pl_cmp_def` הקבוצה $\{\uparrow\}$ שלמה פונקציונלית. תוצאה זו של שפר (1913) יוצאת דופן בכך שהיא מראה קשר בינארי _יחיד_ שממנו ניתן לבנות את כל הלוגיקה הפסוקית. $\blacksquare$
