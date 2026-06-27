---
id: prf_triangle_inequality_geometry
claim_id: thm_triangle_inequality_geometry
method: informal
status: reviewed
dependencies:
- def_triangle
- thm_isosceles_triangle_base_angles
is_canonical: true
date_added: '2026-06-27T16:03:56.115377Z'
schema_version: 1
---

במשולש $\triangle ABC$ נראה $AB + BC > AC$.

נאריך את $AB$ עד נקודה $D$ כך ש-$BD = BC$, כך ש-$AD = AB + BC$.

$\triangle BCD$ שווה שוקיים, לכן $\angle BDC = \angle BCD$. הזווית $\angle ACD$ גדולה מ-$\angle BCD = \angle BDC = \angle ADC$.

במשולש $\triangle ACD$: מול הזווית הגדולה יותר הצלע גדולה יותר. כלומר $AD > AC$, ולכן $AB + BC > AC$. $\blacksquare$
