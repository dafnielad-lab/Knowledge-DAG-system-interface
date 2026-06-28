---
id: prf_parametric_equations_hyperbola
claim_id: thm_parametric_equations_hyperbola
method: informal
status: reviewed
dependencies:
- thm_hyperbola_canonical_equation
- thm_pythagorean_identity_tan
- def_secant_cosecant_cotangent
is_canonical: true
date_added: '2026-06-28T20:34:16.597254Z'
schema_version: 1
---

**הוכחה.** לפי `thm_hyperbola_canonical_equation`, ההיפרבולה מקיימת $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$. לפי `def_secant_cosecant_cotangent` $\sec t = \frac{1}{\cos t}$, כך ש-$\sec t$ מוגדר כאשר $\cos t \neq 0$.

*כיוון אחד — כל נקודה פרמטרית מקיימת את משוואת ההיפרבולה.* נציב $x = a\sec t$, $y = b\tan t$:

$$\frac{x^2}{a^2} - \frac{y^2}{b^2} = \frac{(a\sec t)^2}{a^2} - \frac{(b\tan t)^2}{b^2} = \sec^2 t - \tan^2 t.$$

לפי `thm_pythagorean_identity_tan` מתקיים $1 + \tan^2 t = \sec^2 t$, כלומר $\sec^2 t - \tan^2 t = 1$. לכן הזוג $(x, y)$ נמצא על ההיפרבולה.

*כיוון שני — כל נקודה על ההיפרבולה מתקבלת מ-$t$.* תהי $(x, y)$ נקודה על ההיפרבולה. אזי $\left(\frac{x}{a}\right)^2 - \left(\frac{y}{b}\right)^2 = 1$ ולכן $\left|\frac{x}{a}\right| \geq 1$. נסמן $u = \frac{x}{a}$, $v = \frac{y}{b}$.

- אם $u \geq 1$ (ענף ימני): קיים $t \in (-\frac{\pi}{2}, \frac{\pi}{2})$ יחיד שעבורו $\sec t = u$ (כי $\sec t$ עולה ממונוטונית מ-$1$ ל-$+\infty$ על $[0, \frac{\pi}{2})$, ומ-$1$ ל-$+\infty$ גם על $(-\frac{\pi}{2}, 0]$ — ערך-החתימה של $t$ נקבע על ידי הסימן של $v$: $\tan t$ עולה ממונוטונית מ-$-\infty$ ל-$+\infty$ על אותו תחום). אזי $\tan t = \pm\sqrt{\sec^2 t - 1} = \pm\sqrt{u^2 - 1} = \pm|v|$, ובוחרים את הסימן כך שיתאים ל-$v$.
- אם $u \leq -1$ (ענף שמאלי): אנלוגית, עבור $t \in (\frac{\pi}{2}, \frac{3\pi}{2})$, $\sec t$ נוגעת בכל ערך ב-$(-\infty, -1]$ ו-$\tan t$ נוגעת בכל ערך ב-$\mathbb{R}$.

בכל מקרה, קיים $t$ המתאים ליצירת הנקודה $(x, y)$. $\blacksquare$
