---
id: prf_cot_double_angle
claim_id: thm_cot_double_angle
method: informal
status: reviewed
dependencies:
- thm_cot_addition_formula
is_canonical: true
date_added: '2026-06-28T15:49:27.909205Z'
schema_version: 1
---

ניישם את נוסחת החיבור לקוטנגנס (thm_cot_addition_formula) במקרה הפרטי $\beta = \alpha$. ההנחה $\sin 2\alpha \neq 0$ שקולה לכך ש-$2\sin\alpha\cos\alpha \neq 0$, ולכן $\sin\alpha \neq 0$ וגם $\cos\alpha \neq 0$. בפרט, $\sin\alpha \sin\alpha = \sin^2\alpha \neq 0$ ו-$\sin(\alpha + \alpha) = \sin 2\alpha \neq 0$, כך שתנאי הנוסחה מתקיימים.

מהנוסחה:
$$\cot(\alpha + \alpha) = \frac{\cot\alpha \cdot \cot\alpha - 1}{\cot\alpha + \cot\alpha} = \frac{\cot^2\alpha - 1}{2\cot\alpha}.$$

והאגף השמאלי הוא בדיוק $\cot 2\alpha$. לכן:
$$\cot 2\alpha = \frac{\cot^2\alpha - 1}{2\cot\alpha},$$

כפי שנדרש. $\blacksquare$

**הערה:** הנוסחה ניתנת להפיק גם ישירות: $\cot 2\alpha = \dfrac{\cos 2\alpha}{\sin 2\alpha} = \dfrac{\cos^2\alpha - \sin^2\alpha}{2\sin\alpha \cos\alpha}$, וחלוקת מונה ומכנה ב-$\sin^2\alpha$ נותנת את אותה תוצאה — אבל ההפקה מנוסחת החיבור לקוטנגנס היא ישירה וקצרה יותר.
