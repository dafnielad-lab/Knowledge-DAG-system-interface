---
id: prf_geometric_mean_leg_right_triangle
claim_id: thm_geometric_mean_leg_right_triangle
method: informal
status: reviewed
dependencies:
- def_right_triangle
- def_similar_triangles
- thm_aa_similarity
- thm_triangle_angle_sum
- def_proportion
is_canonical: true
date_added: '2026-06-28T20:34:16.534640Z'
schema_version: 1
---

נתון משולש $\triangle ABC$ עם $\angle ACB = 90°$ (לפי `def_right_triangle`); $CH$ הגובה ליתר $AB$, $H$ על $AB$, $\angle AHC = \angle BHC = 90°$. נסמן $a = BC$, $b = AC$, $c = AB$, $p = AH$, $q = HB$ (אז $p + q = c$).

**שלב 1 — דמיון $\triangle ACB \sim \triangle AHC$.** במשולשים אלו:
- $\angle A$ משותפת.
- $\angle ACB = 90° = \angle AHC$.

לפי `thm_aa_similarity` (AA) $\triangle ACB \sim \triangle AHC$.

ההתאמה בין הקודקודים: $A \leftrightarrow A$, $C \leftrightarrow H$, $B \leftrightarrow C$ (כי $\angle ACB$ ב-$\triangle ACB$ מתאימה ל-$\angle AHC$ ב-$\triangle AHC$, ו-$\angle A$ משותפת — לכן הקודקודים שמולן הזוויות הן $B$ ו-$C$ בהתאמה).

נוודא בקצרה את הזווית השלישית: סכום הזוויות במשולש הוא $180°$ (`thm_triangle_angle_sum`), אז $\angle ABC = 180° - 90° - \angle A$ במשולש המקורי, ובאופן זהה $\angle ACH = 180° - 90° - \angle A$ במשולש המשנה. ולכן $\angle ABC = \angle ACH$, מה שמאמת את ההתאמה.

**שלב 2 — יחס פרופורציונלי המגדיר את $b$.** לפי `def_similar_triangles`, הצלעות המתאימות בדמיון פרופורציונליות. ההתאמה $A \leftrightarrow A$, $C \leftrightarrow H$, $B \leftrightarrow C$ נותנת התאמה בין הצלעות:
- $AC \leftrightarrow AH$ (שתיהן הצלע בין הקודקוד הראשון לשני בהתאמה),
- $AB \leftrightarrow AC$ (שתיהן הצלע בין הקודקוד הראשון לשלישי בהתאמה),
- $CB \leftrightarrow HC$.

ולכן לפי `def_proportion`:
$$\frac{AC}{AH} = \frac{AB}{AC}.$$
כלומר $\dfrac{b}{p} = \dfrac{c}{b}$. כפל מצולב: $b^2 = c \cdot p$, כלומר $b = \sqrt{c \, p}$.

**שלב 3 — דמיון $\triangle ACB \sim \triangle CHB$ והיחס המגדיר את $a$.** במשולשים אלו:
- $\angle B$ משותפת.
- $\angle ACB = 90° = \angle CHB$.

לפי `thm_aa_similarity` $\triangle ACB \sim \triangle CHB$, עם ההתאמה $A \leftrightarrow C$, $C \leftrightarrow H$, $B \leftrightarrow B$.

לפי `def_similar_triangles` ו-`def_proportion`, היחסים המתאימים:
$$\frac{CB}{HB} = \frac{AB}{CB}.$$
כלומר $\dfrac{a}{q} = \dfrac{c}{a}$. כפל מצולב: $a^2 = c \cdot q$, כלומר $a = \sqrt{c \, q}$.

**שלב 4 — אחידות.** קיבלנו את שתי הזהויות:
$$b^2 = c \cdot p, \qquad a^2 = c \cdot q.$$
כל ניצב הוא הממוצע הגיאומטרי של היתר ושל היטלו על היתר.

**הערה — קשר לפיתגורס.** חיבור שתי הזהויות נותן בדיקת עקיבות: $a^2 + b^2 = c(p + q) = c \cdot c = c^2$, בהתאם למשפט פיתגורס. $\blacksquare$
