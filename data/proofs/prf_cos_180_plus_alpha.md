---
id: prf_cos_180_plus_alpha
claim_id: thm_cos_180_plus_alpha
method: informal
status: reviewed
dependencies:
- thm_cos_180_minus_alpha
- thm_cos_even
is_canonical: true
date_added: '2026-06-28T21:06:29.468679Z'
schema_version: 1
---

נכתוב את הזווית $180° + \alpha$ בצורה $180° - (-\alpha)$ ונפעיל את נוסחת ההפחתה $\cos(180° - \beta) = -\cos\beta$ (thm_cos_180_minus_alpha) עם $\beta = -\alpha$:
$$\cos(180° + \alpha) = \cos\bigl(180° - (-\alpha)\bigr) = -\cos(-\alpha).$$

כעת נשתמש בכך ש-$\cos$ היא פונקציה זוגית, $\cos(-\alpha) = \cos\alpha$ (thm_cos_even), ונקבל:
$$\cos(180° + \alpha) = -\cos\alpha.$$

זוהי הזהות המבוקשת. $\blacksquare$

**הערה גאומטרית:** הזוויות $\alpha$ ו-$180° + \alpha$ נותנות על מעגל היחידה נקודות הסימטריות זו לזו ביחס לראשית הצירים, כך שקואורדינטת ה-$x$ (ערך הקוסינוס) הופכת סימן.
