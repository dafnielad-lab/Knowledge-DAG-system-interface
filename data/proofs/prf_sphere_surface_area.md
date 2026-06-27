---
id: prf_sphere_surface_area
claim_id: thm_sphere_surface_area
method: informal
status: reviewed
dependencies:
- def_sphere
- thm_sphere_volume
- def_definite_integral
is_canonical: true
date_added: '2026-06-27T18:26:22.743198Z'
schema_version: 1
---

**גישת אינטגרל:** סובבים חצי מעגל $y = \sqrt{R^2 - x^2}$ סביב ציר $x$. שטח פני סיבוב: $A = 2\pi \int_{-R}^R y \sqrt{1 + (y')^2} dx$.

חישוב $y' = \frac{-x}{\sqrt{R^2 - x^2}}$, ולכן $\sqrt{1 + (y')^2} = \frac{R}{y}$. הצבה: $A = 2\pi \int_{-R}^R y \cdot \frac{R}{y} dx = 2\pi R \cdot 2R = 4\pi R^2$. $\blacksquare$
