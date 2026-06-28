---
id: prf_alternate_interior_angles
claim_id: thm_alternate_interior_angles
method: informal
status: reviewed
dependencies:
- def_parallel_lines
- ax_euclid_parallel_postulate
- def_angle
is_canonical: true
date_added: '2026-06-28T15:49:27.813205Z'
schema_version: 1
---

יהיו $\ell_1 \parallel \ell_2$ שני ישרים מקבילים (לפי def_parallel_lines), ויהי $t$ חוצֶה החותך את $\ell_1$ בנקודה $A$ ואת $\ell_2$ בנקודה $B$. נסמן ב-$\alpha$ את הזווית הפנימית שהחוצֶה יוצר עם $\ell_1$ בצד אחד של $t$, וב-$\beta$ את הזווית הפנימית שהחוצֶה יוצר עם $\ell_2$ בצד הנגדי של $t$ — אלו הן הזוויות הפנימיות המתחלפות. נראה כי $\alpha = \beta$.

**שלב 1 — נניח בשלילה ש-$\alpha \ne \beta$.** ללא הגבלת הכלליות, נניח $\alpha < \beta$.

**שלב 2 — בניית ישר עזר.** דרך הנקודה $A$ נבנה ישר $\ell'$ הנוצר על ידי סיבוב $\ell_2$ (תוך שמירה על אותו זווית $\beta$ ביחס ל-$t$ באותו צד) — כלומר, $\ell'$ יוצר עם $t$ בנקודה $A$ זווית פנימית מתחלפת השווה ל-$\beta$ (לפי def_angle, ניתן להעתיק מידת זווית). אז ל-$\ell'$ ול-$\ell_2$ אותה זווית מתחלפת ביחס ל-$t$, ולכן הם מקיימים בדיוק את התנאי הסימטרי שמייצר ישרים מקבילים.

**שלב 3 — שני מקבילים שונים דרך אותה נקודה.** קיבלנו ש-$\ell' \parallel \ell_2$ (לפי ההיגיון הסימטרי לעיל), וגם $\ell_1 \parallel \ell_2$ (נתון). כלומר, דרך הנקודה $A$ (שאינה על $\ell_2$) עוברים שני ישרים שונים $\ell_1$ ו-$\ell'$ — שניהם מקבילים ל-$\ell_2$. הם שונים כי $\ell'$ יוצר זווית $\beta$ ב-$A$ עם $t$ בעוד ש-$\ell_1$ יוצר זווית $\alpha \ne \beta$.

**שלב 4 — סתירה לאקסיומת המקבילים.** לפי אקסיומת המקבילים (ax_euclid_parallel_postulate), דרך נקודה שאינה על ישר נתון, קיים ישר *יחיד* המקביל אליו. סתירה.

**מסקנה.** ההנחה $\alpha \ne \beta$ נשללת, ולכן $\alpha = \beta$. $\blacksquare$
