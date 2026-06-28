---
id: prf_trig_substitution_integration
claim_id: thm_trig_substitution_integration
method: informal
status: reviewed
dependencies:
- def_trig_substitution
- thm_integral_substitution
- thm_sin_cos_pythagorean
- def_indefinite_integral
- def_tan
is_canonical: true
date_added: '2026-06-28T15:49:27.953202Z'
schema_version: 1
---

השיטה מבוססת על שילוב של thm_integral_substitution (אינטגרציה בהצבה) עם זהות פיתגוראית להעלמת השורש. נוכיח לכל אחד משלושת המקרים המוכרים.

**מקרה I: $\sqrt{a^2 - x^2}$ — הצבה $x = a\sin\theta$, $\theta \in [-\pi/2, \pi/2]$.** לפי def_trig_substitution.

- $dx = a\cos\theta \, d\theta$.
- $a^2 - x^2 = a^2 - a^2\sin^2\theta = a^2(1 - \sin^2\theta)$.
- לפי thm_sin_cos_pythagorean: $1 - \sin^2\theta = \cos^2\theta$, אז $a^2 - x^2 = a^2\cos^2\theta$.
- $\sqrt{a^2 - x^2} = a|\cos\theta| = a\cos\theta$ (כי $\cos\theta \geq 0$ בטווח שנבחר).

לפי thm_integral_substitution, $\int f(x)\,dx = \int f(a\sin\theta) \cdot a\cos\theta\, d\theta$. דוגמה: $\int \sqrt{a^2 - x^2}\, dx = \int a\cos\theta \cdot a\cos\theta\, d\theta = a^2 \int \cos^2\theta\, d\theta$ — אינטגרל טריגונומטרי סטנדרטי.

**מקרה II: $\sqrt{a^2 + x^2}$ — הצבה $x = a\tan\theta$, $\theta \in (-\pi/2, \pi/2)$.**

- לפי def_tan, $\tan\theta = \sin\theta/\cos\theta$. $dx = a\sec^2\theta\, d\theta$.
- $a^2 + x^2 = a^2 + a^2\tan^2\theta = a^2(1 + \tan^2\theta)$.
- מ-thm_sin_cos_pythagorean על ידי חלוקה ב-$\cos^2\theta$: $\tan^2\theta + 1 = \sec^2\theta$, אז $a^2 + x^2 = a^2\sec^2\theta$.
- $\sqrt{a^2 + x^2} = a|\sec\theta| = a\sec\theta$ (חיובי בטווח).

ההצבה מחליפה את האינטגרל באינטגרל טריגונומטרי לפי thm_integral_substitution.

**מקרה III: $\sqrt{x^2 - a^2}$ — הצבה $x = a\sec\theta$, $\theta \in [0, \pi/2) \cup [\pi, 3\pi/2)$.**

- $dx = a\sec\theta\tan\theta\, d\theta$.
- $x^2 - a^2 = a^2\sec^2\theta - a^2 = a^2(\sec^2\theta - 1) = a^2\tan^2\theta$.
- $\sqrt{x^2 - a^2} = a|\tan\theta| = a\tan\theta$ (חיובי בטווח).

**מסקנה כללית:** בכל שלושת המקרים השורש הופך לפונקציה טריגונומטרית פשוטה ללא שורש, ו-thm_integral_substitution מבטיח שניתן לחזור לאחר חישוב לפי def_indefinite_integral, על ידי החזרה ל-$x$ באמצעות יחסים גיאומטריים במשולש עזר. $\blacksquare$
