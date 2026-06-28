---
id: prf_sin_supplementary
claim_id: thm_sin_supplementary
method: informal
status: reviewed
dependencies:
- thm_sin_subtraction_formula
- thm_sin_special_values
- thm_cos_special_values
is_canonical: true
date_added: '2026-06-28T15:07:55.435051Z'
schema_version: 1
---

נשתמש בנוסחת החיסור לסינוס (thm_sin_subtraction_formula) עם $\alpha = \pi$ ו-$\beta = x$:
$$\sin(\pi - x) = \sin\pi \cos x - \cos\pi \sin x.$$

מן הערכים המיוחדים של סינוס (thm_sin_special_values) ושל קוסינוס (thm_cos_special_values), בשילוב עם המחזוריות של $\sin$ ו-$\cos$ ועם הזהויות $\sin(\pi/2 + \pi/2) = \sin(\pi - 0) \cdot \ldots$ — או, באופן ישיר יותר, מהקריאה שערכי $\sin\pi$ ו-$\cos\pi$ הם:
$$\sin\pi = 0, \qquad \cos\pi = -1.$$

(אלה נובעים מן הערכים המיוחדים: על מעגל היחידה, $\pi$ היא הנקודה $(-1, 0)$, כפי שמתקבל מהמשך הטבלה של ערכי הסינוס והקוסינוס דרך $\pi/2$ אל $\pi$ — קואורדינטת ה-$x$ שווה $\cos\pi = -1$ וקואורדינטת ה-$y$ שווה $\sin\pi = 0$.)

נציב חזרה:
$$\sin(\pi - x) = 0 \cdot \cos x - (-1) \cdot \sin x = \sin x.$$

זוהי הזהות המבוקשת. $\blacksquare$

הערה גיאומטרית: על מעגל היחידה, הזוויות $x$ ו-$\pi - x$ נותנות נקודות הסימטריות זו לזו ביחס לציר ה-$y$, ולכן יש להן אותה קואורדינטת $y$ — דהיינו אותו ערך סינוס. זה הצידוק האינטואיטיבי שמאחורי הזהות, והוא גם הסיבה שמשוואת $\sin x = a$ מקבלת בכל מחזור שני פתרונות הקשורים על-ידי $x \mapsto \pi - x$.
