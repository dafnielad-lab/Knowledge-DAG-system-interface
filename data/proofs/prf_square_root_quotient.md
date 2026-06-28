---
id: prf_square_root_quotient
claim_id: thm_square_root_quotient
method: informal
status: reviewed
dependencies:
- def_square_root
- def_division
- thm_sqrt_of_product
- ax_multiplicative_inverse
- ax_multiplication_commutativity
- ax_multiplication_associativity
- ax_multiplicative_identity
is_canonical: true
date_added: '2026-06-28T21:06:29.445179Z'
schema_version: 1
---

נסמן $x = \sqrt{a}$ ו-$y = \sqrt{b}$. לפי הגדרת שורש ריבועי (def_square_root), $x \geq 0$, $y \geq 0$, $x^2 = a$, ו-$y^2 = b$. כיוון ש-$b > 0$ נובע ש-$y > 0$ (אילו $y = 0$ היה $b = y^2 = 0$), ובפרט $y \neq 0$.

נגדיר $z := \dfrac{x}{y} = x \cdot y^{-1}$ (לפי הגדרת חילוק, def_division). מאחר ש-$x \geq 0$ ו-$y > 0$ נובע ש-$y^{-1} > 0$ (לפי איבר הפכי לכפל, ax_multiplicative_inverse, חיוביות של ההפכי), ולכן $z \geq 0$.

נחשב את $z^2$ באמצעות שורש של מכפלה (thm_sqrt_of_product) ביישום הפוך — נשים לב ש-$z \cdot z = (x \cdot y^{-1}) \cdot (x \cdot y^{-1})$. לפי קומוטטיביות ואסוציאטיביות הכפל (ax_multiplication_commutativity, ax_multiplication_associativity):
$z^2 = x \cdot x \cdot y^{-1} \cdot y^{-1} = x^2 \cdot (y^{-1})^2 = a \cdot (y^{-1})^2$.

אבל $y^2 \cdot (y^{-1})^2 = (y \cdot y^{-1})^2 = 1^2 = 1$ (לפי ax_multiplicative_inverse ו-ax_multiplicative_identity), ולכן $(y^{-1})^2 = (y^2)^{-1} = b^{-1}$.

מכאן $z^2 = a \cdot b^{-1} = \dfrac{a}{b}$ (שוב לפי def_division).

הראינו ש-$z \geq 0$ ו-$z^2 = \dfrac{a}{b}$. לפי יחידות השורש הריבועי האי-שלילי (def_square_root), $z$ הוא בדיוק $\sqrt{\dfrac{a}{b}}$, כלומר $\sqrt{\dfrac{a}{b}} = \dfrac{\sqrt{a}}{\sqrt{b}}$.

הערה לגבי קישור ל-thm_sqrt_of_product: ניתן באופן חלופי להוכיח על-ידי הצבת $\dfrac{a}{b}$ בנוסחה: $\sqrt{a} = \sqrt{b \cdot \dfrac{a}{b}} = \sqrt{b} \cdot \sqrt{\dfrac{a}{b}}$, ואז חלוקה ב-$\sqrt{b} > 0$. $\blacksquare$
