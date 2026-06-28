---
id: prf_sin_complementary
claim_id: thm_sin_complementary
method: informal
status: reviewed
dependencies:
- def_sin
- def_cos
- def_unit_circle
- thm_cos_addition_formula
- thm_sin_special_values
- thm_cos_special_values
is_canonical: true
date_added: '2026-06-28T15:07:55.571550Z'
schema_version: 1
---

**הוכחה ישירה ממעגל היחידה ומנוסחת חיבור לקוסינוס** (כדי לא להישען על נוסחת חיסור לסינוס).

**שלב 1 — $\cos\!\left(\frac{\pi}{2}-\theta\right) = \sin\theta$ מנוסחת חיבור לקוסינוס.**

נכתוב $\frac{\pi}{2}-\theta = \frac{\pi}{2}+(-\theta)$ ונפעיל את נוסחת חיבור לקוסינוס:
$$\cos\!\left(\tfrac{\pi}{2}-\theta\right) = \cos\!\left(\tfrac{\pi}{2}+(-\theta)\right) = \cos\tfrac{\pi}{2}\cos(-\theta) - \sin\tfrac{\pi}{2}\sin(-\theta).$$
ממעגל היחידה, הנקודות המתאימות לזוויות $-\theta$ ו-$\theta$ הן השתקפויות זו של זו ביחס לציר ה-$x$, לכן $\cos(-\theta)=\cos\theta$ ו-$\sin(-\theta)=-\sin\theta$ (ישירות מהגדרות $\sin$, $\cos$ ומעגל היחידה). מהערכים המיוחדים $\cos\frac{\pi}{2}=0$ ו-$\sin\frac{\pi}{2}=1$ נקבל:
$$\cos\!\left(\tfrac{\pi}{2}-\theta\right) = 0\cdot\cos\theta - 1\cdot(-\sin\theta) = \sin\theta.$$

**שלב 2 — $\sin\!\left(\frac{\pi}{2}-\theta\right) = \cos\theta$ מסימטריית מעגל היחידה ביחס לישר $y=x$.**

לפי ההגדרות, הנקודה במעגל היחידה המתאימה לזווית $\theta$ היא $P_\theta=(\cos\theta,\sin\theta)$, והנקודה המתאימה לזווית $\frac{\pi}{2}-\theta$ היא $P_{\pi/2-\theta}=\bigl(\cos(\tfrac{\pi}{2}-\theta),\sin(\tfrac{\pi}{2}-\theta)\bigr)$.

השתקפות מישורית ביחס לישר $y=x$ מחליפה את הקואורדינטות: $(a,b)\mapsto(b,a)$, ובפרט שולחת את מעגל היחידה לעצמו (שכן $a^2+b^2=b^2+a^2$). תחת השתקפות זו, הזווית $\theta$ הנמדדת מהציר החיובי של $x$ הופכת לזווית המשלימה $\frac{\pi}{2}-\theta$ הנמדדת מאותו ציר, שכן הישר $y=x$ הוא חוצה הזווית בין הציר החיובי של $x$ לציר החיובי של $y$. לכן:
$$P_{\pi/2-\theta} = \text{Reflect}_{y=x}(P_\theta) = (\sin\theta,\cos\theta).$$

השוואת קואורדינטות נותנת:
$$\cos\!\left(\tfrac{\pi}{2}-\theta\right) = \sin\theta \qquad\text{ו}\qquad \sin\!\left(\tfrac{\pi}{2}-\theta\right) = \cos\theta.$$

(השוויון הראשון משחזר את שלב 1 ומאשר את העקביות; השוויון השני הוא הזהות המבוקשת.) $\blacksquare$
