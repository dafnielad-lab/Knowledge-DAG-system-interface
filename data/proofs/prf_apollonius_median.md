---
id: prf_apollonius_median
claim_id: thm_apollonius_median
method: informal
status: reviewed
dependencies:
- thm_law_of_cosines
- def_centroid
is_canonical: true
date_added: '2026-06-27T18:47:27.564532Z'
schema_version: 1
---

**הוכחה (קוסינוסים).** $M$ אמצע $BC$, $BM = MC = a/2$. במשולש $ABM$ ו-$ACM$ נשתמש בקוסינוסים על הזוויות ב-$M$ (שהן משלימות).

$c^2 = m_a^2 + (a/2)^2 - a m_a \cos\theta$

$b^2 = m_a^2 + (a/2)^2 + a m_a \cos\theta$

חיבור: $b^2 + c^2 = 2m_a^2 + a^2/2$, כלומר $m_a = \frac{1}{2}\sqrt{2b^2 + 2c^2 - a^2}$. $\blacksquare$
