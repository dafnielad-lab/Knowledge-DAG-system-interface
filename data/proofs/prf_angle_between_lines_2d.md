---
id: prf_angle_between_lines_2d
claim_id: thm_angle_between_lines_2d
method: informal
status: reviewed
dependencies:
- thm_slope_as_tan_of_inclination
- thm_slope_intercept_form
- def_tan
- thm_sin_subtraction_formula
- thm_cos_subtraction_formula
is_canonical: true
date_added: '2026-06-28T15:07:55.481050Z'
schema_version: 1
---

השיפוע של ישר הוא $m = \tan\alpha$ כאשר $\alpha$ זווית הישר עם ציר $x$. הזווית בין הישרים היא $\theta = \alpha_1 - \alpha_2$. אז $\tan\theta = \frac{\sin(\alpha_1 - \alpha_2)}{\cos(\alpha_1 - \alpha_2)} = \frac{\tan\alpha_1 - \tan\alpha_2}{1 + \tan\alpha_1 \tan\alpha_2} = \frac{m_1 - m_2}{1 + m_1 m_2}$. הערך המוחלט נותן את הזווית החדה. $\blacksquare$
