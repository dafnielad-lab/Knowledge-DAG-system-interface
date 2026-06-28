---
id: prf_triangle_exterior_angle_inequality
claim_id: thm_triangle_exterior_angle_inequality
method: informal
status: reviewed
dependencies:
- def_triangle
- def_angle
- thm_triangle_angle_sum
is_canonical: true
date_added: '2026-06-28T15:07:55.476550Z'
schema_version: 1
---

יהי $\triangle ABC$ משולש (לפי def_triangle), ותהי $D$ נקודה על המשך הצלע $BC$ מעבר ל-$C$, כך ש-$B$, $C$, $D$ קוֹליניאריים ו-$C$ נמצאת בין $B$ ל-$D$.

הזווית $\angle ACD$ היא הזווית החיצונית בקודקוד $C$ (לפי def_angle), והיא צמודה לזווית הפנימית $\angle ACB$ של המשולש. מכיוון ש-$B$, $C$, $D$ על ישר אחד, שתי הזוויות הללו יוצרות זווית שטוחה, ולכן:
$$\angle ACD + \angle ACB = 180°.$$

מצד שני, לפי משפט סכום הזוויות במשולש (thm_triangle_angle_sum), שלוש הזוויות הפנימיות של $\triangle ABC$ מקיימות:
$$\angle A + \angle B + \angle ACB = 180°.$$

משוויון שני הביטויים ל-$180°$ נקבל:
$$\angle ACD + \angle ACB = \angle A + \angle B + \angle ACB,$$
ולאחר חיסור $\angle ACB$ משני האגפים:
$$\angle ACD = \angle A + \angle B.$$

קיבלנו שהזווית החיצונית שווה לסכום שתי הזוויות הפנימיות הלא-צמודות (זהו "משפט הזווית החיצונית" במובנו השוויוני).

נוכיח כעת את אי-השוויון. שתי הזוויות $\angle A$ ו-$\angle B$ הן זוויות פנימיות של משולש לא מנוון (לפי def_triangle, שלוש הקודקודים אינם קוֹליניאריים), ולכן כל אחת מהן חיובית ממש: $\angle A > 0$ ו-$\angle B > 0$. מכאן:
$$\angle ACD = \angle A + \angle B > \angle A,$$
$$\angle ACD = \angle A + \angle B > \angle B.$$

הוכחנו את האי-שוויון לקודקוד $C$. ההוכחה לקודקודים $A$ ו-$B$ זהה בסימטריה — המשפט תקף לכל קודקוד במשולש. $\blacksquare$
