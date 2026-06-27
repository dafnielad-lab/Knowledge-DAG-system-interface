---
id: prf_sphere_volume
claim_id: thm_sphere_volume
method: informal
status: reviewed
dependencies:
- def_sphere
- thm_volume_of_revolution_disc
is_canonical: true
date_added: '2026-06-27T16:34:26.423690Z'
schema_version: 1
---

כדור ברדיוס $R$ הוא גוף הסיבוב של חצי-מעגל $f(x) = \sqrt{R^2 - x^2}$ סביב ציר $x$.

$V = \pi \int_{-R}^{R} (R^2 - x^2) \, dx = \pi \left[R^2 x - \frac{x^3}{3}\right]_{-R}^{R} = \pi \cdot \left(\frac{4 R^3}{3}\right) = \frac{4}{3}\pi R^3$. $\blacksquare$
