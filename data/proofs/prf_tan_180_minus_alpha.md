---
id: prf_tan_180_minus_alpha
claim_id: thm_tan_180_minus_alpha
method: informal
status: reviewed
dependencies:
- def_tan
- thm_sin_180_minus_alpha
- thm_cos_180_minus_alpha
is_canonical: true
date_added: '2026-06-28T21:06:29.476679Z'
schema_version: 1
---

לפי הגדרת הטנגנס (def_tan), עבור כל זווית שבה הקוסינוס שונה מאפס,
$$\tan(180° - \alpha) = \frac{\sin(180° - \alpha)}{\cos(180° - \alpha)}.$$

נציב את שתי נוסחאות ההפחתה הידועות: $\sin(180° - \alpha) = \sin\alpha$ (thm_sin_180_minus_alpha) ו-$\cos(180° - \alpha) = -\cos\alpha$ (thm_cos_180_minus_alpha):
$$\tan(180° - \alpha) = \frac{\sin\alpha}{-\cos\alpha} = -\frac{\sin\alpha}{\cos\alpha}.$$

לפי הגדרת הטנגנס שוב (def_tan), $\dfrac{\sin\alpha}{\cos\alpha} = \tan\alpha$, ולכן
$$\tan(180° - \alpha) = -\tan\alpha.$$

ההנחה $\cos\alpha \neq 0$ מבטיחה שגם $\tan\alpha$ וגם $\cos(180° - \alpha) = -\cos\alpha$ מוגדרים, כך ששני האגפים מוגדרים בו-זמנית. $\blacksquare$

**הערה גאומטרית:** סימטריה ביחס לציר ה-$y$ הופכת את סימן קואורדינטת ה-$x$ ומשאירה את ה-$y$ ללא שינוי, ולכן יחס $y/x$ הופך סימן — מה שמסביר את הזהות $\tan(180° - \alpha) = -\tan\alpha$.
