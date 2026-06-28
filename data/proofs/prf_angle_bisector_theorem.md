---
id: prf_angle_bisector_theorem
claim_id: thm_angle_bisector_theorem
method: informal
status: reviewed
dependencies:
- def_triangle
- thm_triangle_area_sin
- thm_triangle_area_base_height
is_canonical: true
date_added: '2026-06-28T15:07:55.420554Z'
schema_version: 1
---

**הוכחה (שיטת השטחים).** נסמן את חציית הזווית ב-$A$ כך ש-$\angle BAD = \angle DAC = \alpha/2$, כאשר $\alpha = \angle BAC$. הנקודה $D$ נמצאת על הצלע $BC$ (זוהי הגדרת חוצה זווית פנימי במשולש $ABC$ — ר' def_triangle).

נחשב את שטחי שני תת-המשולשים $ABD$ ו-$ACD$ בשתי דרכים שונות.

**דרך ראשונה (לפי הזווית הכלואה ב-$A$).** במשולש $ABD$ הצלעות $AB = c$ ו-$AD$ סוגרות את הזווית $\alpha/2$, ולכן לפי thm_triangle_area_sin:
$$S(ABD) = \tfrac{1}{2} \cdot c \cdot AD \cdot \sin(\alpha/2).$$
באופן דומה במשולש $ACD$ הצלעות $AC = b$ ו-$AD$ סוגרות אותה זווית $\alpha/2$:
$$S(ACD) = \tfrac{1}{2} \cdot b \cdot AD \cdot \sin(\alpha/2).$$
חלוקה איבר באיבר נותנת
$$\frac{S(ABD)}{S(ACD)} = \frac{c}{b}. \qquad (\star)$$

**דרך שנייה (לפי בסיס וגובה משותף).** שני המשולשים $ABD$ ו-$ACD$ חולקים את אותו קודקוד $A$, והבסיסים שלהם $BD$ ו-$DC$ שוכנים על אותו ישר $BC$. לכן הגובה מ-$A$ אל הישר $BC$ הוא הגובה לשניהם — נסמנו $h_a$. לפי thm_triangle_area_base_height:
$$S(ABD) = \tfrac{1}{2} \cdot BD \cdot h_a, \qquad S(ACD) = \tfrac{1}{2} \cdot DC \cdot h_a,$$
ומכאן
$$\frac{S(ABD)}{S(ACD)} = \frac{BD}{DC}. \qquad (\star\star)$$

**שילוב.** מ-$(\star)$ ו-$(\star\star)$ קיבלנו את אותו יחס שטחים בשתי דרכים, ולכן
$$\frac{BD}{DC} = \frac{c}{b}. \qquad \blacksquare$$
