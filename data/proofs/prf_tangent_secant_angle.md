---
id: prf_tangent_secant_angle
claim_id: thm_tangent_secant_angle
method: informal
status: reviewed
dependencies:
- thm_tangent_perpendicular_to_radius
- thm_thales
- thm_inscribed_angle_theorem
- thm_triangle_angle_sum
is_canonical: true
date_added: '2026-06-27T20:41:51.335588Z'
schema_version: 1
---

ניקח משיק $\ell$ במעגל בנקודה $T$, וחותך $TA$ (כאשר $A$ נקודה נוספת על המעגל). נסמן $\alpha$ את הזווית בין $\ell$ ל-$TA$, ונראה שהיא שווה למחצית הקשת $\widehat{TA}$ הכלואה ביניהם.

**שלב 1 — בניית עזר:** נעביר את הקוטר $TC$ דרך $T$. לפי משפט "משיק מאונך לרדיוס", $\ell \perp TC$, ולכן הזווית בין $\ell$ ל-$TC$ היא $90°$.

**שלב 2 — תאלס:** במשולש $TAC$ הצלע $TC$ קוטר, ולפי משפט תאלס $\angle TAC = 90°$.

**שלב 3 — סכום זוויות במשולש:** במשולש ישר-זווית $TAC$ עם $\angle TAC = 90°$ מתקיים $\angle ATC + \angle TCA = 90°$.

**שלב 4 — שיוויון זוויות:** הזווית בין $\ell$ ל-$TC$ היא $90°$, וזווית $\angle ATC$ נמצאת בתוכה. הזווית בין $\ell$ ל-$TA$ היא ההפרש: $\alpha = 90° - \angle ATC = \angle TCA$ (לפי שלב 3).

**שלב 5 — זווית היקפית:** $\angle TCA$ זווית היקפית הנשענת על הקשת $\widehat{TA}$. לפי משפט הזווית ההיקפית, $\angle TCA = \tfrac{1}{2} \widehat{TA}$.

**שלב 6:** ולכן $\alpha = \tfrac{1}{2} \widehat{TA}$. $\blacksquare$

*הערה:* טיעון זה לא מסתמך על משפט הזווית ההיקפית עבור הקשת $\widehat{TA}$ ישירות, אלא עבור הזווית $\angle TCA$ שאינה הזווית שבין משיק לחותך — ולכן אינו מעגלי.
