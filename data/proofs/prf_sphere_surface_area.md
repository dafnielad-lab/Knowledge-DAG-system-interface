---
id: prf_sphere_surface_area
claim_id: thm_sphere_surface_area
method: informal
status: reviewed
dependencies:
- def_sphere
- thm_surface_of_revolution
- def_definite_integral
is_canonical: true
date_added: '2026-06-27T20:41:51.335588Z'
schema_version: 1
---

ניצור את הספירה כסיבוב חצי-המעגל $y = \sqrt{R^2 - x^2}$, $-R \leq x \leq R$, סביב ציר $x$.

לפי נוסחת שטח-פני-סיבוב: $S = 2\pi \int_{-R}^{R} y \sqrt{1 + (y')^2}\, dx$.

מחשבים: $y' = -\tfrac{x}{\sqrt{R^2 - x^2}}$, ולכן $1 + (y')^2 = \tfrac{R^2}{R^2 - x^2}$, ו-$\sqrt{1 + (y')^2} = \tfrac{R}{\sqrt{R^2 - x^2}}$.

$y \sqrt{1 + (y')^2} = \sqrt{R^2 - x^2} \cdot \tfrac{R}{\sqrt{R^2 - x^2}} = R$ (קבוע).

אז $S = 2\pi \int_{-R}^{R} R\, dx = 2\pi R \cdot 2R = 4\pi R^2$. $\blacksquare$
