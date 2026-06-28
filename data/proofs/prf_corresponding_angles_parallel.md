---
id: prf_corresponding_angles_parallel
claim_id: thm_corresponding_angles_parallel
method: informal
status: reviewed
dependencies:
- def_parallel_lines
- thm_alternate_interior_angles
- def_angle
is_canonical: true
date_added: '2026-06-28T15:49:27.816694Z'
schema_version: 1
---

יהיו $\ell_1 \parallel \ell_2$ (לפי def_parallel_lines), ויהי $t$ חוצה אותם, חותך את $\ell_1$ בנקודה $A$ ואת $\ell_2$ בנקודה $B$. בנקודת החיתוך $A$ נוצרות ארבע זוויות; נסמן ב-$\gamma$ זווית מתאימה אחת — למשל, הזווית מעל $\ell_1$ ובימין $t$ (בכיוון $B$). בנקודת החיתוך $B$ נסמן ב-$\gamma'$ את הזווית המתאימה — הזווית מעל $\ell_2$ ובימין $t$ (באותו צד). נראה כי $\gamma = \gamma'$.

**שלב 1 — קיום של זווית מתחלפת ב-$A$.** הזווית הסמוכה ל-$\gamma$ באותה נקודה $A$, הנמצאת מתחת ל-$\ell_1$ ובימין $t$, נסמן ב-$\alpha$. שתי הזוויות $\gamma$ ו-$\alpha$ הן זוויות צמודות לאורך הישר $\ell_1$, ולפי def_angle הזוויות הצמודות על ישר מסכמות $180°$:
$$\gamma + \alpha = 180°. \qquad (1)$$
אך גם, הזוויות $\gamma$ ו-$\alpha$ הן זוויות קודקודיות-נגדיות (vertically opposite) ביחס לנקודה $A$: זוג קרניים מנוגדות של $t$ עם זוג קרניים מנוגדות של $\ell_1$. ליתר דיוק, הזווית $\alpha$ ש-מתחת ל-$\ell_1$ ובימין $t$ שווה לזווית $\alpha$ שמעל $\ell_1$ ובשמאל $t$ (זוויות קודקודיות). אבל הזווית מעל $\ell_1$ ובשמאל $t$ היא דווקא הזווית הפנימית המתחלפת ל-$\gamma'$.

ניסוח פשוט יותר: נסמן ב-$\delta$ את הזווית הפנימית בנקודה $A$, מתחת ל-$\ell_1$ ובשמאל $t$. אז $\delta$ ו-$\gamma$ הן זוויות קודקודיות נגדיות (נוצרות על ידי שני זוגות קרניים מנוגדים) ולכן $\delta = \gamma$.

**שלב 2 — הפעלת זוויות מתחלפות.** הזווית $\delta$ (פנימית, ב-$A$, מתחת ל-$\ell_1$, בשמאל $t$) והזווית הפנימית ב-$B$ הנמצאת מעל $\ell_2$ ובימין $t$ — הן זוויות פנימיות מתחלפות ביחס לחוצֶה $t$. אבל זווית זו ב-$B$ היא בדיוק $\gamma'$ (לפי הגדרת הזווית המתאימה שלקחנו). לפי thm_alternate_interior_angles, $\delta = \gamma'$.

**שלב 3 — שרשור.** משילוב הצעדים: $\gamma = \delta = \gamma'$, ולכן $\gamma = \gamma'$. $\blacksquare$
