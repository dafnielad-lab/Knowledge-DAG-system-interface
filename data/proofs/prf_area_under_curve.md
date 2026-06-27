---
id: prf_area_under_curve
claim_id: thm_area_under_curve
method: informal
status: reviewed
dependencies:
- def_definite_integral
- def_riemann_sum
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

סכום רימן עבור $f \geq 0$ הוא בדיוק סכום שטחים של מלבנים שמכוסים בין הגרף לציר $x$.

ככל שהחלוקה נעשית עדינה יותר ($\Delta x \to 0$), הסכום מתכנס לשטח המדויק תחת הגרף, שזה $\int_a^b f(x) \, dx$. $\blacksquare$
