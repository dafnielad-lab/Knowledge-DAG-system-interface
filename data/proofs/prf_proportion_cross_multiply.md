---
id: prf_proportion_cross_multiply
claim_id: thm_proportion_cross_multiply
method: informal
status: reviewed
dependencies:
- def_proportion
- def_fraction
- ax_multiplicative_inverse
- ax_multiplication_associativity
- ax_multiplication_commutativity
is_canonical: true
date_added: '2026-06-28T15:49:27.776204Z'
schema_version: 1
---

נניח שמתקיימת הפרופורציה $\frac{a}{b} = \frac{c}{d}$ עם $b, d \neq 0$, לפי `def_proportion`.

**שלב 1 — פתיחת הגדרת השבר:** לפי `def_fraction`, מתקיים $\frac{a}{b} = a \cdot b^{-1}$ ו-$\frac{c}{d} = c \cdot d^{-1}$. לכן שוויון הפרופורציה שקול לכך:
$$ a \cdot b^{-1} = c \cdot d^{-1} $$

**שלב 2 — כפל בשני האגפים:** נכפול את שני אגפי השוויון ב-$b \cdot d$ (גורם זה שונה מאפס משום ש-$b \neq 0$ ו-$d \neq 0$, ולכן הכפל הוא פעולה הפיכה). נקבל:
$$ (a \cdot b^{-1}) \cdot (b \cdot d) = (c \cdot d^{-1}) \cdot (b \cdot d) $$

**שלב 3 — סידור באמצעות אסוציאטיביות וקומוטטיביות:** באגף שמאל, נשתמש בקומוטטיביות (`ax_multiplication_commutativity`) ובאסוציאטיביות (`ax_multiplication_associativity`):
$$ (a \cdot b^{-1}) \cdot (b \cdot d) = a \cdot (b^{-1} \cdot b) \cdot d $$
ולפי איבר הפכי לכפל (`ax_multiplicative_inverse`), $b^{-1} \cdot b = 1$, ולכן:
$$ a \cdot 1 \cdot d = a \cdot d $$

באגף ימין באופן דומה:
$$ (c \cdot d^{-1}) \cdot (b \cdot d) = c \cdot b \cdot (d^{-1} \cdot d) = c \cdot b \cdot 1 = c \cdot b $$
ולפי קומוטטיביות הכפל, $c \cdot b = b \cdot c$.

**שלב 4 — שילוב:** קיבלנו $a \cdot d = b \cdot c$, כנדרש.

**הערה:** טכניקה זו, הקרויה "כפל הצלבי", מאפשרת לפתור פרופורציות ולחלץ נעלם. אם ידועים שלושה מתוך ארבעת הערכים $a, b, c, d$ והקצוות $b, d$ שונים מאפס, ניתן לחלץ את הערך הרביעי. למשל אם $\frac{x}{6} = \frac{2}{3}$, אז $3x = 12$ ומכאן $x = 4$. $\blacksquare$
