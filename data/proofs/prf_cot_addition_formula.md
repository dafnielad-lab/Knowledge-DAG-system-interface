---
id: prf_cot_addition_formula
claim_id: thm_cot_addition_formula
method: informal
status: reviewed
dependencies:
- def_secant_cosecant_cotangent
- thm_sin_addition_formula
- thm_cos_addition_formula
is_canonical: true
date_added: '2026-06-28T15:49:27.906701Z'
schema_version: 1
---

לפי הגדרת הקוטנגנס (def_secant_cosecant_cotangent), $\cot\theta = \dfrac{\cos\theta}{\sin\theta}$ כאשר $\sin\theta \neq 0$. נכתוב:
$$\cot(\alpha + \beta) = \frac{\cos(\alpha + \beta)}{\sin(\alpha + \beta)}.$$

נציב את נוסחת החיבור לקוסינוס (thm_cos_addition_formula) במונה ואת נוסחת החיבור לסינוס (thm_sin_addition_formula) במכנה:
$$\cot(\alpha + \beta) = \frac{\cos\alpha \cos\beta - \sin\alpha \sin\beta}{\sin\alpha \cos\beta + \cos\alpha \sin\beta}.$$

כעת נחלק את המונה ואת המכנה ב-$\sin\alpha \sin\beta$, שהוא שונה מאפס לפי ההנחה:

- מונה: $\dfrac{\cos\alpha \cos\beta - \sin\alpha \sin\beta}{\sin\alpha \sin\beta} = \dfrac{\cos\alpha}{\sin\alpha} \cdot \dfrac{\cos\beta}{\sin\beta} - 1 = \cot\alpha \cot\beta - 1.$

- מכנה: $\dfrac{\sin\alpha \cos\beta + \cos\alpha \sin\beta}{\sin\alpha \sin\beta} = \dfrac{\cos\beta}{\sin\beta} + \dfrac{\cos\alpha}{\sin\alpha} = \cot\beta + \cot\alpha.$

לכן:
$$\cot(\alpha + \beta) = \frac{\cot\alpha \cot\beta - 1}{\cot\alpha + \cot\beta},$$

בדיוק הזהות המבוקשת. ההנחה $\sin(\alpha + \beta) \neq 0$ מבטיחה שהאגף השמאלי מוגדר; ההנחה $\sin\alpha \sin\beta \neq 0$ מבטיחה שכל אחד מ-$\cot\alpha$ ו-$\cot\beta$ מוגדר ושהמכנה החדש ($\cot\alpha + \cot\beta$) הוא $\dfrac{\sin(\alpha+\beta)}{\sin\alpha\sin\beta} \neq 0$. $\blacksquare$
