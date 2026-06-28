---
id: prf_parametric_equations_ellipse
claim_id: thm_parametric_equations_ellipse
method: informal
status: reviewed
dependencies:
- thm_ellipse_canonical_equation
- thm_sin_cos_pythagorean
is_canonical: true
date_added: '2026-06-28T20:34:16.591733Z'
schema_version: 1
---

**הוכחה.** נבדוק את שני הכיוונים.

*כיוון אחד — כל נקודה פרמטרית מקיימת את המשוואה הקנונית.* נציב $x = a\cos t$, $y = b\sin t$ במשוואה הקנונית של האליפסה (מ-`thm_ellipse_canonical_equation`):

$$\frac{x^2}{a^2} + \frac{y^2}{b^2} = \frac{(a\cos t)^2}{a^2} + \frac{(b\sin t)^2}{b^2} = \cos^2 t + \sin^2 t.$$

לפי `thm_sin_cos_pythagorean`, $\cos^2 t + \sin^2 t = 1$, ולכן הזוג $(x, y)$ מקיים את משוואת האליפסה.

*כיוון שני — כל נקודה על האליפסה מתקבלת מ-$t$ יחיד.* תהי $(x, y)$ נקודה על האליפסה. אזי $\left(\frac{x}{a}\right)^2 + \left(\frac{y}{b}\right)^2 = 1$, כלומר $\left(\frac{x}{a}, \frac{y}{b}\right)$ נקודה על מעגל היחידה. לכן קיים $t \in [0, 2\pi)$ יחיד שעבורו $\cos t = \frac{x}{a}$ ו-$\sin t = \frac{y}{b}$, ומכאן $x = a\cos t$ ו-$y = b\sin t$. הפרמטריזציה היא אם כן חד-חד-ערכית ועל.

**הערה גאומטרית:** עיוות הקנה-מידה במישור — המרחק האנכי מהציר ב-$y$ נמתח ב-$b/a$ ביחס למעגל היחידה — הופך את $t$ ל"זווית אקסצנטרית": $t$ היא זווית הנקודה המתאימה על מעגל היחידה לפני העיוות, ולא הזווית הקוטבית של $(x, y)$ עצמה. $\blacksquare$
