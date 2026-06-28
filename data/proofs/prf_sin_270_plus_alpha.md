---
id: prf_sin_270_plus_alpha
claim_id: thm_sin_270_plus_alpha
method: informal
status: reviewed
dependencies:
- thm_sin_addition_formula
- thm_cos_addition_formula
- thm_sin_special_values
- thm_cos_special_values
is_canonical: true
date_added: '2026-06-28T15:49:27.903704Z'
schema_version: 1
---

נשתמש בנוסחת החיבור לסינוס (thm_sin_addition_formula) עם הזווית הקבועה $270°$:
$$\sin(270° + \alpha) = \sin 270° \cdot \cos\alpha + \cos 270° \cdot \sin\alpha.$$

את הערכים $\sin 270°$ ו-$\cos 270°$ נחשב באמצעות $270° = 180° + 90°$ ונוסחאות החיבור (thm_sin_addition_formula, thm_cos_addition_formula) על בסיס הערכים המיוחדים (thm_sin_special_values, thm_cos_special_values).

ראשית, $\cos 180° = \cos(90°+90°) = 0\cdot 0 - 1\cdot 1 = -1$ ו-$\sin 180° = \sin(90°+90°) = 1\cdot 0 + 0\cdot 1 = 0$.

כעת:
- $\sin 270° = \sin(180° + 90°) = \sin 180° \cos 90° + \cos 180° \sin 90° = 0 \cdot 0 + (-1) \cdot 1 = -1.$
- $\cos 270° = \cos(180° + 90°) = \cos 180° \cos 90° - \sin 180° \sin 90° = (-1) \cdot 0 - 0 \cdot 1 = 0.$

נציב חזרה:
$$\sin(270° + \alpha) = (-1) \cdot \cos\alpha + 0 \cdot \sin\alpha = -\cos\alpha.$$

זוהי הזהות המבוקשת. $\blacksquare$

**הערה גאומטרית:** סיבוב הנקודה $(\cos\alpha, \sin\alpha)$ ב-$270°$ נגד כיוון השעון על מעגל היחידה שולח אותה ל-$(\sin\alpha, -\cos\alpha)$. קואורדינטת ה-$y$ של הנקודה החדשה — שהיא $\sin(270° + \alpha)$ לפי הגדרת הסינוס — היא $-\cos\alpha$, בהתאם לחישוב האלגברי.
