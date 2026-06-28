---
id: prf_sss_similarity
claim_id: thm_sss_similarity
method: informal
status: reviewed
dependencies:
- def_similar_triangles
- def_congruent_triangles
- def_proportion
- thm_sas_similarity
- ax_sss_congruence
- def_triangle
is_canonical: true
date_added: '2026-06-28T20:34:16.528621Z'
schema_version: 1
---

נתון $\triangle ABC$ ו-$\triangle A'B'C'$ עם $\dfrac{A'B'}{AB} = \dfrac{B'C'}{BC} = \dfrac{A'C'}{AC} = k > 0$ (לפי `def_proportion`). נראה שהמשולשים דומים.

**מקרה $k = 1$.** במקרה זה כל הצלעות שוות בהתאמה: $A'B' = AB$, $B'C' = BC$, $A'C' = AC$. לפי `ax_sss_congruence` (צ.צ.צ) המשולשים חופפים, ולפי `def_congruent_triangles` יש בהם שוויון זוויות ושוויון אורכים — שני התנאים שב-`def_similar_triangles` מתקיימים (יחס דמיון $1$), והמשולשים דומים.

**מקרה $k \neq 1$.** נבנה משולש עזר $\triangle A''B''C''$ בעל אותן צלעות כמו $\triangle ABC$ מוכפלות ב-$k$: על קרן הוצאת מנקודה $A''$ נסמן נקודה $B''$ כך ש-$A''B'' = k \cdot AB = A'B'$. בזווית $\angle A'' = \angle A$ נסמן נקודה $C''$ כך ש-$A''C'' = k \cdot AC = A'C'$. לפי `def_triangle` קיים המשולש $\triangle A''B''C''$.

במשולשים $\triangle ABC$ ו-$\triangle A''B''C''$ הזווית $\angle A = \angle A''$ (לפי הבנייה), והצלעות הסמוכות לה מקיימות:
$$\dfrac{A''B''}{AB} = k = \dfrac{A''C''}{AC}.$$
לפי `thm_sas_similarity` (קריטריון דמיון SAS) המשולשים $\triangle ABC$ ו-$\triangle A''B''C''$ דומים עם יחס דמיון $k$. ולכן לפי `def_similar_triangles` הצלע השלישית מקיימת $B''C'' = k \cdot BC$.

**השוואה למשולש $\triangle A'B'C'$.** קיבלנו: $A''B'' = A'B' = k \cdot AB$, $A''C'' = A'C' = k \cdot AC$, ו-$B''C'' = k \cdot BC = B'C'$ (האחרון לפי הנתון $\dfrac{B'C'}{BC} = k$). שלוש הצלעות של $\triangle A''B''C''$ ו-$\triangle A'B'C'$ שוות בהתאמה, ולפי `ax_sss_congruence` המשולשים חופפים. לפי `def_congruent_triangles` כל הזוויות המתאימות שוות.

**סיום.** $\triangle ABC \sim \triangle A''B''C''$ (דמיון מקריטריון SAS) ו-$\triangle A''B''C'' \cong \triangle A'B'C'$ (חפיפה). דמיון משולשים הוא יחס שמש שמירת זוויות מתאימות (לפי `def_similar_triangles`) ופרופורציונליות צלעות; הרכבת דמיון ביחס $k$ עם חפיפה (דמיון ביחס $1$) נותנת דמיון ביחס $k$. לכן $\triangle ABC \sim \triangle A'B'C'$ ויחס הדמיון $k$. $\blacksquare$
