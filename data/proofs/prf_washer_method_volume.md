---
id: prf_washer_method_volume
claim_id: thm_washer_method_volume
method: informal
status: reviewed
dependencies:
- def_volume_of_revolution
- thm_volume_of_revolution_disc
- thm_definite_integral_linearity
- def_definite_integral
is_canonical: true
date_added: '2026-06-28T20:34:16.574209Z'
schema_version: 1
---

נסמן ב-$V_f$ את נפח גוף הסיבוב של $f$ סביב ציר $x$ ב-$[a,b]$, וב-$V_g$ את נפח גוף הסיבוב של $g$. מאחר ש-$g(x) \leq f(x)$, האזור הסיבובי של $g$ מוכל באזור הסיבובי של $f$ (לפי `def_volume_of_revolution`), והנפח הנדרש הוא ההפרש:

$$V = V_f - V_g.$$

לפי `thm_volume_of_revolution_disc`:

$$V_f = \pi \int_a^b f(x)^2 \, dx, \qquad V_g = \pi \int_a^b g(x)^2 \, dx.$$

על פי `thm_definite_integral_linearity` (הוצאת קבוע וחיבור אינטגרלים על אותו תחום):

$$V = \pi \int_a^b f(x)^2 \, dx - \pi \int_a^b g(x)^2 \, dx = \pi \int_a^b \left[ f(x)^2 - g(x)^2 \right] dx.$$

גיאומטרית, בעובי $\Delta x$ בנקודה $x$ נחתכת "טבעת" (annulus) עם רדיוס חיצוני $f(x)$ ורדיוס פנימי $g(x)$, ושטחה $\pi[f(x)^2 - g(x)^2]$; הגדרת `def_definite_integral` כסכום רימן של נפחי הטבעות הדקות $\pi[f(x)^2 - g(x)^2]\Delta x$ מובילה בדיוק לאינטגרל זה. $\blacksquare$
