---
id: prf_rectangular_to_polar_complex
claim_id: thm_rectangular_to_polar_complex
method: informal
status: reviewed
dependencies:
- def_complex_number
- def_modulus_complex
- def_polar_form_complex
- def_argument_complex_number
- def_tan
- def_arctan
- thm_sin_cos_pythagorean
is_canonical: true
date_added: '2026-06-28T15:49:27.950204Z'
schema_version: 1
---

יהי $z = a + bi$ עם $z \neq 0$, כלומר $(a, b) \neq (0, 0)$.

**שלב 1: חישוב $r$.** לפי def_modulus_complex, $r := |z| = \sqrt{a^2 + b^2}$. כיוון ש-$(a,b) \neq (0,0)$, מתקיים $r > 0$.

**שלב 2: הגדרת הזווית $\theta$.** הנקודה $(a, b)$ במישור הקרטזי נמצאת במרחק $r$ מהראשית. לפי def_argument_complex_number, $\theta = \arg(z)$ היא הזווית שיוצר הוקטור $(a, b)$ עם ציר ה-$x$ החיובי. מהגיאומטריה האלמנטרית של משולש ישר זווית (או מהגדרת $\sin, \cos$ על מעגל היחידה):
$$\cos\theta = \frac{a}{r}, \quad \sin\theta = \frac{b}{r}.$$
כלומר, $a = r\cos\theta$ ו-$b = r\sin\theta$.

**שלב 3: וידוא עקביות עם זהות פיתגוראית.** לפי thm_sin_cos_pythagorean, $\sin^2\theta + \cos^2\theta = 1$. אכן:
$$\left(\frac{a}{r}\right)^2 + \left(\frac{b}{r}\right)^2 = \frac{a^2 + b^2}{r^2} = \frac{r^2}{r^2} = 1. \checkmark$$

**שלב 4: כתיבת $z$ בצורה קוטבית.** לפי def_complex_number, $z = a + bi$. הצבת $a = r\cos\theta$ ו-$b = r\sin\theta$ נותנת:
$$z = r\cos\theta + (r\sin\theta) i = r(\cos\theta + i\sin\theta),$$
וזו בדיוק הצורה הקוטבית של def_polar_form_complex.

**שלב 5: חישוב $\theta$ באמצעות $\arctan$.** כאשר $a \neq 0$, לפי def_tan, $\tan\theta = \sin\theta / \cos\theta = (b/r) / (a/r) = b/a$. לכן, אם $a > 0$ (כלומר $(a,b)$ ברביע I או IV), נקבל $\theta = \arctan(b/a)$ לפי def_arctan, שכן $\arctan$ מחזיר ערכים בטווח $(-\pi/2, \pi/2)$ המתאים לרביעים אלו.

**זהירות עם הרביע:** $\arctan(b/a)$ לבדו אינו מספיק — יש להוסיף/להחסיר $\pi$ או לטפל באופן מיוחד:
- אם $a > 0$: $\theta = \arctan(b/a)$.
- אם $a < 0, b \geq 0$: $\theta = \arctan(b/a) + \pi$.
- אם $a < 0, b < 0$: $\theta = \arctan(b/a) - \pi$.
- אם $a = 0, b > 0$: $\theta = \pi/2$.
- אם $a = 0, b < 0$: $\theta = -\pi/2$.

כך הוכחנו את ההמרה והבאנו את הנוסחאות המעשיות. $\blacksquare$
