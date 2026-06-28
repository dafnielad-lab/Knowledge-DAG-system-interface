---
id: prf_parallelogram_properties
claim_id: thm_parallelogram_properties
method: informal
status: reviewed
dependencies:
- def_parallelogram
- thm_alternate_interior_angles
- ax_asa_congruence
- def_congruent_triangles
- def_angle
is_canonical: true
date_added: '2026-06-28T15:49:27.827703Z'
schema_version: 1
---

תהי $ABCD$ מקבילית (def_parallelogram), כלומר $AB \parallel CD$ ו-$BC \parallel AD$. נעביר את האלכסון $AC$. הוא חוצה את המקבילית לשני משולשים: $\triangle ABC$ ו-$\triangle CDA$.

**שלב 1 — חפיפת המשולשים $\triangle ABC \cong \triangle CDA$.** האלכסון $AC$ הוא חותך של זוג המקבילים $AB$ ו-$CD$, ולכן הזוויות המתחלפות שוות (thm_alternate_interior_angles):
$$\angle BAC = \angle DCA.$$
בדומה, $AC$ הוא חותך של זוג המקבילים $BC$ ו-$AD$, ולכן:
$$\angle BCA = \angle DAC.$$
בנוסף, הצלע $AC$ משותפת לשני המשולשים. לפי משפט החפיפה צ.ז.צ — ליתר דיוק, ז.צ.ז (ax_asa_congruence) המתאים לזווית-צלע-זווית — שני המשולשים חופפים: $\triangle ABC \cong \triangle CDA$.

**שלב 2 — שוויון הצלעות הנגדיות.** ממשולשים חופפים (def_congruent_triangles) נובע ששוויון של צלעות מתאימות, ולכן:
$$AB = CD, \qquad BC = DA.$$
זוהי תכונה (1).

**שלב 3 — שוויון הזוויות הנגדיות.** מחפיפת המשולשים מקבלים גם $\angle B = \angle ABC = \angle CDA = \angle D$. עבור הזוג השני, $\angle A = \angle BAC + \angle DAC$ ו-$\angle C = \angle BCA + \angle DCA$ (סכום זוויות סמוכות בקודקוד, def_angle). מהשוויונות בשלב 1 נובע ש-$\angle A = \angle C$. זוהי תכונה (2).

**שלב 4 — האלכסונים חוצים זה את זה.** נסמן ב-$O$ את נקודת החיתוך של $AC$ ו-$BD$. נתבונן במשולשים $\triangle AOB$ ו-$\triangle COD$. הזוויות $\angle OAB$ ו-$\angle OCD$ הן זוויות מתחלפות בין המקבילים $AB$ ו-$CD$ עם החותך $AC$, ולכן שוות (thm_alternate_interior_angles). באופן דומה $\angle OBA = \angle ODC$ הן זוויות מתחלפות בין אותם מקבילים עם החותך $BD$. בנוסף, $AB = CD$ לפי שלב 2. לפי ז.צ.ז (ax_asa_congruence) מקבלים $\triangle AOB \cong \triangle COD$, ולכן הצלעות המתאימות שוות (def_congruent_triangles):
$$OA = OC, \qquad OB = OD.$$
כלומר, $O$ הוא אמצע של $AC$ וגם של $BD$, וזוהי תכונה (3). $\blacksquare$
