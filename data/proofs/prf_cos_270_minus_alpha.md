---
id: prf_cos_270_minus_alpha
claim_id: thm_cos_270_minus_alpha
method: informal
status: reviewed
dependencies:
- thm_cos_270_plus_alpha
- thm_sin_odd
is_canonical: true
date_added: '2026-06-28T21:06:29.474178Z'
schema_version: 1
---

נכתוב את הזווית $270° - \alpha$ כ-$270° + (-\alpha)$ ונפעיל את נוסחת ההפחתה $\cos(270° + \beta) = \sin\beta$ (thm_cos_270_plus_alpha) עם $\beta = -\alpha$:
$$\cos(270° - \alpha) = \cos\bigl(270° + (-\alpha)\bigr) = \sin(-\alpha).$$

כעת נשתמש בכך ש-$\sin$ היא פונקציה אי-זוגית, $\sin(-\alpha) = -\sin\alpha$ (thm_sin_odd), ונקבל:
$$\cos(270° - \alpha) = -\sin\alpha.$$

זוהי הזהות המבוקשת. $\blacksquare$

**הערה גאומטרית:** הזווית $270° - \alpha$ מתקבלת על מעגל היחידה משיקוף הנקודה של $270° + \alpha$ ביחס לציר ה-$y$, ולכן קואורדינטת ה-$x$ (ערך הקוסינוס) הופכת סימן.
