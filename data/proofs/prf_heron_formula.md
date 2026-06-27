---
id: prf_heron_formula
claim_id: thm_heron_formula
method: informal
status: reviewed
dependencies:
- thm_triangle_area_sin
- thm_law_of_cosines
- thm_sin_cos_pythagorean
is_canonical: true
date_added: '2026-06-27T18:26:22.743198Z'
schema_version: 1
---

מ-$S = \tfrac{1}{2} a b \sin C$ ו-$\cos C = \frac{a^2+b^2-c^2}{2ab}$ (קוסינוסים), $\sin^2 C = 1 - \cos^2 C = \frac{(2ab)^2 - (a^2+b^2-c^2)^2}{(2ab)^2}$.

פתיחה אלגברית ארוכה: $16 S^2 = 2 a^2 b^2 + 2 b^2 c^2 + 2 c^2 a^2 - a^4 - b^4 - c^4 = (a+b+c)(-a+b+c)(a-b+c)(a+b-c) = 16 s (s-a)(s-b)(s-c)$.

לכן $S = \sqrt{s(s-a)(s-b)(s-c)}$. $\blacksquare$
