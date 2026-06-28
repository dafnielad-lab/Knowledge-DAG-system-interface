---
id: prf_30_60_90_triangle
claim_id: def_30_60_90_triangle
method: informal
status: reviewed
dependencies:
- def_right_triangle
- def_equilateral_triangle
- thm_equilateral_triangle_angles
- ax_sss_congruence
- def_congruent_triangles
- thm_triangle_angle_sum
- thm_pythagoras
is_canonical: true
date_added: '2026-06-28T21:06:29.453679Z'
schema_version: 1
---

**רישום המושג.** משולש 30-60-90 הוא מקרה פרטי של משולש ישר-זווית (def_right_triangle), שבו אחת הזוויות הישרה ($90°$) ושתי הזוויות החדות הן $30°$ ו-$60°$ — צירוף שמחויב על-ידי משפט סכום זוויות במשולש: $30° + 60° + 90° = 180°$ (thm_triangle_angle_sum).

**בנייה — כיצד מתקבל משולש כזה.** ניקח משולש שווה צלעות $\triangle PQR$ עם אורך צלע $a$ (def_equilateral_triangle), שבו לפי thm_equilateral_triangle_angles כל זווית פנימית היא $60°$:
$$\angle QPR = \angle PQR = \angle PRQ = 60°.$$
תהי $M$ נקודת האמצע של הצלע $QR$. נחבר את $P$ אל $M$ ונקבל את הקטע $PM$. נסמן באורך $QR = a$, ולכן $QM = MR = \dfrac{a}{2}$.

**שני המשולשים הקטנים חופפים.** נשווה את המשולשים $\triangle PQM$ ו-$\triangle PRM$:
1. $PQ = PR$ — שתי הצלעות שוות באורך $a$, מהיות $\triangle PQR$ שווה צלעות (def_equilateral_triangle).
2. $QM = RM$ — שתיהן באורך $\dfrac{a}{2}$, מהיות $M$ נקודת האמצע של $QR$.
3. $PM = PM$ — צלע משותפת.

כלומר שלוש הצלעות של $\triangle PQM$ שוות בהתאמה לשלוש הצלעות של $\triangle PRM$. לפי משפט החפיפה צ.צ.צ (ax_sss_congruence): $\triangle PQM \cong \triangle PRM$.

**חישוב הזוויות במשולש $\triangle PQM$.** מן החפיפה ומהגדרת משולשים חופפים (def_congruent_triangles) נובע ש-$\angle PMQ = \angle PMR$. שתי הזוויות הללו ביחד יוצרות זווית שטוחה (כי $Q, M, R$ על ישר אחד) ולכן סכומן $180°$, ומכאן
$$\angle PMQ = \angle PMR = 90°.$$
כן נובע מהחפיפה ש-$\angle QPM = \angle RPM$. שתי הזוויות הללו ביחד הן הזווית $\angle QPR = 60°$, ולכן
$$\angle QPM = \angle RPM = 30°.$$
והזווית הנותרת ב-$\triangle PQM$ היא $\angle PQM = \angle PQR = 60°$ (לא השתנתה).

קיבלנו ש-$\triangle PQM$ הוא משולש ישר-זווית (def_right_triangle) עם זוויות $30°, 60°, 90°$ — בדיוק ההגדרה של משולש 30-60-90. הראינו אפוא שמושג זה אינו ריק.

**יחסי הצלעות.** במשולש $\triangle PQM$ שקיבלנו, היתר הוא $PQ = a$ (מול הזווית הישרה ב-$M$), הניצב שמול הזווית $30°$ (שב-$P$) הוא $QM = \dfrac{a}{2}$, והניצב שמול הזווית $60°$ (שב-$Q$) הוא $PM$. לפי משפט פיתגורס (thm_pythagoras):
$$PM^2 = PQ^2 - QM^2 = a^2 - \left(\frac{a}{2}\right)^2 = a^2 - \frac{a^2}{4} = \frac{3a^2}{4},$$
ולכן $PM = \dfrac{a\sqrt{3}}{2}$. כאשר נסמן את אורך היתר ב-$c$ (כלומר $c = a$) מתקבל:
$$\text{ניצב מול } 30° = \frac{c}{2}, \qquad \text{ניצב מול } 60° = \frac{c\sqrt{3}}{2}, \qquad \text{יתר} = c,$$
והיחס $1 : \sqrt{3} : 2$. $\blacksquare$
