---
id: prf_thales
claim_id: thm_thales
method: informal
status: reviewed
dependencies:
- def_circle
- thm_isosceles_triangle_base_angles
- thm_triangle_angle_sum
is_canonical: true
date_added: '2026-06-27T16:13:44.126814Z'
schema_version: 1
---

יהי $AB$ קוטר במעגל עם מרכז $O$, $C$ נקודה על המעגל. $OA = OB = OC$ (רדיוסים).

$\triangle OAC$ שווה שוקיים, לכן $\angle OAC = \angle OCA$. ובדומה $\angle OBC = \angle OCB$.

סכום זוויות $\triangle ABC$: $\angle A + \angle B + \angle C = (\angle OCA) + (\angle OCB) + (\angle OCA + \angle OCB) = 2(\angle OCA + \angle OCB) = 180°$.

לכן $\angle OCA + \angle OCB = 90°$, כלומר $\angle ACB = 90°$. $\blacksquare$
