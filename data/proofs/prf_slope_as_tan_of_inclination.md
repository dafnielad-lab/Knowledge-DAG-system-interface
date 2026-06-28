---
id: prf_slope_as_tan_of_inclination
claim_id: thm_slope_as_tan_of_inclination
method: informal
status: reviewed
dependencies:
- def_slope_between_points
- def_sin
- def_cos
- def_tan
is_canonical: true
date_added: '2026-06-28T15:07:55.453051Z'
schema_version: 1
---

יהי $\ell$ ישר שאינו אנכי במישור. נבחר על $\ell$ נקודה כלשהי $P_0 = (x_0, y_0)$, ונסמן ב-$\alpha$ את זווית ההטיה של $\ell$ — הזווית בין הכיוון החיובי של ציר $x$ לבין $\ell$, נמדדת נגד כיוון השעון. מאחר ש-$\ell$ אינו אנכי, $\alpha \neq \pi/2$, ולכן $\cos\alpha \neq 0$ והביטוי $\tan\alpha = \frac{\sin\alpha}{\cos\alpha}$ (לפי def_tan) מוגדר.

נתבונן בנקודה $P_1$ המתקבלת מ-$P_0$ על ידי תזוזה באורך יחידה בכיוון $\ell$ (בכיוון שמשמר את הזווית $\alpha$). על פי הגדרת הסינוס והקוסינוס במעגל היחידה (def_sin ו-def_cos), וקטור היחידה בכיוון שיוצר זווית $\alpha$ עם הכיוון החיובי של ציר $x$ הוא $(\cos\alpha, \sin\alpha)$. לכן
$$P_1 = (x_0 + \cos\alpha,\ y_0 + \sin\alpha).$$

הנקודות $P_0$ ו-$P_1$ שונות (כי וקטור היחידה אינו אפס) ושייכות לישר $\ell$. בנוסף, $x_1 - x_0 = \cos\alpha \neq 0$, ולכן מותר להפעיל את הגדרת השיפוע בין שתי נקודות (def_slope_between_points):
$$m = \frac{y_1 - y_0}{x_1 - x_0} = \frac{\sin\alpha}{\cos\alpha}.$$

לפי def_tan, האגף הימני הוא בדיוק $\tan\alpha$, ולכן
$$m = \tan\alpha.$$

שיפוע של ישר אינו תלוי בבחירת שתי הנקודות עליו (זוהי תכונה ידועה הנובעת מדמיון משולשים, ומובנית בהגדרה def_slope_between_points כאשר היא מיושמת על ישר), כך שהזהות שהוכחה אינה תלויה בבחירת $P_0$ ובכיוון התזוזה. $\blacksquare$
