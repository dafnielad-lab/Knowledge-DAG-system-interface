---
id: prf_compare_fractions
claim_id: thm_compare_fractions
method: informal
status: reviewed
dependencies:
- def_fraction
- thm_fraction_equality
- ax_positive_multiplication_preserves_order
- ax_multiplicative_inverse
- ax_multiplication_associativity
- ax_multiplication_commutativity
- ax_multiplicative_identity
is_canonical: true
date_added: '2026-06-28T20:34:16.471519Z'
schema_version: 1
---

**כיוון 1: אם $a \cdot d < b \cdot c$ אז $\frac{a}{b} < \frac{c}{d}$.**

נניח $a \cdot d < b \cdot c$. הואיל ו-$b, d > 0$, גם $b \cdot d > 0$ (חיוביות נסגרת תחת כפל), ולפי איבר הפכי לכפל (ax_multiplicative_inverse) קיים $(b \cdot d)^{-1}$, וגם הוא חיובי.

נכפול את שני אגפי האי-שוויון בגורם החיובי $(b \cdot d)^{-1}$. לפי שימור סדר בכפל בחיובי (ax_positive_multiplication_preserves_order):
$$(a \cdot d) \cdot (b \cdot d)^{-1} < (b \cdot c) \cdot (b \cdot d)^{-1}$$

נשתמש בעובדה $(b \cdot d)^{-1} = b^{-1} \cdot d^{-1}$ (כפי שהוכח, למשל, בהוכחת thm_fraction_simplification, על בסיס ax_multiplicative_inverse, ax_multiplication_associativity, ax_multiplication_commutativity, ax_multiplicative_identity).

אגף שמאל:
$$(a \cdot d) \cdot (b^{-1} \cdot d^{-1}) = a \cdot b^{-1} \cdot (d \cdot d^{-1}) = a \cdot b^{-1} \cdot 1 = a \cdot b^{-1} = \frac{a}{b}$$
(לפי ax_multiplication_associativity, ax_multiplication_commutativity, ax_multiplicative_inverse, ax_multiplicative_identity, def_fraction).

אגף ימין:
$$(b \cdot c) \cdot (b^{-1} \cdot d^{-1}) = c \cdot d^{-1} \cdot (b \cdot b^{-1}) = c \cdot d^{-1} \cdot 1 = c \cdot d^{-1} = \frac{c}{d}$$

לכן $\frac{a}{b} < \frac{c}{d}$.

**כיוון 2: אם $\frac{a}{b} < \frac{c}{d}$ אז $a \cdot d < b \cdot c$.**

נניח $\frac{a}{b} < \frac{c}{d}$. נכפול את שני האגפים בגורם החיובי $b \cdot d > 0$. לפי ax_positive_multiplication_preserves_order:
$$\frac{a}{b} \cdot (b \cdot d) < \frac{c}{d} \cdot (b \cdot d)$$

לפי הגדרת שבר (def_fraction) ובחישוב דומה לעיל:
$$\frac{a}{b} \cdot (b \cdot d) = a \cdot b^{-1} \cdot b \cdot d = a \cdot 1 \cdot d = a \cdot d$$
ו-
$$\frac{c}{d} \cdot (b \cdot d) = c \cdot d^{-1} \cdot b \cdot d = c \cdot b \cdot 1 = b \cdot c$$
(לפי ax_multiplication_commutativity).

לכן $a \cdot d < b \cdot c$.

**שוויון:** המקרה $a \cdot d = b \cdot c$ מתאים בדיוק לשוויון השברים $\frac{a}{b} = \frac{c}{d}$ לפי משפט שוויון שברים (thm_fraction_equality). $\blacksquare$
