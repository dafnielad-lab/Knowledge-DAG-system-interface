---
id: prf_parametric_equations_circle
claim_id: thm_parametric_equations_circle
method: informal
status: reviewed
dependencies:
- def_circle_equation_standard
- thm_sin_cos_pythagorean
is_canonical: true
date_added: '2026-06-28T20:34:16.588227Z'
schema_version: 1
---

**הוכחה.** נראה שתמונת ההעתקה $t \mapsto (h + r\cos t,\ k + r\sin t)$ עבור $t \in [0, 2\pi)$ מכסה את המעגל באופן חד-חד-ערכי.

*כיוון אחד — כל נקודה פרמטרית מקיימת את משוואת המעגל.* נציב $x = h + r\cos t$, $y = k + r\sin t$ במשוואה הקנונית מ-`def_circle_equation_standard`:

$$(x - h)^2 + (y - k)^2 = (r\cos t)^2 + (r\sin t)^2 = r^2(\cos^2 t + \sin^2 t).$$

לפי `thm_sin_cos_pythagorean` מתקיים $\cos^2 t + \sin^2 t = 1$, ולכן $(x - h)^2 + (y - k)^2 = r^2$. כלומר, הנקודה $(x, y)$ נמצאת על המעגל.

*כיוון שני — כל נקודה על המעגל מתקבלת מ-$t$ יחיד.* תהי $(x, y)$ נקודה כלשהי על המעגל. אזי $(x - h)^2 + (y - k)^2 = r^2$ ולכן הזוג $\left(\frac{x-h}{r}, \frac{y-k}{r}\right)$ מקיים $\left(\frac{x-h}{r}\right)^2 + \left(\frac{y-k}{r}\right)^2 = 1$, כך שהוא נקודה על מעגל היחידה. לכל נקודה על מעגל היחידה קיים $t$ יחיד בתחום $[0, 2\pi)$ שעבורו $\cos t = \frac{x-h}{r}$ ו-$\sin t = \frac{y-k}{r}$ (זוהי הגדרת הזווית המכוונת). מכאן $x = h + r\cos t$ ו-$y = k + r\sin t$.

שני הכיוונים יחד מראים שהמשוואות הפרמטריות מתארות בדיוק את המעגל הנדון, באופן חד-חד-ערכי. $\blacksquare$
