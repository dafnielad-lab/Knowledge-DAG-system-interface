---
id: prf_angle_bisector_length
claim_id: thm_angle_bisector_length
method: informal
status: reviewed
dependencies:
- thm_stewart_theorem
- thm_angle_bisectors_concur
is_canonical: true
date_added: '2026-06-27T18:48:38.235747Z'
schema_version: 1
---

**הוכחה (סטיוארט + חוצה זווית).** חוצה זווית $A$ פוגע ב-$BC$ ב-$D$ עם $BD/DC = c/b$ (משפט חוצה זווית). מכאן $BD = ac/(b+c)$, $DC = ab/(b+c)$.

הצבה במשפט סטיוארט עם $m = BD$, $n = DC$, $d = t_a$:

$b^2 \cdot \frac{ac}{b+c} + c^2 \cdot \frac{ab}{b+c} - a t_a^2 = a \cdot \frac{a^2 bc}{(b+c)^2}$

סידור: $abc(b+c)/(b+c) = abc$, ולכן $t_a^2 = bc - \frac{a^2 bc}{(b+c)^2} = bc(1 - \frac{a^2}{(b+c)^2})$. $\blacksquare$
