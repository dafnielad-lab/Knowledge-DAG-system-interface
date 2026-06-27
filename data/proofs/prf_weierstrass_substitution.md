---
id: prf_weierstrass_substitution
claim_id: thm_weierstrass_substitution
method: informal
status: reviewed
dependencies:
- def_tan
- thm_half_angle_sin
- thm_half_angle_cos
- thm_sin_double_angle
- thm_cos_double_angle
is_canonical: true
date_added: '2026-06-27T18:28:08.122596Z'
schema_version: 1
---

$\sin x = 2 \sin\frac{x}{2}\cos\frac{x}{2} = \frac{2 \sin(x/2)/\cos(x/2)}{1/\cos^2(x/2)} = \frac{2t}{1 + t^2}$ (חלוקה ב-$\cos^2$ ושימוש ב-$1 + \tan^2 = 1/\cos^2$).

בדומה $\cos x = \cos^2(x/2) - \sin^2(x/2) = \frac{1 - t^2}{1 + t^2}$.

$dx = \frac{2 \, dt}{1 + t^2}$ מגזירה $t = \tan(x/2)$. $\blacksquare$
