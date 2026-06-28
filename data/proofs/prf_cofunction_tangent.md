---
id: prf_cofunction_tangent
claim_id: thm_cofunction_tangent
method: informal
status: reviewed
dependencies:
- def_tan
- def_secant_cosecant_cotangent
- thm_sin_complementary
is_canonical: true
date_added: '2026-06-28T20:34:16.537632Z'
schema_version: 1
---

נתון $\theta$ עם $\sin\theta \neq 0$. בפרט, $\sin\theta \neq 0$ גם מבטיח ש-$\cos(\tfrac{\pi}{2} - \theta) \neq 0$ — כי לפי `thm_sin_complementary` מתקיים $\cos(\tfrac{\pi}{2} - \theta) = \sin\theta \neq 0$. לכן הטנגנס בצד שמאל מוגדר לפי `def_tan`, וגם $\cot\theta$ מוגדר לפי `def_secant_cosecant_cotangent` (כי $\sin\theta \neq 0$).

**שלב 1 — פתיחת הטנגנס לפי הגדרתו.** לפי `def_tan`:
$$\tan\!\left(\frac{\pi}{2} - \theta\right) = \frac{\sin\!\left(\frac{\pi}{2} - \theta\right)}{\cos\!\left(\frac{\pi}{2} - \theta\right)}.$$

**שלב 2 — שימוש בזהויות המשלים.** לפי `thm_sin_complementary`:
$$\sin\!\left(\frac{\pi}{2} - \theta\right) = \cos\theta, \qquad \cos\!\left(\frac{\pi}{2} - \theta\right) = \sin\theta.$$
הצבה בשלב 1 נותנת:
$$\tan\!\left(\frac{\pi}{2} - \theta\right) = \frac{\cos\theta}{\sin\theta}.$$

**שלב 3 — זיהוי כקוטנגנס.** לפי `def_secant_cosecant_cotangent`, $\cot\theta = \dfrac{\cos\theta}{\sin\theta}$ (כל עוד $\sin\theta \neq 0$, מה שמתקיים בהנחת המשפט). ולכן
$$\tan\!\left(\frac{\pi}{2} - \theta\right) = \cot\theta. \qquad \blacksquare$$

**הערה גאומטרית.** במשולש ישר-זווית, אם $\theta$ זווית חדה, אז $\frac{\pi}{2} - \theta$ היא הזווית החדה השנייה. הטנגנס של זווית חדה הוא היחס בין הניצב שמולה לניצב שלידה; בהחלפת תפקיד הניצבים — הניצב שליד $\theta$ הופך לניצב שמול $\frac{\pi}{2} - \theta$, וההפך. לכן הטנגנס של הזווית המשלימה הוא הופכי הטנגנס של $\theta$, שזה בדיוק $\cot\theta$. זוהי הסיבה שהפונקציות $\tan$ ו-$\cot$ נקראות 'פונקציות-משלים' (cofunctions).
