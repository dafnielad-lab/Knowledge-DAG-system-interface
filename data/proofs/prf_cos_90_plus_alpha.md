---
id: prf_cos_90_plus_alpha
claim_id: thm_cos_90_plus_alpha
method: informal
status: reviewed
dependencies:
- thm_cos_addition_formula
- thm_sin_special_values
- thm_cos_special_values
is_canonical: true
date_added: '2026-06-28T15:49:27.889702Z'
schema_version: 1
---

נשתמש בנוסחת החיבור לקוסינוס (thm_cos_addition_formula) עם $\beta = \alpha$ והזווית הקבועה $90°$:
$$\cos(90° + \alpha) = \cos 90° \cdot \cos\alpha - \sin 90° \cdot \sin\alpha.$$

מן הערכים המיוחדים של קוסינוס (thm_cos_special_values) נקבל $\cos 90° = \cos\frac{\pi}{2} = 0$, ומן הערכים המיוחדים של סינוס (thm_sin_special_values) נקבל $\sin 90° = \sin\frac{\pi}{2} = 1$. נציב:
$$\cos(90° + \alpha) = 0 \cdot \cos\alpha - 1 \cdot \sin\alpha = -\sin\alpha.$$

זוהי הזהות המבוקשת. $\blacksquare$

**הערה גאומטרית:** על מעגל היחידה, הזווית $90° + \alpha$ מתקבלת על-ידי סיבוב הנקודה המתאימה לזווית $\alpha$ בעוד $90°$ נגד כיוון השעון. סיבוב כזה שולח את הנקודה $(\cos\alpha, \sin\alpha)$ לנקודה $(-\sin\alpha, \cos\alpha)$, ולכן קואורדינטת ה-$x$ של הנקודה החדשה — שהיא $\cos(90° + \alpha)$ לפי הגדרת הקוסינוס — שווה $-\sin\alpha$, כפי שהוכחנו אלגברית.
