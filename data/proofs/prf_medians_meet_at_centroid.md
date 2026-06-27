---
id: prf_medians_meet_at_centroid
claim_id: thm_medians_meet_at_centroid
method: informal
status: reviewed
dependencies:
- def_centroid
- def_triangle
- thm_aa_similarity
is_canonical: true
date_added: '2026-06-27T17:22:39.263705Z'
schema_version: 1
---

ניקח שני תיכונים $AM, BN$ במשולש $\triangle ABC$, נסמן את נקודת חיתוכם $G$.

**גישה וקטורית:** מציבים את הקודקודים כווקטורים $\vec{A}, \vec{B}, \vec{C}$. אמצע $BC$ הוא $\vec{M} = \frac{\vec{B} + \vec{C}}{2}$. נקודה על תיכון $AM$: $\vec{A} + t(\vec{M} - \vec{A})$. חיתוך עם תיכון $BN$ נותן $\vec{G} = \frac{\vec{A} + \vec{B} + \vec{C}}{3}$.

לפי הסימטריה, גם התיכון השלישי עובר דרך $G$. יחס החלוקה $AG:GM = 2:1$ מקבלים מ-$t = \tfrac{2}{3}$. $\blacksquare$
