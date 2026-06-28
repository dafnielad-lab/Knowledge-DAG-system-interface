---
id: prf_distance_between_parallel_planes
claim_id: thm_distance_between_parallel_planes
method: informal
status: reviewed
dependencies:
- def_equation_of_plane
- thm_distance_point_to_plane
is_canonical: true
date_added: '2026-06-28T20:34:16.582218Z'
schema_version: 1
---

**הוכחה.** לפי `def_equation_of_plane`, וקטור הנורמל לשני המישורים הוא $\vec{n} = (a, b, c)$. מאחר ושני המישורים חולקים את אותו וקטור נורמל אך מקבועים חופשיים שונים ($d_1 \neq d_2$), הם מקבילים ולא חופפים.

נבחר נקודה כלשהי $P_0 = (x_0, y_0, z_0)$ על המישור $\Pi_1$, כלומר $a x_0 + b y_0 + c z_0 = d_1$. המרחק בין שני מישורים מקבילים שווה למרחק מנקודה כלשהי על אחד המישורים אל המישור השני (שכן המרחק נמדד לאורך הנורמל המשותף). נשתמש ב-`thm_distance_point_to_plane`:

$$d(P_0, \Pi_2) = \frac{|a x_0 + b y_0 + c z_0 - d_2|}{\sqrt{a^2 + b^2 + c^2}} = \frac{|d_1 - d_2|}{\sqrt{a^2 + b^2 + c^2}}.$$

התוצאה אינה תלויה בבחירת הנקודה $P_0$ על $\Pi_1$, ולכן מוגדרת היטב כמרחק בין שני המישורים. $\blacksquare$
