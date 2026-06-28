---
id: prf_sin_270_minus_alpha
claim_id: thm_sin_270_minus_alpha
method: informal
status: reviewed
dependencies:
- thm_sin_270_plus_alpha
- thm_cos_even
is_canonical: true
date_added: '2026-06-28T21:06:29.471178Z'
schema_version: 1
---

נכתוב את הזווית $270° - \alpha$ כ-$270° + (-\alpha)$ ונפעיל את נוסחת ההפחתה $\sin(270° + \beta) = -\cos\beta$ (thm_sin_270_plus_alpha) עם $\beta = -\alpha$:
$$\sin(270° - \alpha) = \sin\bigl(270° + (-\alpha)\bigr) = -\cos(-\alpha).$$

כעת נשתמש בכך ש-$\cos$ היא פונקציה זוגית, $\cos(-\alpha) = \cos\alpha$ (thm_cos_even), ונקבל:
$$\sin(270° - \alpha) = -\cos\alpha.$$

זוהי הזהות המבוקשת. $\blacksquare$

**הערה גאומטרית:** על מעגל היחידה, הזווית $270° - \alpha$ נמצאת ברביע השלישי כאשר $\alpha$ ברביע הראשון, ושיקוף ביחס לציר ה-$y$ של הנקודה המתאימה ל-$270°+\alpha$ אינו משנה את קואורדינטת ה-$y$ עד כדי סימן — מה שמסביר את הזהות $\sin(270° - \alpha) = -\cos\alpha$.
