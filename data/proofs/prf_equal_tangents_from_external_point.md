---
id: prf_equal_tangents_from_external_point
claim_id: thm_equal_tangents_from_external_point
method: informal
status: reviewed
dependencies:
- def_circle
- def_circle_center
- def_circle_radius
- def_chord
- def_tangent_to_circle
- thm_tangent_perpendicular_to_radius
- def_right_triangle
- def_congruent_triangles
- ax_hl_congruence
- ax_sas_congruence
is_canonical: true
date_added: '2026-06-28T21:06:29.460178Z'
schema_version: 1
---

יהי מעגל ברדיוס $r$ שמרכזו $O$ (`def_circle`, `def_circle_center`, `def_circle_radius`), ותהי $P$ נקודה מחוץ למעגל. נניח ש-$PA$ ו-$PB$ הם שני משיקים למעגל (`def_tangent_to_circle`) מ-$P$, כאשר $A$ ו-$B$ נקודות ההשקה.

**צעד 1 — חפיפת המשולשים $\triangle OAP$ ו-$\triangle OBP$.**

לפי `thm_tangent_perpendicular_to_radius`, משיק למעגל מאונך לרדיוס בנקודת ההשקה. לכן $OA \perp PA$ ו-$OB \perp PB$. נובע ששני המשולשים $\triangle OAP$ ו-$\triangle OBP$ הם משולשים ישרי-זווית (`def_right_triangle`) — הזווית הישרה ב-$A$ וב-$B$ בהתאמה — והיתר בשניהם הוא $OP$ (הצלע שמול הזווית הישרה).

נשווה את שני המשולשים:
- **יתר משותף:** $OP = OP$.
- **ניצב שווה:** $OA = OB = r$ — שני רדיוסים של אותו מעגל (`def_circle_radius`).

לפי `ax_hl_congruence` (חפיפת יתר-ניצב במשולשים ישרי-זווית), $\triangle OAP \cong \triangle OBP$.

**צעד 2 — $PA = PB$ והקרן $PO$ חוצה את $\angle APB$.**

מהגדרת חפיפת משולשים (`def_congruent_triangles`) נובע ששאר הצלעות והזוויות המתאימות שוות. בפרט:
- $PA = PB$ — הניצבים השניים מתאימים זה לזה בחפיפה. זוהי הטענה המרכזית.
- $\angle APO = \angle BPO$ — הזוויות שב-$P$ מתאימות זו לזו. לכן הקרן $PO$ היא חוצה הזווית $\angle APB$.
- $\angle AOP = \angle BOP$ — הזוויות שב-$O$ מתאימות זו לזו. נסמן $\angle AOP = \angle BOP = \alpha$.

**צעד 3 — $OP$ מאונך ל-$AB$ וחוצה אותו (גזירה ישירה ב-SAS).**

הקטע $AB$ הוא מיתר במעגל (`def_chord`). תהי $M$ נקודת החיתוך של הקטע $OP$ עם הקטע $AB$ (קיימת ויחידה, כי $P$ מחוץ למעגל, $O$ במרכז, ו-$A,B$ משני צידי הישר $OP$ לפי החפיפה הסימטרית בצעד 1). נשווה את שני המשולשים $\triangle OAM$ ו-$\triangle OBM$:
- $OA = OB = r$ — שני רדיוסים (`def_circle_radius`).
- $\angle AOM = \angle BOM = \alpha$ — מצעד 2 ($M$ על הקטע $OP$, לכן הזוויות $\angle AOM$ ו-$\angle AOP$ זהות; כנ"ל $\angle BOM = \angle BOP$).
- $OM = OM$ — צלע משותפת.

הזוויות $\angle AOM, \angle BOM$ כלואות בין הצלעות המתאימות $OA, OM$ ו-$OB, OM$ בהתאמה. לפי `ax_sas_congruence` (חפיפת צ.ז.צ), $\triangle OAM \cong \triangle OBM$. מהגדרת חפיפה (`def_congruent_triangles`):
- $AM = BM$ — לכן $M$ אמצע $AB$, כלומר $OP$ חוצה את $AB$.
- $\angle OMA = \angle OMB$ — שתי זוויות אלו צמודות וסכומן $180^\circ$ (זווית שטוחה לאורך $AB$). זוויות צמודות שוות חייבות להיות ישרות, כלומר $\angle OMA = \angle OMB = 90^\circ$. לכן $OP \perp AB$.

לפיכך $OP$ מאונך ל-$AB$ וחוצה אותו, כנדרש. $\blacksquare$
