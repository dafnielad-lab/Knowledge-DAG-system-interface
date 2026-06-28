---
id: prf_symmetric_equation_line_3d
claim_id: def_symmetric_equation_line_3d
method: informal
status: reviewed
dependencies:
- def_parametric_equation_of_line_3d
is_canonical: true
date_added: '2026-06-28T20:34:16.585236Z'
schema_version: 1
---

**הצדקה.** לפי `def_parametric_equation_of_line_3d`, נקודה $(x, y, z)$ נמצאת על הישר אם ורק אם קיים $t \in \mathbb{R}$ כך ש-$x = x_0 + t v_1$, $y = y_0 + t v_2$, $z = z_0 + t v_3$. כאשר $v_1, v_2, v_3 \neq 0$ נוכל לחלץ את $t$ מכל אחת מהמשוואות:

$$t = \frac{x - x_0}{v_1}, \quad t = \frac{y - y_0}{v_2}, \quad t = \frac{z - z_0}{v_3}.$$

מכיוון שכל שלוש המשוואות חייבות לתת את אותו ערך של $t$ (כדי שייצגו נקודה אחת על הישר), קיבלנו את הצורה הסימטרית $\frac{x - x_0}{v_1} = \frac{y - y_0}{v_2} = \frac{z - z_0}{v_3}$. הצורה הסימטרית שקולה לזוג משוואות לינאריות (למשל $\frac{x-x_0}{v_1} = \frac{y-y_0}{v_2}$ ו-$\frac{y-y_0}{v_2} = \frac{z-z_0}{v_3}$), ולכן הישר במרחב מתואר כחיתוך שני מישורים. כאשר אחד הרכיבים מתאפס (למשל $v_1 = 0$), הפרמטר $t$ אינו משפיע על קואורדינטת $x$ ולכן הישר מקיים $x \equiv x_0$, ואת שני השוויונות הנותרים שומרים. $\blacksquare$
