---
id: prf_expected_value_product_independent
claim_id: thm_expected_value_product_independent
method: informal
status: reviewed
dependencies:
- def_expected_value
- def_independent_random_variables
- def_discrete_random_variable
- thm_expected_value_of_function
is_canonical: true
date_added: '2026-06-28T15:07:55.467550Z'
schema_version: 1
---

נוכיח את הטענה במקרה הבדיד; ההוכחה במקרה הרציף זהה לחלוטין כשמחליפים סכומים באינטגרלים וערכי הסתברות בצפיפויות.

יהיו $X, Y$ משתנים מקריים בדידים עם טווחים $\{x_i\}$ ו-$\{y_j\}$ בהתאמה (לפי `def_discrete_random_variable`). נסמן את ההתפלגות המשותפת $p_{ij} = P(X = x_i,\ Y = y_j)$.

**שלב 1 — נוסחת תוחלת של פונקציה דו-משתנית.** המכפלה $XY$ היא פונקציה $g(X, Y) = XY$ של הזוג $(X, Y)$. לפי `thm_expected_value_of_function` (בהרחבתו הטבעית לזוג משתנים, שבה הסכימה היא על כל הזוגות בטווח המשותף):
$$E[XY] = \sum_{i}\sum_{j} x_i\, y_j \cdot P(X = x_i,\ Y = y_j) = \sum_i \sum_j x_i\, y_j\, p_{ij}.$$

**שלב 2 — שימוש באי-תלות לפירוק ההתפלגות המשותפת.** מתוך `def_independent_random_variables` נובע ששוויון הפילוגים המצטברים גורר $P(X = x_i,\ Y = y_j) = P(X = x_i)\cdot P(Y = y_j)$ לכל $i, j$ (זהו ניסוח שקול לאי-תלות עבור משתנים בדידים, המתקבל מהפרשי פונקציות ההתפלגות הצוברת). נציב:
$$E[XY] = \sum_i \sum_j x_i\, y_j\, P(X = x_i)\, P(Y = y_j).$$

**שלב 3 — הפרדת הסכומים.** הגורם $x_i\, P(X = x_i)$ אינו תלוי ב-$j$, והגורם $y_j\, P(Y = y_j)$ אינו תלוי ב-$i$. לכן, על-פי דיסטריבוטיביות של כפל מעל סכום סופי (ובמקרה האין-סופי תוך שימוש בהתכנסות מוחלטת המובטחת מסופיות התוחלות):
$$E[XY] = \sum_i \Big( x_i\, P(X = x_i) \sum_j y_j\, P(Y = y_j) \Big) = \Big( \sum_i x_i\, P(X = x_i) \Big) \cdot \Big( \sum_j y_j\, P(Y = y_j) \Big).$$

**שלב 4 — זיהוי התוחלות.** לפי `def_expected_value`, $\sum_i x_i\, P(X = x_i) = E[X]$ ו-$\sum_j y_j\, P(Y = y_j) = E[Y]$. לפיכך
$$E[XY] = E[X] \cdot E[Y]. \quad \blacksquare$$
