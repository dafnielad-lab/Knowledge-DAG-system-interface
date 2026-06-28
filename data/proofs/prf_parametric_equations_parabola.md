---
id: prf_parametric_equations_parabola
claim_id: thm_parametric_equations_parabola
method: informal
status: reviewed
dependencies:
- thm_parabola_canonical_equation
is_canonical: true
date_added: '2026-06-28T20:34:16.594254Z'
schema_version: 1
---

**הוכחה.** לפי `thm_parabola_canonical_equation` הפרבולה הקנונית מתוארת על ידי $x^2 = 4py$.

*כיוון אחד — כל נקודה פרמטרית נמצאת על הפרבולה.* נציב $x = 2pt$, $y = pt^2$:

$$x^2 = (2pt)^2 = 4p^2 t^2 = 4p \cdot (pt^2) = 4p y.$$

כלומר $(x, y) = (2pt, pt^2)$ אכן על הפרבולה לכל $t \in \mathbb{R}$.

*כיוון שני — כל נקודה על הפרבולה מתקבלת מ-$t$ יחיד.* תהי $(x, y)$ נקודה על הפרבולה, $x^2 = 4py$. נגדיר $t := \dfrac{x}{2p}$ (מותר כי $p \neq 0$). אזי $2pt = x$, ובנוסף:

$$pt^2 = p \cdot \left(\frac{x}{2p}\right)^2 = p \cdot \frac{x^2}{4p^2} = \frac{x^2}{4p} = \frac{4py}{4p} = y.$$

שתי המשוואות הפרמטריות מתקיימות עם אותו $t$ יחיד. לכן ההעתקה $t \mapsto (2pt, pt^2)$ היא חד-חד-ערכית ועל הפרבולה כולה. $\blacksquare$
