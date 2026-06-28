---
id: prf_sin_180_minus_alpha
claim_id: thm_sin_180_minus_alpha
method: informal
status: reviewed
dependencies:
- thm_sin_subtraction_formula
- thm_sin_special_values
- thm_cos_special_values
- thm_cos_addition_formula
- thm_sin_addition_formula
is_canonical: true
date_added: '2026-06-28T15:49:27.898194Z'
schema_version: 1
---

נשתמש בנוסחת החיסור לסינוס (thm_sin_subtraction_formula) עם $\alpha_0 = 180°$ ו-$\beta = \alpha$:
$$\sin(180° - \alpha) = \sin 180° \cdot \cos\alpha - \cos 180° \cdot \sin\alpha.$$

נחשב את $\sin 180°$ ו-$\cos 180°$ באמצעות הזהות $180° = 90° + 90°$ ונוסחאות החיבור (thm_sin_addition_formula, thm_cos_addition_formula) יחד עם הערכים המיוחדים (thm_sin_special_values, thm_cos_special_values):

- $\sin 180° = \sin(90° + 90°) = \sin 90° \cos 90° + \cos 90° \sin 90° = 1 \cdot 0 + 0 \cdot 1 = 0.$
- $\cos 180° = \cos(90° + 90°) = \cos 90° \cos 90° - \sin 90° \sin 90° = 0 \cdot 0 - 1 \cdot 1 = -1.$

נציב חזרה:
$$\sin(180° - \alpha) = 0 \cdot \cos\alpha - (-1) \cdot \sin\alpha = \sin\alpha.$$

זוהי הזהות המבוקשת. $\blacksquare$

**הערה גאומטרית:** על מעגל היחידה, הזוויות $\alpha$ ו-$180° - \alpha$ נותנות נקודות הסימטריות זו לזו ביחס לציר ה-$y$. שתי הנקודות חולקות אותה קואורדינטת $y$ — שהיא ערך הסינוס — ולכן $\sin(180° - \alpha) = \sin\alpha$. זו הסיבה גם לכך שבמשוואת $\sin x = a$ מתקבלים בכל מחזור שני פתרונות הקשורים על-ידי $x \mapsto 180° - x$.
