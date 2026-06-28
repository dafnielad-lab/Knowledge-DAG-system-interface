---
id: prf_liouville
claim_id: thm_liouville
method: informal
status: reviewed
dependencies:
- def_modulus_complex
- def_complex_number
- def_derivative_at_point
- def_definite_integral
is_canonical: true
date_added: '2026-06-28T15:07:55.432049Z'
schema_version: 1
---

**הוכחה (באמצעות הערכת קושי).**

תהי $z_0 \in \mathbb{C}$ נקודה כלשהי. נראה ש-$f'(z_0) = 0$; מכיוון ש-$z_0$ שרירותית, תינבע מכך קביעות של $f$ (פונקציה אנליטית עם נגזרת מתאפסת זהותית במישור הקשיר $\mathbb{C}$ היא קבועה).

**שלב 1 — נוסחת קושי לנגזרת.** מאחר ש-$f$ אנליטית בכל המישור, לכל $R > 0$ המעגל $C_R = \{ z : |z - z_0| = R \}$ מוכל בתחום האנליטיות, ולכן מתקיימת נוסחת האינטגרל של קושי לנגזרת הראשונה:
$$f'(z_0) = \frac{1}{2\pi i} \oint_{C_R} \frac{f(\zeta)}{(\zeta - z_0)^2} \, d\zeta.$$
(זהו אינטגרל קווי במובן המוגדר ב-`def_definite_integral`, מורחב למישור המרוכב; הנגזרת $f'(z_0)$ מתבססת על `def_derivative_at_point` בגרסתה המרוכבת.)

**שלב 2 — הערכת המודולוס.** על המעגל $C_R$ מתקיים $|\zeta - z_0| = R$, ולכן $|(\zeta - z_0)^2| = R^2$ (על-פי תכונת הכפליות של המודולוס מ-`def_modulus_complex`). מההנחה $|f(\zeta)| \leq M$ נקבל לכל $\zeta \in C_R$:
$$\left| \frac{f(\zeta)}{(\zeta - z_0)^2} \right| \leq \frac{M}{R^2}.$$
אורך המסלול $C_R$ הוא $2\pi R$, ולכן מאי-שוויון ה-ML הסטנדרטי לאינטגרלים קוויים:
$$|f'(z_0)| = \left| \frac{1}{2\pi i} \oint_{C_R} \frac{f(\zeta)}{(\zeta - z_0)^2} \, d\zeta \right| \leq \frac{1}{2\pi} \cdot \frac{M}{R^2} \cdot 2\pi R = \frac{M}{R}.$$

**שלב 3 — שאיפת $R$ לאינסוף.** הביטוי $M/R$ אינו תלוי ב-$z_0$, ומכיוון ש-$f$ שלמה רשאים לבחור $R$ גדול ככל שנרצה. מקבלים
$$|f'(z_0)| \leq \lim_{R \to \infty} \frac{M}{R} = 0,$$
ולכן $f'(z_0) = 0$.

**שלב 4 — מסקנה.** $z_0$ הייתה שרירותית, אז $f' \equiv 0$ במישור. עבור $z_1, z_2 \in \mathbb{C}$ נסמן $\gamma(t) = z_1 + t(z_2 - z_1)$, $t \in [0,1]$ — קטע ישר המחבר אותן (מוגדר היטב מאחר ש-$\mathbb{C}$ כמרחב נקודות הוא $\{a + bi\}$ לפי `def_complex_number`, וקמור). אז $\frac{d}{dt} f(\gamma(t)) = f'(\gamma(t)) \cdot (z_2 - z_1) = 0$, ולכן $f(z_2) - f(z_1) = \int_0^1 \frac{d}{dt} f(\gamma(t))\, dt = 0$. כלומר $f(z_1) = f(z_2)$ לכל זוג, ו-$f$ קבועה. $\blacksquare$
