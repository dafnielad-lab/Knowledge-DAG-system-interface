---
id: prf_exterior_angle
claim_id: thm_exterior_angle
method: informal
status: reviewed
dependencies:
- thm_triangle_angle_sum
- def_triangle
- def_angle
is_canonical: true
date_added: '2026-06-28T15:07:55.441051Z'
schema_version: 1
---

יהי $\triangle ABC$ משולש כלשהו (לפי def_triangle), ונאריך את הצלע $BC$ מעבר לקודקוד $C$ אל נקודה $D$ כך ש-$B$, $C$, $D$ נמצאות על ישר אחד באותו סדר.

נסמן את שלוש הזוויות הפנימיות של המשולש:
$$\alpha = \angle BAC, \qquad \beta = \angle ABC, \qquad \gamma = \angle BCA.$$

הזווית $\angle ACD$ היא הזווית החיצונית של המשולש בקודקוד $C$, ביחס להארכת הצלע $BC$.

**שלב 1 — זוויות צמודות על ישר.** מאחר ש-$B$, $C$, $D$ נמצאות על ישר אחד, הקרניים $CB$ ו-$CD$ הן קרניים מנוגדות היוצאות מ-$C$. הקרן $CA$ יוצרת איתן שתי זוויות צמודות שמרכיבות יחד את הזווית השטוחה שמעל הישר $BD$. לפי המידה של זווית (def_angle), זווית שטוחה היא $180°$, ולכן:
$$\gamma + \angle ACD = \angle BCA + \angle ACD = 180°. \qquad (*)$$

**שלב 2 — סכום זוויות פנימיות במשולש.** לפי משפט סכום זוויות במשולש (thm_triangle_angle_sum), שלוש הזוויות הפנימיות של $\triangle ABC$ סוכמות ל-$180°$:
$$\alpha + \beta + \gamma = 180°. \qquad (**)$$

**שלב 3 — השוואת המשוואות.** מהמשוואות $(*)$ ו-$(**)$ מקבלים אגף שווה לאגף:
$$\gamma + \angle ACD = \alpha + \beta + \gamma.$$

נחסר $\gamma$ משני האגפים:
$$\angle ACD = \alpha + \beta = \angle BAC + \angle ABC.$$

קיבלנו שהזווית החיצונית בקודקוד $C$ שווה לסכום שתי הזוויות הפנימיות שאינן צמודות לה — הזוויות בקודקודים $A$ ו-$B$. $\blacksquare$
