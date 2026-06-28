---
id: prf_cos_180_minus_alpha
claim_id: thm_cos_180_minus_alpha
method: informal
status: reviewed
dependencies:
- thm_cos_subtraction_formula
- thm_sin_special_values
- thm_cos_special_values
is_canonical: true
date_added: '2026-06-28T15:49:27.895200Z'
schema_version: 1
---

נשתמש בנוסחת החיסור לקוסינוס (thm_cos_subtraction_formula) עם $\alpha_0 = 180°$ ו-$\beta = \alpha$:
$$\cos(180° - \alpha) = \cos 180° \cdot \cos\alpha + \sin 180° \cdot \sin\alpha.$$

כדי לחשב את $\cos 180°$ ו-$\sin 180°$, נשתמש שוב בנוסחאות החיבור עם $180° = 90° + 90°$:

- $\cos 180° = \cos(90°+90°) = \cos 90° \cos 90° - \sin 90° \sin 90° = 0 \cdot 0 - 1 \cdot 1 = -1$, באמצעות הערכים המיוחדים (thm_cos_special_values, thm_sin_special_values).
- $\sin 180° = \sin(90°+90°) = \sin 90° \cos 90° + \cos 90° \sin 90° = 1 \cdot 0 + 0 \cdot 1 = 0$.

(לחילופין: על מעגל היחידה, $180°$ מתאים לנקודה $(-1, 0)$, כך ש-$\cos 180° = -1$ ו-$\sin 180° = 0$ ישירות מהגדרות $\cos$ ו-$\sin$.)

נציב חזרה:
$$\cos(180° - \alpha) = (-1) \cdot \cos\alpha + 0 \cdot \sin\alpha = -\cos\alpha.$$

זוהי הזהות המבוקשת. $\blacksquare$

**הערה גאומטרית:** הזוויות $\alpha$ ו-$180° - \alpha$ נותנות על מעגל היחידה נקודות הסימטריות זו לזו ביחס לציר ה-$y$. לכן קואורדינטות ה-$x$ שלהן (כלומר ערכי הקוסינוס) הן הפוכות זו לזו בסימן.
