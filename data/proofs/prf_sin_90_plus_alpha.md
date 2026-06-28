---
id: prf_sin_90_plus_alpha
claim_id: thm_sin_90_plus_alpha
method: informal
status: reviewed
dependencies:
- thm_sin_addition_formula
- thm_sin_special_values
- thm_cos_special_values
is_canonical: true
date_added: '2026-06-28T15:49:27.892204Z'
schema_version: 1
---

נשתמש בנוסחת החיבור לסינוס (thm_sin_addition_formula) עם $\beta = \alpha$ והזווית הקבועה $90°$:
$$\sin(90° + \alpha) = \sin 90° \cdot \cos\alpha + \cos 90° \cdot \sin\alpha.$$

מן הערכים המיוחדים של סינוס (thm_sin_special_values) נקבל $\sin 90° = \sin\frac{\pi}{2} = 1$, ומן הערכים המיוחדים של קוסינוס (thm_cos_special_values) נקבל $\cos 90° = \cos\frac{\pi}{2} = 0$. נציב:
$$\sin(90° + \alpha) = 1 \cdot \cos\alpha + 0 \cdot \sin\alpha = \cos\alpha.$$

זוהי הזהות המבוקשת. $\blacksquare$

**הערה גאומטרית:** על מעגל היחידה, הזווית $90° + \alpha$ מתקבלת מהזווית $\alpha$ בסיבוב של $90°$ נגד כיוון השעון. בסיבוב זה הנקודה $(\cos\alpha, \sin\alpha)$ נשלחת לנקודה $(-\sin\alpha, \cos\alpha)$, וקואורדינטת ה-$y$ שלה — שהיא $\sin(90° + \alpha)$ — שווה $\cos\alpha$, בהתאם לתוצאה האלגברית.
