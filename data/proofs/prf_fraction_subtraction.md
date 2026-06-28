---
id: prf_fraction_subtraction
claim_id: thm_fraction_subtraction
method: informal
status: reviewed
dependencies:
- def_fraction
- def_subtraction
- thm_fraction_addition
- thm_fraction_multiplication
- thm_multiplication_by_negative_one
is_canonical: true
date_added: '2026-06-28T20:34:16.469017Z'
schema_version: 1
---

ננסח את החיסור באמצעות חיבור ונשתמש בנוסחת חיבור שברים.

לפי הגדרת חיסור (def_subtraction), $x - y := x + (-y)$ לכל מספרים ממשיים. בפרט:
$$\frac{a}{b} - \frac{c}{d} = \frac{a}{b} + \left(-\frac{c}{d}\right)$$

כעת נטען ש-$-\frac{c}{d} = \frac{-c}{d}$. לפי הגדרת שבר (def_fraction), $\frac{c}{d} = c \cdot d^{-1}$, ולפי משפט הכפל ב-$-1$ (thm_multiplication_by_negative_one), $-x = (-1) \cdot x$ לכל ממשי. לכן:
$$-\frac{c}{d} = (-1) \cdot (c \cdot d^{-1}) = ((-1) \cdot c) \cdot d^{-1} = (-c) \cdot d^{-1} = \frac{-c}{d}$$
(השתמשנו באסוציאטיביות כפל ושוב ב-thm_multiplication_by_negative_one).

לכן:
$$\frac{a}{b} - \frac{c}{d} = \frac{a}{b} + \frac{-c}{d}$$

כעת נשתמש בנוסחת חיבור שברים (thm_fraction_addition) עם $a' = a$, $b' = b$, $c' = -c$, $d' = d$:
$$\frac{a}{b} + \frac{-c}{d} = \frac{a \cdot d + b \cdot (-c)}{b \cdot d} = \frac{a \cdot d - b \cdot c}{b \cdot d}$$

במעבר האחרון השתמשנו ש-$b \cdot (-c) = -(b \cdot c)$ (שוב thm_multiplication_by_negative_one ואסוציאטיביות), ובהגדרת חיסור (def_subtraction) בכיוון ההפוך: $x + (-y) = x - y$. $\blacksquare$
