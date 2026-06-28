---
id: prf_tan_periodicity
claim_id: thm_tan_periodicity
method: informal
status: reviewed
dependencies:
- def_tan
- thm_tan_in_sin_cos
- thm_sin_addition_formula
- thm_cos_addition_formula
- thm_sin_special_values
- thm_cos_special_values
- thm_sin_double_angle
- thm_cos_double_angle
is_canonical: true
date_added: '2026-06-28T15:07:55.438051Z'
schema_version: 1
---

לפי **thm_tan_in_sin_cos** (וכן **def_tan**), עבור $\theta$ שבו $\cos\theta \neq 0$ מתקיים $\tan\theta = \dfrac{\sin\theta}{\cos\theta}$. נחשב תחילה את $\sin(\theta+\pi)$ ואת $\cos(\theta+\pi)$ באמצעות נוסחאות החיבור.

**שלב 1 — חישוב $\sin\pi$ ו-$\cos\pi$.** לפי **thm_sin_double_angle** $\sin\pi = \sin\!\left(2\cdot\tfrac{\pi}{2}\right) = 2\sin\tfrac{\pi}{2}\cos\tfrac{\pi}{2}$, ולפי **thm_sin_special_values** ו-**thm_cos_special_values** $\sin\tfrac{\pi}{2}=1$ ו-$\cos\tfrac{\pi}{2}=0$, ולכן $\sin\pi = 2\cdot 1\cdot 0 = 0$. בדומה, לפי **thm_cos_double_angle**, $\cos\pi = \cos\!\left(2\cdot\tfrac{\pi}{2}\right) = \cos^2\tfrac{\pi}{2}-\sin^2\tfrac{\pi}{2} = 0-1 = -1$.

**שלב 2 — הצבה בנוסחאות החיבור.** לפי **thm_sin_addition_formula**:
$$\sin(\theta+\pi) = \sin\theta\cos\pi + \cos\theta\sin\pi = \sin\theta\cdot(-1) + \cos\theta\cdot 0 = -\sin\theta.$$
לפי **thm_cos_addition_formula**:
$$\cos(\theta+\pi) = \cos\theta\cos\pi - \sin\theta\sin\pi = \cos\theta\cdot(-1) - \sin\theta\cdot 0 = -\cos\theta.$$

**שלב 3 — חישוב $\tan(\theta+\pi)$.** הואיל ו-$\cos\theta\neq 0$, גם $\cos(\theta+\pi) = -\cos\theta\neq 0$, ולכן $\tan(\theta+\pi)$ מוגדר. לפי **thm_tan_in_sin_cos**:
$$\tan(\theta+\pi) = \frac{\sin(\theta+\pi)}{\cos(\theta+\pi)} = \frac{-\sin\theta}{-\cos\theta} = \frac{\sin\theta}{\cos\theta} = \tan\theta.$$

**שלב 4 — מינימליות המחזור.** הראינו ש-$\pi$ הוא מחזור. הוא גם המחזור היסודי: $\tan 0 = 0$, ואילו עבור $0<t<\pi$ מתקיים $\sin t > 0$ ולכן $\tan t \neq 0$ כל עוד $\cos t \neq 0$, כך שאין מחזור חיובי קטן מ-$\pi$. $\blacksquare$
