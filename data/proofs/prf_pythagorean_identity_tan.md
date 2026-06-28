---
id: prf_pythagorean_identity_tan
claim_id: thm_pythagorean_identity_tan
method: informal
status: reviewed
dependencies:
- thm_sin_cos_pythagorean
- def_tan
is_canonical: true
date_added: '2026-06-28T15:07:55.450051Z'
schema_version: 1
---

נצא מהזהות הפיתגוראית הטריגונומטרית [thm_sin_cos_pythagorean]:
$$\sin^2 x + \cos^2 x = 1.$$

נניח $\cos x \neq 0$, ולכן גם $\cos^2 x \neq 0$. נחלק את שני אגפי הזהות ב-$\cos^2 x$:
$$\frac{\sin^2 x}{\cos^2 x} + \frac{\cos^2 x}{\cos^2 x} = \frac{1}{\cos^2 x}.$$

האיבר השני באגף שמאל שווה ל-$1$. באיבר הראשון נשתמש בהגדרת הטנגנס [def_tan], $\tan x = \dfrac{\sin x}{\cos x}$, ובריבוע נקבל $\tan^2 x = \dfrac{\sin^2 x}{\cos^2 x}$. נציב:
$$\tan^2 x + 1 = \frac{1}{\cos^2 x}.$$

כלומר $1 + \tan^2 x = \dfrac{1}{\cos^2 x}$, כנדרש. $\blacksquare$
