---
id: prf_argument_complex_number
claim_id: def_argument_complex_number
method: informal
status: reviewed
dependencies:
- def_complex_number
- def_modulus_complex
- def_polar_form_complex
is_canonical: true
date_added: '2026-06-28T15:49:27.947195Z'
schema_version: 1
---

מוטיבציה והגדרה מפורטת: לפי def_complex_number, מספר מרוכב $z = a + bi$ מזוהה עם הנקודה $(a, b)$ במישור הקרטזי הקרוי המישור המרוכב (ציר $x$ — ממשי, ציר $y$ — דמיוני).

לפי def_modulus_complex, $|z| = \sqrt{a^2 + b^2}$ הוא המרחק של הנקודה מהראשית. עבור $z \neq 0$ מתקיים $|z| > 0$.

הנקודה $(a, b)$ במישור ניתנת לתיאור לא רק ע"י הקואורדינטות הקרטזיות $(a, b)$ אלא גם ע"י הקואורדינטות הקוטביות $(r, \theta)$, כאשר $r = |z|$ הוא המרחק מהראשית ו-$\theta$ הוא הזווית שעושה הקרן מהראשית אל $(a, b)$ עם הכיוון החיובי של ציר ה-$x$.

**הגדרת הארגומנט הראשי:** ה-$\theta$ הזה אינו יחיד — הזוויות $\theta, \theta + 2\pi, \theta - 2\pi, \ldots$ כולן מתארות את אותה נקודה. כדי לקבל ערך יחיד, מסכמים על בחירה של **ערך ראשי** (principal value), בדרך כלל $\theta \in (-\pi, \pi]$ (לעיתים $[0, 2\pi)$). אז $\arg(z)$ מוגדר היטב לכל $z \neq 0$.

**עבור $z = 0$:** הארגומנט אינו מוגדר, כי הנקודה $(0,0)$ אינה מגדירה כיוון.

**קשר לצורה הקוטבית:** לפי def_polar_form_complex, $z = r(\cos\theta + i\sin\theta)$ עבור $r = |z|$ ו-$\theta = \arg(z)$. כך הארגומנט והמודולוס יחד נותנים ייצוג חד-משמעי של $z$ (עד כדי $2\pi$-מחזוריות בארגומנט).

**תכונות בסיסיות:** עבור $z_1, z_2 \neq 0$ מתקיים $\arg(z_1 z_2) = \arg(z_1) + \arg(z_2) \pmod{2\pi}$ ו-$\arg(z_1/z_2) = \arg(z_1) - \arg(z_2) \pmod{2\pi}$ — תכונות הנגזרות מתכונות הצורה הקוטבית. $\blacksquare$
