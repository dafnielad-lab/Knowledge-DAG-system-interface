---
id: prf_cos_270_plus_alpha
claim_id: thm_cos_270_plus_alpha
method: informal
status: reviewed
dependencies:
- thm_cos_addition_formula
- thm_sin_addition_formula
- thm_sin_special_values
- thm_cos_special_values
is_canonical: true
date_added: '2026-06-28T15:49:27.901201Z'
schema_version: 1
---

נשתמש בנוסחת החיבור לקוסינוס (thm_cos_addition_formula) עם הזווית הקבועה $270°$:
$$\cos(270° + \alpha) = \cos 270° \cdot \cos\alpha - \sin 270° \cdot \sin\alpha.$$

כדי לחשב את $\cos 270°$ ו-$\sin 270°$, נשתמש בכך ש-$270° = 180° + 90°$ ונפעיל את נוסחאות החיבור:

תחילה, מהזהות $180° = 90° + 90°$, נוסחת החיבור לקוסינוס וערכי הסינוס/קוסינוס המיוחדים (thm_sin_special_values, thm_cos_special_values): $\cos 180° = 0 \cdot 0 - 1 \cdot 1 = -1$ ו-$\sin 180° = 1 \cdot 0 + 0 \cdot 1 = 0$.

כעת:
- $\cos 270° = \cos(180° + 90°) = \cos 180° \cos 90° - \sin 180° \sin 90° = (-1) \cdot 0 - 0 \cdot 1 = 0.$
- $\sin 270° = \sin(180° + 90°) = \sin 180° \cos 90° + \cos 180° \sin 90° = 0 \cdot 0 + (-1) \cdot 1 = -1$, באמצעות נוסחת החיבור לסינוס (thm_sin_addition_formula).

נציב חזרה:
$$\cos(270° + \alpha) = 0 \cdot \cos\alpha - (-1) \cdot \sin\alpha = \sin\alpha.$$

זוהי הזהות המבוקשת. $\blacksquare$

**הערה גאומטרית:** על מעגל היחידה, $270°$ מתאים לנקודה $(0,-1)$. סיבוב הנקודה $(\cos\alpha, \sin\alpha)$ בעוד $270°$ נגד כיוון השעון (או, באופן שקול, $90°$ עם כיוון השעון) שולח אותה לנקודה $(\sin\alpha, -\cos\alpha)$, וקואורדינטת ה-$x$ של הנקודה הזו היא בדיוק $\sin\alpha$.
