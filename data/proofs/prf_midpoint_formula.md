---
id: prf_midpoint_formula
claim_id: def_midpoint_formula
method: informal
status: reviewed
dependencies:
- def_coordinate_plane
- def_distance_formula
is_canonical: true
date_added: '2026-06-28T15:49:27.852205Z'
schema_version: 1
---

נקודת האמצע של קטע $AB$ מוגדרת גאומטרית כנקודה $M$ על הקטע המקיימת $|AM| = |MB|$. נראה כי הנקודה $M = \left(\dfrac{x_1 + x_2}{2}, \dfrac{y_1 + y_2}{2}\right)$ אכן מקיימת תכונה זו עבור $A = (x_1, y_1)$ ו-$B = (x_2, y_2)$.

**שלב 1: שוויון המרחקים.** נחשב את המרחקים בעזרת נוסחת המרחק (`def_distance_formula`):
$$|AM|^2 = \left(\frac{x_1 + x_2}{2} - x_1\right)^2 + \left(\frac{y_1 + y_2}{2} - y_1\right)^2 = \left(\frac{x_2 - x_1}{2}\right)^2 + \left(\frac{y_2 - y_1}{2}\right)^2.$$
ובאופן דומה:
$$|MB|^2 = \left(x_2 - \frac{x_1 + x_2}{2}\right)^2 + \left(y_2 - \frac{y_1 + y_2}{2}\right)^2 = \left(\frac{x_2 - x_1}{2}\right)^2 + \left(\frac{y_2 - y_1}{2}\right)^2.$$
קיבלנו $|AM|^2 = |MB|^2$, ומכיוון ששני האגפים אי-שליליים נובע $|AM| = |MB|$.

**שלב 2: $M$ נמצאת על הקטע $AB$.** נראה כי שלוש הנקודות $A$, $M$, $B$ נמצאות על אותו ישר, וכי $M$ בין $A$ ל-$B$. נחשב את המרחק $|AB|$ לפי `def_distance_formula`:
$$|AB| = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}.$$
ומצד שני, $|AM| + |MB| = 2|AM| = 2 \cdot \sqrt{\left(\dfrac{x_2 - x_1}{2}\right)^2 + \left(\dfrac{y_2 - y_1}{2}\right)^2} = 2 \cdot \dfrac{1}{2}\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} = |AB|$.

מכיוון ש-$|AM| + |MB| = |AB|$ (אי-שוויון המשולש מתקיים בשוויון), שלוש הנקודות הן קולינאריות ו-$M$ נמצאת בין $A$ ל-$B$.

**מסקנה.** הנקודה $M = \left(\dfrac{x_1 + x_2}{2}, \dfrac{y_1 + y_2}{2}\right)$ נמצאת על הקטע $AB$ ומקיימת $|AM| = |MB|$, ולכן היא נקודת האמצע של הקטע (לפי `def_coordinate_plane` כל נקודה זו מוגדרת היטב ע"י זוג קואורדינטות במישור). $\blacksquare$
