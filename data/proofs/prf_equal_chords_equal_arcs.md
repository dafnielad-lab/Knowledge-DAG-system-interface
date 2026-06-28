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
- def_congruent_triangles
- ax_sas_congruence
- ax_sss_congruence
is_canonical: true
date_added: '2026-06-28T21:06:29.457177Z'
schema_version: 1
---

יהי מעגל ברדיוס $r$ שמרכזו $O$ (`def_circle`, `def_circle_center`, `def_circle_radius`), ויהיו $AB$ ו-$CD$ שני מיתרים שלו (`def_chord`). נוכיח את שלושת השוויונות לפי שתי גרירות הדדיות.

**כיוון א — ($AB = CD \Rightarrow \angle AOB = \angle COD$).**

נתבונן במשולשים $\triangle OAB$ ו-$\triangle OCD$:
- $OA = OC = r$ — שני רדיוסים של אותו מעגל (`def_circle_radius`).
- $OB = OD = r$ — שני רדיוסים של אותו מעגל (`def_circle_radius`).
- $AB = CD$ — נתון.

לפי `ax_sss_congruence` (חפיפת צ.צ.צ), $\triangle OAB \cong \triangle OCD$. מהגדרת חפיפת משולשים (`def_congruent_triangles`) נובע ששוויון הזוויות המתאימות מתקיים; בפרט הזווית שמול הצלע $AB$ ב-$\triangle OAB$ שווה לזווית שמול $CD$ ב-$\triangle OCD$:
$$\angle AOB = \angle COD.$$

**כיוון ב — ($\angle AOB = \angle COD \Rightarrow AB = CD$).**

נתבונן שוב באותם משולשים. כעת ידוע:
- $OA = OC = r$ (`def_circle_radius`).
- $\angle AOB = \angle COD$ — נתון.
- $OB = OD = r$ (`def_circle_radius`).

הזווית $\angle AOB$ כלואה בין הצלעות $OA, OB$, והזווית $\angle COD$ כלואה בין $OC, OD$. לפי `ax_sas_congruence` (חפיפת צ.ז.צ), $\triangle OAB \cong \triangle OCD$. מהגדרת חפיפה (`def_congruent_triangles`) נובע ש-$AB = CD$.

שני הכיוונים יחד נותנים את השקילות $AB = CD \Leftrightarrow \angle AOB = \angle COD$.

**כיוון ג — שקילות הזוויות המרכזיות לאורכי הקשתות.**

זווית מרכזית במעגל מוגדרת (`def_central_angle`) כזווית שקודקודה במרכז המעגל, והקשת שעליה היא נשענת (`def_arc_of_circle`) היא חלק רציף של המעגל הכלוא בין שוקי הזווית. גודל הקשת — מספר המעלות שהיא תופסת לאורך המעגל — נקבע לחלוטין על-ידי הזווית המרכזית שמולה: בחטיבת הביניים מוסכם שמודדים קשת באותו גודל כמו הזווית המרכזית הנשענת עליה ("מידת קשת" במעלות). לכן שתי קשתות באותו מעגל שוות במידתן אם ורק אם הזוויות המרכזיות שמולן שוות.

כיוון שהמעגל סימטרי סביב מרכזו $O$ ובעל רדיוס יחיד $r$, שתי קשתות באותו מעגל בעלות אותה מידה (אותה זווית מרכזית) הן גם בעלות אותו אורך — שתיהן נחתכות מאותו מעגל "שלם" ביחס זהה. לכן:
$$\angle AOB = \angle COD \;\Leftrightarrow\; \overset{\frown}{AB} = \overset{\frown}{CD}.$$

**איחוד.** משילוב כיוונים א, ב, ג מתקבל:
$$AB = CD \;\Leftrightarrow\; \angle AOB = \angle COD \;\Leftrightarrow\; \overset{\frown}{AB} = \overset{\frown}{CD}. \quad\blacksquare$$
