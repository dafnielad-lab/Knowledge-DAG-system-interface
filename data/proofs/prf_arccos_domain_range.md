---
id: prf_arccos_domain_range
claim_id: thm_arccos_domain_range
method: informal
status: reviewed
dependencies:
- def_arccos
- def_cos
- def_inverse_function
- def_bijection
- def_decreasing_function
- def_unit_circle
- thm_cos_special_values
- thm_sin_cos_pythagorean
is_canonical: true
date_added: '2026-06-28T20:34:16.544144Z'
schema_version: 1
---

**שלב 1 — צמצום $\cos$ לתחום $[0, \pi]$ הוא חד-חד-ערכי.**

לפי `def_cos`, $\cos\theta$ הוא הקואורדינטה $x$ של הנקודה $P(\theta) = (\cos\theta, \sin\theta)$ על מעגל היחידה (`def_unit_circle`). כאשר $\theta$ עובר מ-$0$ עד $\pi$, הנקודה עוברת לאורך החצי העליון של מעגל היחידה (הקואורדינטה $y = \sin\theta \geq 0$ שם), מ-$(1, 0)$ עד $(-1, 0)$. הקואורדינטה $x$ במסלול זה יורדת ממש: אם $0 \leq \theta_1 < \theta_2 \leq \pi$, אז $\cos\theta_1 > \cos\theta_2$. לפי `def_decreasing_function`, $\cos$ יורדת ממש בתחום זה, ובפרט חד-חד-ערכית.

**שלב 2 — צמצום $\cos$ הוא על $[-1, 1]$.**

לפי `thm_sin_cos_pythagorean`, $\cos^2\theta \leq 1$, כלומר $-1 \leq \cos\theta \leq 1$. מ-`thm_cos_special_values` $\cos 0 = 1$ ו-$\cos\pi = -1$. רציפות $\cos$ ומשפט ערך הביניים מבטיחים שכל ערך $y \in [-1, 1]$ מתקבל בנקודה $\theta \in [0, \pi]$. לכן הפונקציה על.

**שלב 3 — הגדרת ההופכית.**

משלב 1+2, $\cos$ מצומצמת ל-$[0, \pi]$ היא בייקציה אל $[-1, 1]$ (`def_bijection`). לפי `def_inverse_function` קיימת לה הפונקציה ההפוכה היחידה $\arccos: [-1, 1] \to [0, \pi]$ — בהתאם להגדרה ב-`def_arccos`. האקוויולנציה $\arccos(y) = \theta \iff (\cos\theta = y \wedge \theta \in [0, \pi])$ היא מאפיין הפונקציה ההפוכה.

**שלב 4 — $\arccos$ יורדת ממש.**

ההופכית של פונקציה יורדת ממש היא יורדת ממש. אם $y_1 < y_2$ ונסמן $\theta_i = \arccos(y_i)$, אז $\cos\theta_1 = y_1 < y_2 = \cos\theta_2$; אם היה $\theta_1 \leq \theta_2$, מהמונוטוניות היורדת של $\cos$ בשלב 1 היה $\cos\theta_1 \geq \cos\theta_2$, סתירה. לכן $\theta_1 > \theta_2$.

**שלב 5 — הזהות $\arccos(-y) = \pi - \arccos(y)$.**

יהי $y \in [-1, 1]$ ונסמן $\theta = \arccos(y)$, כך ש-$\theta \in [0, \pi]$ ו-$\cos\theta = y$. אז $\pi - \theta \in [0, \pi]$, ו-$\cos(\pi - \theta) = -\cos\theta = -y$ (זהות שמשלימה לפי הסימטריה של מעגל היחידה ביחס לציר $y$). לכן, מהאקוויולנציה בשלב 3, $\arccos(-y) = \pi - \theta = \pi - \arccos(y)$. $\blacksquare$
