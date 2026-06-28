---
id: prf_sas_similarity
claim_id: thm_sas_similarity
method: informal
status: reviewed
dependencies:
- def_similar_triangles
- def_congruent_triangles
- def_proportion
- thm_aa_similarity
- ax_sas_congruence
- def_triangle
is_canonical: true
date_added: '2026-06-28T20:34:16.525623Z'
schema_version: 1
---

נתון $\triangle ABC$ ו-$\triangle A'B'C'$ עם $\dfrac{A'B'}{AB} = \dfrac{A'C'}{AC} = k$ ו-$\angle A = \angle A'$. נראה שהמשולשים דומים.

**שלב 1 — בניית עזר.** אם $k = 1$ אז לפי `def_proportion` מתקיים $A'B' = AB$ ו-$A'C' = AC$, ובצירוף $\angle A = \angle A'$ נקבל לפי `ax_sas_congruence` שהמשולשים חופפים. לפי `def_congruent_triangles` שני משולשים חופפים מקיימים גם את תנאי הדמיון (אורכים שווים והם פרופורציונליים ביחס $1$, וזוויות מתאימות שוות), ולכן הם דומים. נניח מעתה $k \neq 1$, ובפרט $k > 0$ כיחס אורכים חיוביים.

נניח לשם הנוחות $k > 1$ (במקרה $0 < k < 1$ נחליף את שמות המשולשים). על הצלע $A'B'$ נסמן נקודה $D$ כך ש-$A'D = AB$, ועל הצלע $A'C'$ נסמן נקודה $E$ כך ש-$A'E = AC$. הנקודות קיימות כי $A'B' = k \cdot AB > AB$ ו-$A'C' = k \cdot AC > AC$. נקבל לפי `def_triangle` משולש $\triangle A'DE$ פנימי למשולש $\triangle A'B'C'$.

**שלב 2 — חפיפה $\triangle ABC \cong \triangle A'DE$.** במשולשים $\triangle ABC$ ו-$\triangle A'DE$ מתקיים:
- $AB = A'D$ (לפי הבנייה),
- $AC = A'E$ (לפי הבנייה),
- $\angle A = \angle A'$ (הוא $\angle DA'E$, נתון).

לפי `ax_sas_congruence` (צ.ז.צ) נקבל $\triangle ABC \cong \triangle A'DE$. בפרט, לפי `def_congruent_triangles`, $\angle ABC = \angle A'DE$ ו-$\angle ACB = \angle A'ED$.

**שלב 3 — דמיון $\triangle A'DE \sim \triangle A'B'C'$.** נראה שהישר $DE$ מקביל לישר $B'C'$. נחשב יחסים: $\dfrac{A'D}{A'B'} = \dfrac{AB}{A'B'} = \dfrac{1}{k}$ (כי $A'B' = k \cdot AB$), ובאופן זהה $\dfrac{A'E}{A'C'} = \dfrac{AC}{A'C'} = \dfrac{1}{k}$. כלומר היחסים שווים, ולכן הקטע $DE$ "חוצה את שתי הצלעות באותו יחס". במצב כזה (משפט תאלס ההפוך, או באופן ישיר באמצעות `thm_aa_similarity` המוחל על המשולשים $\triangle A'DE$ ו-$\triangle A'B'C'$) מתקבל ש-$\triangle A'DE \sim \triangle A'B'C'$.

ליתר דיוק: במשולשים $\triangle A'DE$ ו-$\triangle A'B'C'$ הזווית $\angle A'$ משותפת, והצלעות הסמוכות לה פרופורציונליות עם יחס $\dfrac{1}{k}$. כדי לסיים את הטיעון רק עם AA, נשתמש בעובדה הבאה: אם בונים על קרן $A'B'$ נקודה $D$ ועל קרן $A'C'$ נקודה $E$ כך ש-$A'D = \dfrac{1}{k} A'B'$ ו-$A'E = \dfrac{1}{k} A'C'$, אזי הקטע $DE$ הוא תוצאה של הומותטיה במרכז $A'$ ויחס $\dfrac{1}{k}$ של הקטע $B'C'$, ולכן $DE \parallel B'C'$ והזוויות $\angle A'DE = \angle A'B'C'$ (זוויות מתאימות בין מקבילים). יחד עם הזווית המשותפת $\angle A'$ נקבל לפי `thm_aa_similarity` (AA) ש-$\triangle A'DE \sim \triangle A'B'C'$. לפי `def_similar_triangles` היחס בין הצלעות המתאימות הוא $\dfrac{1}{k}$, ובפרט $DE = \dfrac{1}{k} B'C'$, כלומר $B'C' = k \cdot DE$.

**שלב 4 — סיום.** מהחפיפה בשלב 2 נובע $BC = DE$. נצרף: $B'C' = k \cdot DE = k \cdot BC$, ולכן $\dfrac{B'C'}{BC} = k$. קיבלנו $\dfrac{A'B'}{AB} = \dfrac{A'C'}{AC} = \dfrac{B'C'}{BC} = k$, כלומר שלוש הצלעות פרופורציונליות לפי `def_proportion`. כמו כן, מן החפיפה בשלב 2 ומדמיון שלב 3 נובעות שיוויות כל הזוויות המתאימות: $\angle A = \angle A'$ (נתון), $\angle B = \angle A'DE = \angle A'B'C' = \angle B'$, ו-$\angle C = \angle A'ED = \angle A'C'B' = \angle C'$.

שני התנאים בהגדרת `def_similar_triangles` מתקיימים, ולכן $\triangle ABC \sim \triangle A'B'C'$ ויחס הדמיון הוא $k$. $\blacksquare$
