---
id: prf_arcsin_domain_range
claim_id: thm_arcsin_domain_range
method: informal
status: reviewed
dependencies:
- def_arcsin
- def_sin
- def_inverse_function
- def_bijection
- def_increasing_function
- def_unit_circle
- thm_sin_special_values
- thm_sin_cos_pythagorean
is_canonical: true
date_added: '2026-06-28T20:34:16.541131Z'
schema_version: 1
---

**שלב 1 — צמצום $\sin$ לתחום $[-\pi/2, \pi/2]$ הוא חד-חד-ערכי.**

לפי `def_sin`, $\sin\theta$ הוא הקואורדינטה $y$ של הנקודה $P(\theta) = (\cos\theta, \sin\theta)$ על מעגל היחידה (`def_unit_circle`). כאשר $\theta$ עובר ברציפות מ-$-\pi/2$ עד $\pi/2$, הנקודה $P(\theta)$ עוברת לאורך החצי הימני של מעגל היחידה (הקואורדינטה $x = \cos\theta \geq 0$ שם), מהנקודה $(0, -1)$ עד $(0, 1)$. הקואורדינטה $y$ במסלול זה גדלה ממש: אם $-\pi/2 \leq \theta_1 < \theta_2 \leq \pi/2$, אז $\sin\theta_1 < \sin\theta_2$. לכן לפי `def_increasing_function` הפונקציה $\sin$ עולה ממש בתחום זה, ובפרט חד-חד-ערכית.

**שלב 2 — צמצום $\sin$ הוא על $[-1, 1]$.**

לפי `thm_sin_cos_pythagorean`, $\sin^2\theta + \cos^2\theta = 1$, ולכן $\sin^2\theta \leq 1$, כלומר $-1 \leq \sin\theta \leq 1$. מ-`thm_sin_special_values` $\sin(-\pi/2) = -1$ ו-$\sin(\pi/2) = 1$. רציפות הפונקציה $\sin$ ומשפט ערך הביניים מבטיחים שכל ערך $y \in [-1, 1]$ מתקבל בנקודה כלשהי $\theta \in [-\pi/2, \pi/2]$. לכן הפונקציה על.

**שלב 3 — הגדרת ההופכית.**

משלב 1+2, $\sin$ מצומצמת ל-$[-\pi/2, \pi/2]$ היא בייקציה אל $[-1, 1]$ (`def_bijection`). לכן לפי `def_inverse_function` קיימת לה פונקציה הפוכה יחידה $\arcsin: [-1, 1] \to [-\pi/2, \pi/2]$. זוהי בדיוק ההגדרה ב-`def_arcsin`, והאקוויולנציה $\arcsin(y) = \theta \iff (\sin\theta = y \wedge \theta \in [-\pi/2, \pi/2])$ נובעת ישירות מתכונת הפונקציה ההפוכה.

**שלב 4 — $\arcsin$ עולה ממש.**

ההופכית של פונקציה עולה ממש היא עולה ממש (אם $y_1 < y_2$ ונסמן $\theta_i = \arcsin(y_i)$, אזי $\sin\theta_1 = y_1 < y_2 = \sin\theta_2$; אם היה $\theta_1 \geq \theta_2$, מהמונוטוניות של $\sin$ בשלב 1 היה $\sin\theta_1 \geq \sin\theta_2$, סתירה).

**שלב 5 — $\arcsin$ אי-זוגית.**

$\sin$ אי-זוגית: $\sin(-\theta) = -\sin\theta$ (נובע מהסימטריה של מעגל היחידה ביחס לציר $x$). יהי $y \in [-1, 1]$ ונסמן $\theta = \arcsin(y) \in [-\pi/2, \pi/2]$. אז $-\theta \in [-\pi/2, \pi/2]$ ו-$\sin(-\theta) = -\sin\theta = -y$, ולכן $\arcsin(-y) = -\theta = -\arcsin(y)$. $\blacksquare$
