---
id: prf_equal_chords_equal_arcs
claim_id: thm_equal_chords_equal_arcs
method: informal
status: reviewed
dependencies:
- def_circle
- def_circle_center
- def_circle_radius
- def_chord
- def_arc_of_circle
- def_central_angle
- ax_sss_congruence
- thm_arc_length_in_circle
is_canonical: true
date_added: '2026-06-28T16:00:00.000000Z'
schema_version: 1
---

יהי מעגל ברדיוס $r$ שמרכזו $O$ (`def_circle`, `def_circle_center`, `def_circle_radius`), ויהיו $AB$ ו-$CD$ שני מיתרים (`def_chord`) במעגל המקיימים $AB = CD$.

**צעד 1 — חפיפת המשולשים $\triangle OAB$ ו-$\triangle OCD$.**

נסתכל בשני המשולשים:

- $OA = OC = r$ (שני רדיוסים, לפי `def_circle_radius`).
- $OB = OD = r$ (שני רדיוסים, לפי `def_circle_radius`).
- $AB = CD$ (נתון).

לפי `ax_sss_congruence` (חפיפת צ.צ.צ), $\triangle OAB \cong \triangle OCD$.

**צעד 2 — הזוויות המרכזיות שוות.**

מהחפיפה נובע שכל הזוויות המתאימות שוות. בפרט הזוויות שמול הצלעות השוות $AB$ ו-$CD$ — אלה הזוויות $\angle AOB$ ו-$\angle COD$ — שוות:
$$\angle AOB = \angle COD.$$

זוויות אלה הן הזוויות המרכזיות (`def_central_angle`) המתאימות לקשתות $\overset{\frown}{AB}$ ו-$\overset{\frown}{CD}$.

**צעד 3 — הקשתות שוות באורכן.**

לפי `thm_arc_length_in_circle`, אורך קשת במעגל ברדיוס $r$ שעליה נשענת זווית מרכזית $\theta$ (ברדיאנים) הוא $L = r\theta$ (אורך הקשת `def_arc_of_circle` המתאימה). לפי צעד 2, הזוויות המרכזיות שוות, ולכן:
$$\overset{\frown}{AB} = r \cdot \angle AOB = r \cdot \angle COD = \overset{\frown}{CD}.$$

**הכיוון ההפוך.** אם נתון $\overset{\frown}{AB} = \overset{\frown}{CD}$, אזי לפי `thm_arc_length_in_circle` (בכיוון ההפוך, חלוקה ב-$r > 0$) הזוויות המרכזיות שוות $\angle AOB = \angle COD$. אז לפי `ax_sas_congruence` (צ.ז.צ עם $OA=OC=r$, $\angle AOB = \angle COD$, $OB=OD=r$) המשולשים $\triangle OAB \cong \triangle OCD$, ולכן הצלעות $AB = CD$.

לפיכך, $AB = CD \Leftrightarrow \angle AOB = \angle COD \Leftrightarrow \overset{\frown}{AB} = \overset{\frown}{CD}$. $\blacksquare$
