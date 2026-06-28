---
id: prf_geometric_mean_altitude_right_triangle
claim_id: thm_geometric_mean_altitude_right_triangle
method: informal
status: reviewed
dependencies:
- def_right_triangle
- def_similar_triangles
- thm_aa_similarity
- thm_triangle_angle_sum
- def_proportion
is_canonical: true
date_added: '2026-06-28T20:34:16.531624Z'
schema_version: 1
---

נתון משולש $\triangle ABC$ עם $\angle ACB = 90°$ (לפי `def_right_triangle`). $CH$ הוא הגובה היורד מ-$C$ ליתר $AB$, כך ש-$\angle AHC = \angle BHC = 90°$. נסמן $p = AH$, $q = HB$, $h = CH$.

**שלב 1 — שני משולשי משנה דומים למקורי.** נבחן את שלושת המשולשים $\triangle ACB$ (המקורי), $\triangle AHC$ ו-$\triangle CHB$.

במשולשים $\triangle ACB$ ו-$\triangle AHC$:
- $\angle A$ משותפת לשניהם.
- $\angle ACB = 90° = \angle AHC$.

לפי `thm_aa_similarity` (קריטריון AA — שתי זוויות שוות גוררות דמיון) נקבל $\triangle ACB \sim \triangle AHC$.

באופן דומה, במשולשים $\triangle ACB$ ו-$\triangle CHB$:
- $\angle B$ משותפת.
- $\angle ACB = 90° = \angle CHB$.

ולכן לפי `thm_aa_similarity` גם $\triangle ACB \sim \triangle CHB$.

מ"דמיון הוא יחס טרנזיטיבי" (או ישירות מכך ששתי המשולשים דומים לאותו משולש שלישי) נקבל
$$\triangle AHC \sim \triangle CHB.$$

**שלב 2 — בדיקת ההתאמה בין הקודקודים.** בדמיון $\triangle AHC \sim \triangle CHB$ ההתאמה היא $A \leftrightarrow C$, $H \leftrightarrow H$, $C \leftrightarrow B$. נוודא שהזוויות אכן מתאימות:
- ב-$\triangle AHC$ הזווית בקודקוד $H$ היא $90°$. ב-$\triangle CHB$ הזווית בקודקוד $H$ היא $90°$. שוויון.
- הזווית $\angle HAC$ ב-$\triangle AHC$ — נסמנה $\alpha$. במשולש $\triangle ACB$ סכום הזוויות הוא $180°$ (לפי `thm_triangle_angle_sum`), והזווית בקודקוד $C$ היא $90°$, אז $\angle A + \angle B = 90°$, כלומר $\angle B = 90° - \alpha$. במשולש $\triangle CHB$ הזווית בקודקוד $C$ (היא $\angle HCB$) ניתנת לחישוב: $\angle HCB = 90° - \angle B = 90° - (90° - \alpha) = \alpha$. כלומר הזווית בקודקוד $C$ של $\triangle CHB$ שווה ל-$\alpha$, כפי שצריך להיות לפי ההתאמה.
- הזווית בקודקוד $C$ של $\triangle AHC$ היא $\angle ACH = 90° - \alpha$. הזווית בקודקוד $B$ של $\triangle CHB$ היא $\angle B = 90° - \alpha$. שוויון.

ההתאמה נכונה.

**שלב 3 — יישום `def_similar_triangles` להפקת היחסים.** מן הדמיון $\triangle AHC \sim \triangle CHB$ עם ההתאמה הנ"ל, לפי `def_similar_triangles` הצלעות המתאימות פרופורציונליות. הצלעות המתאימות:
- מול הזווית של $90°$ (היפותנוזה של כל משולש משנה): ב-$\triangle AHC$ זו $AC$, ב-$\triangle CHB$ זו $CB$.
- מול הזווית $\alpha$: ב-$\triangle AHC$ זו הצלע מול $\angle A = \alpha$, היינו $HC = h$. ב-$\triangle CHB$ זו הצלע מול $\angle HCB = \alpha$, היינו $HB = q$.
- מול הזווית $90° - \alpha$: ב-$\triangle AHC$ זו $AH = p$ (מול $\angle ACH$). ב-$\triangle CHB$ זו $HC = h$ (מול $\angle B$).

לפי `def_proportion` היחסים שווים:
$$\frac{p}{h} = \frac{h}{q}.$$
כפל מצולב נותן $h \cdot h = p \cdot q$, כלומר
$$h^2 = p \cdot q.$$

לאחר הוצאת שורש חיובי (כי $h, p, q > 0$): $h = \sqrt{pq}$, כלומר $h$ הוא הממוצע הגיאומטרי של $p$ ו-$q$. $\blacksquare$
