---
id: prf_complex_conjugate_arithmetic
claim_id: thm_complex_conjugate_arithmetic
method: informal
status: reviewed
dependencies:
- def_complex_number
- def_complex_conjugate
- def_modulus_complex
- thm_complex_multiplication
is_canonical: true
date_added: '2026-06-28T20:34:16.600252Z'
schema_version: 1
---

**הוכחה.** נכתוב $z = a + bi$ ו-$w = c + di$ עם $a, b, c, d \in \mathbb{R}$ לפי `def_complex_number`, ונשתמש בהגדרת הצמוד מ-`def_complex_conjugate`: $\bar{z} = a - bi$, $\bar{w} = c - di$.

**(א) חיבור.** $z + w = (a+c) + (b+d)i$, ולכן $\overline{z+w} = (a+c) - (b+d)i$. מאידך $\bar{z} + \bar{w} = (a - bi) + (c - di) = (a+c) - (b+d)i$. שווים. $\checkmark$

**(ב) כפל.** לפי `thm_complex_multiplication`, $z \cdot w = (ac - bd) + (ad + bc)i$, ולכן $\overline{z \cdot w} = (ac - bd) - (ad + bc)i$. מאידך, שוב לפי `thm_complex_multiplication`:

$$\bar{z} \cdot \bar{w} = (a - bi)(c - di) = (ac - (-b)(-d)) + (a \cdot (-d) + (-b) \cdot c)i = (ac - bd) - (ad + bc)i.$$

שווים. $\checkmark$

**(ג) צמוד הצמוד.** $\bar{z} = a - bi$, ולכן $\overline{\bar{z}} = a - (-b)i = a + bi = z$. $\checkmark$

**(ד) חלק ממשי ודמיוני.** $z + \bar{z} = (a+bi) + (a-bi) = 2a = 2\,\mathrm{Re}\,z$. וכן $z - \bar{z} = (a+bi) - (a-bi) = 2bi = 2i\,\mathrm{Im}\,z$. $\checkmark$

**(ה) מכפלת מספר בצמודו.** לפי `thm_complex_multiplication` עם $w = \bar{z} = a + (-b)i$:

$$z \cdot \bar{z} = (a + bi)(a - bi) = (a \cdot a - b \cdot (-b)) + (a \cdot (-b) + b \cdot a)i = (a^2 + b^2) + 0 \cdot i = a^2 + b^2.$$

לפי `def_modulus_complex`, $|z| = \sqrt{a^2 + b^2}$, ולכן $z \cdot \bar{z} = a^2 + b^2 = |z|^2$. זהו מספר ממשי אי-שלילי. $\checkmark$

**(ו) חילוק.** עבור $w \neq 0$ מתקיים $\bar{w} \neq 0$ (אחרת לפי (ג) גם $w = 0$). נסמן $q = z/w$, אזי $z = q \cdot w$. נצמיד את שני האגפים ונשתמש ב-(ב): $\bar{z} = \overline{q \cdot w} = \bar{q} \cdot \bar{w}$. נחלק ב-$\bar{w}$ (חוקי כי $\bar{w} \neq 0$): $\bar{q} = \bar{z}/\bar{w}$, כלומר $\overline{(z/w)} = \bar{z}/\bar{w}$. $\checkmark$

**מסקנה.** $z = \bar{z}$ אם ורק אם $z - \bar{z} = 0$, ולפי (ד) זה שקול ל-$2i\,\mathrm{Im}\,z = 0$, כלומר $\mathrm{Im}\,z = 0$, כלומר $z \in \mathbb{R}$. $\blacksquare$
