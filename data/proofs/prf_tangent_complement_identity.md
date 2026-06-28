---
id: prf_tangent_complement_identity
claim_id: thm_tangent_complement_identity
method: informal
status: reviewed
dependencies:
- def_tan
- def_secant_cosecant_cotangent
- thm_sin_addition_formula
- thm_cos_addition_formula
- thm_sin_special_values
- thm_cos_special_values
is_canonical: true
date_added: '2026-06-28T15:07:55.447049Z'
schema_version: 1
---

נחשב את $\sin\!\left(\alpha + \tfrac{\pi}{2}\right)$ ואת $\cos\!\left(\alpha + \tfrac{\pi}{2}\right)$ באמצעות נוסחאות החיבור, ואז נחלק לפי הגדרת הטנגנס.

**שלב 1 — חישוב המונה.** לפי `thm_sin_addition_formula`,
$$\sin\!\left(\alpha + \tfrac{\pi}{2}\right) = \sin\alpha\cos\tfrac{\pi}{2} + \cos\alpha\sin\tfrac{\pi}{2}.$$
מ-`thm_cos_special_values` נקבל $\cos\tfrac{\pi}{2} = 0$, ומ-`thm_sin_special_values` נקבל $\sin\tfrac{\pi}{2} = 1$. הצבה נותנת
$$\sin\!\left(\alpha + \tfrac{\pi}{2}\right) = \sin\alpha \cdot 0 + \cos\alpha \cdot 1 = \cos\alpha.$$

**שלב 2 — חישוב המכנה.** לפי `thm_cos_addition_formula`,
$$\cos\!\left(\alpha + \tfrac{\pi}{2}\right) = \cos\alpha\cos\tfrac{\pi}{2} - \sin\alpha\sin\tfrac{\pi}{2}.$$
שוב באמצעות הערכים המיוחדים $\cos\tfrac{\pi}{2}=0$ ו-$\sin\tfrac{\pi}{2}=1$ מ-`thm_cos_special_values` ו-`thm_sin_special_values` מתקבל
$$\cos\!\left(\alpha + \tfrac{\pi}{2}\right) = \cos\alpha \cdot 0 - \sin\alpha \cdot 1 = -\sin\alpha.$$

**שלב 3 — הרכבה.** ההנחה $\sin\alpha \neq 0$ מבטיחה ש-$\cos\!\left(\alpha + \tfrac{\pi}{2}\right) = -\sin\alpha \neq 0$, ולכן הטנגנס מוגדר ב-$\alpha + \tfrac{\pi}{2}$. לפי `def_tan`,
$$\tan\!\left(\alpha + \tfrac{\pi}{2}\right) = \frac{\sin\!\left(\alpha + \tfrac{\pi}{2}\right)}{\cos\!\left(\alpha + \tfrac{\pi}{2}\right)} = \frac{\cos\alpha}{-\sin\alpha} = -\frac{\cos\alpha}{\sin\alpha}.$$

לפי `def_secant_cosecant_cotangent` מתקיים $\cot\alpha = \dfrac{\cos\alpha}{\sin\alpha}$ (מוגדר כי $\sin\alpha \neq 0$), ולכן
$$\tan\!\left(\alpha + \tfrac{\pi}{2}\right) = -\cot\alpha. \qquad \blacksquare$$
