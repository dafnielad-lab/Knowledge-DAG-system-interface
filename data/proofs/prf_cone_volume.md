---
id: prf_cone_volume
claim_id: thm_cone_volume
method: informal
status: reviewed
dependencies:
- def_cone
- thm_volume_of_revolution_disc
is_canonical: true
date_added: '2026-06-27T16:34:26.423690Z'
schema_version: 1
---

חרוט גובה $h$ ורדיוס בסיס $r$ הוא גוף הסיבוב של משולש ישר-זווית. גרף הצלע: $f(x) = \frac{r x}{h}$ ב-$[0, h]$.

$V = \pi \int_0^h \left(\frac{r x}{h}\right)^2 \, dx = \frac{\pi r^2}{h^2} \cdot \frac{x^3}{3}\Big|_0^h = \frac{\pi r^2 h}{3}$. $\blacksquare$
