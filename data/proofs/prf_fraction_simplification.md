---
id: prf_fraction_simplification
claim_id: thm_fraction_simplification
method: informal
status: reviewed
dependencies:
- def_fraction
- ax_multiplication_associativity
- ax_multiplication_commutativity
- ax_multiplicative_inverse
- ax_multiplicative_identity
is_canonical: true
date_added: '2026-06-28T15:49:27.750471Z'
schema_version: 1
---

נראה ש-$\frac{a \cdot c}{b \cdot c} = \frac{a}{b}$ עבור $a, b, c \in \mathbb{Z}$ ו-$b, c \neq 0$.

לפי הגדרת שבר (def_fraction), $\frac{a \cdot c}{b \cdot c} = (a \cdot c) \cdot (b \cdot c)^{-1}$.

נשתמש בעובדה ש-$(b \cdot c)^{-1} = b^{-1} \cdot c^{-1}$: זאת מפני שלפי איבר הפכי לכפל (ax_multiplicative_inverse), $b$ ו-$c$ שונים מאפס, כך שגם $b \cdot c \neq 0$ וקיים $(b \cdot c)^{-1}$. נכפול $(b \cdot c) \cdot (b^{-1} \cdot c^{-1})$ ונשתמש באסוציאטיביות וקומוטטיביות הכפל (ax_multiplication_associativity, ax_multiplication_commutativity): $(b \cdot c) \cdot (b^{-1} \cdot c^{-1}) = (b \cdot b^{-1}) \cdot (c \cdot c^{-1}) = 1 \cdot 1 = 1$ (לפי ax_multiplicative_inverse ו-ax_multiplicative_identity). מכאן $b^{-1} \cdot c^{-1}$ הוא ההפכי הכפלי של $b \cdot c$, כלומר $(b \cdot c)^{-1} = b^{-1} \cdot c^{-1}$.

כעת:
$(a \cdot c) \cdot (b \cdot c)^{-1} = (a \cdot c) \cdot (b^{-1} \cdot c^{-1})$

לפי אסוציאטיביות וקומוטטיביות הכפל (ax_multiplication_associativity, ax_multiplication_commutativity), נסדר את הגורמים מחדש:
$= a \cdot (c \cdot b^{-1} \cdot c^{-1}) = a \cdot b^{-1} \cdot (c \cdot c^{-1})$

לפי איבר הפכי לכפל (ax_multiplicative_inverse), $c \cdot c^{-1} = 1$:
$= a \cdot b^{-1} \cdot 1$

לפי איבר ניטרלי לכפל (ax_multiplicative_identity), $a \cdot b^{-1} \cdot 1 = a \cdot b^{-1}$.

לסיכום, $\frac{a \cdot c}{b \cdot c} = a \cdot b^{-1} = \frac{a}{b}$ (לפי def_fraction בכיוון ההפוך). $\blacksquare$
