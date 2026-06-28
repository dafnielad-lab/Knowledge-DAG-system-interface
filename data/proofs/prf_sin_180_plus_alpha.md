---
id: prf_sin_180_plus_alpha
claim_id: thm_sin_180_plus_alpha
method: informal
status: reviewed
dependencies:
- thm_sin_180_minus_alpha
- thm_sin_odd
is_canonical: true
date_added: '2026-06-28T21:06:29.466178Z'
schema_version: 1
---

נכתוב את הזווית $180° + \alpha$ בצורה $180° - (-\alpha)$ ונפעיל את נוסחת ההפחתה $\sin(180° - \beta) = \sin\beta$ (thm_sin_180_minus_alpha) עם $\beta = -\alpha$:
$$\sin(180° + \alpha) = \sin\bigl(180° - (-\alpha)\bigr) = \sin(-\alpha).$$

כעת נשתמש בכך ש-$\sin$ היא פונקציה אי-זוגית, $\sin(-\alpha) = -\sin\alpha$ (thm_sin_odd), ונקבל:
$$\sin(180° + \alpha) = -\sin\alpha.$$

זוהי הזהות המבוקשת. $\blacksquare$

**הערה גאומטרית:** על מעגל היחידה, הזוויות $\alpha$ ו-$180° + \alpha$ נותנות נקודות הסימטריות זו לזו ביחס לראשית הצירים. לכן שתי הקואורדינטות מתחלפות בסימן, ובפרט קואורדינטת ה-$y$ (שהיא ערך הסינוס) הופכת סימן.
