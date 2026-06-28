---
id: prf_equal_tangents_from_external_point
claim_id: thm_equal_tangents_from_external_point
method: informal
status: reviewed
dependencies:
- def_circle
- def_circle_center
- def_circle_radius
- def_tangent_to_circle
- thm_tangent_perpendicular_to_radius
- def_right_triangle
- ax_hl_congruence
is_canonical: true
date_added: '2026-06-28T16:00:00.000000Z'
schema_version: 1
---

יהי מעגל ברדיוס $r$ שמרכזו $O$ (`def_circle`, `def_circle_center`, `def_circle_radius`), ותהי $P$ נקודה מחוץ למעגל. נניח ש-$PA$ ו-$PB$ הם שני משיקים למעגל (`def_tangent_to_circle`) מ-$P$, כאשר $A,B$ נקודות ההשקה.

**צעד 1 — שני משולשים ישרי-זווית.**

לפי `thm_tangent_perpendicular_to_radius`, משיק למעגל מאונך לרדיוס בנקודת ההשקה. לכן:
$$OA \perp PA \quad \text{וגם} \quad OB \perp PB.$$

לפיכך $\triangle OAP$ ו-$\triangle OBP$ הם משולשים ישרי-זווית (`def_right_triangle`), כאשר הזווית הישרה ב-$A$ וב-$B$ בהתאמה. בכל אחד מהם, היתר הוא $OP$ (הצלע שמול הזווית הישרה).

**צעד 2 — חפיפת המשולשים לפי יתר-ניצב.**

נשווה את שני המשולשים $\triangle OAP$ ו-$\triangle OBP$:

- **יתר משותף:** $OP = OP$ — צלע משותפת לשני המשולשים.
- **ניצב שווה:** $OA = OB = r$, שני רדיוסים של אותו מעגל (לפי `def_circle_radius`).

לפי `ax_hl_congruence` (חפיפת יתר-ניצב במשולשים ישרי-זווית), $\triangle OAP \cong \triangle OBP$.

**צעד 3 — מסקנות מהחפיפה.**

מהחפיפה נובע ששאר הצלעות והזוויות המתאימות שוות:

1. **שוויון אורכי המשיקים:** $PA = PB$ — שני הניצבים השניים מתאימים זה לזה במשולשים החופפים. זוהי הטענה המרכזית.

2. **$PO$ חוצה את $\angle APB$:** הזוויות $\angle APO = \angle BPO$ מתאימות זו לזו בחפיפה, ולכן הקרן $PO$ היא חוצה הזווית $\angle APB$.

3. **$OP$ חוצה את $AB$ באנך:** הזוויות $\angle AOP = \angle BOP$ מתאימות זו לזו בחפיפה, ולכן הקרן $OP$ היא גם חוצה הזווית $\angle AOB$. במשולש שווה-השוקיים $\triangle OAB$ (שכן $OA = OB = r$), חוצה זווית הראש $O$ הוא גם תיכון ואנך לבסיס $AB$. לכן $OP$ מאונך ל-$AB$ וחוצה אותו.

$\blacksquare$
