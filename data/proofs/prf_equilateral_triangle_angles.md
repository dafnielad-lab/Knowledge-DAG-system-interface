---
id: prf_equilateral_triangle_angles
claim_id: thm_equilateral_triangle_angles
method: informal
status: reviewed
dependencies:
- def_equilateral_triangle
- thm_isosceles_triangle_base_angles
- thm_triangle_angle_sum
is_canonical: true
date_added: '2026-06-28T15:49:27.822202Z'
schema_version: 1
---

יהי $\triangle ABC$ משולש שווה צלעות, כלומר $AB = BC = CA$ (לפי def_equilateral_triangle). נסמן את שלוש הזוויות הפנימיות:
$$\alpha = \angle BAC, \quad \beta = \angle ABC, \quad \gamma = \angle BCA.$$

**שלב 1 — שוויון הזוויות בזוגות.** המשולש שווה צלעות הוא בפרט שווה שוקיים בשלוש דרכים (ראה def_equilateral_triangle):

- כאשר נחשיב את $AB$ ואת $AC$ כשוקיים (השוויון $AB = AC$ מתקיים), אזי לפי משפט זוויות הבסיס במשולש שווה שוקיים (thm_isosceles_triangle_base_angles), הזוויות שמול שתי השוקיים שוות. הזווית שמול $AB$ היא $\gamma$ (ב-$C$), הזווית שמול $AC$ היא $\beta$ (ב-$B$), לכן:
$$\beta = \gamma. \qquad (1)$$

- כאשר נחשיב את $BA$ ואת $BC$ כשוקיים (השוויון $BA = BC$ מתקיים), אזי לפי thm_isosceles_triangle_base_angles, הזווית שמול $BA$ (היא $\gamma$ ב-$C$) שווה לזווית שמול $BC$ (היא $\alpha$ ב-$A$):
$$\alpha = \gamma. \qquad (2)$$

ממשוואות $(1)$ ו-$(2)$ קיבלנו:
$$\alpha = \beta = \gamma. \qquad (3)$$

**שלב 2 — שימוש בסכום הזוויות במשולש.** לפי משפט סכום הזוויות במשולש (thm_triangle_angle_sum):
$$\alpha + \beta + \gamma = 180°. \qquad (4)$$

**שלב 3 — חישוב.** מציבים $(3)$ במשוואה $(4)$:
$$\alpha + \alpha + \alpha = 3\alpha = 180°,$$
ומחלקים ב-$3$:
$$\alpha = 60°.$$

לפי $(3)$, גם $\beta = 60°$ וגם $\gamma = 60°$. לכן כל שלוש הזוויות הפנימיות במשולש שווה צלעות שוות $60°$. $\blacksquare$
