---
id: prf_fraction_division
claim_id: thm_fraction_division
method: informal
status: reviewed
dependencies:
- def_fraction
- def_division
- thm_fraction_multiplication
- ax_multiplication_associativity
- ax_multiplication_commutativity
- ax_multiplicative_inverse
- ax_multiplicative_identity
is_canonical: true
date_added: '2026-06-28T15:49:27.753471Z'
schema_version: 1
---

ראשית נראה שההפכי הכפלי של השבר $\frac{c}{d}$ (כאשר $c, d \neq 0$) הוא $\frac{d}{c}$.

לפי הגדרת שבר (def_fraction), $\frac{c}{d} = c \cdot d^{-1}$ ו-$\frac{d}{c} = d \cdot c^{-1}$.

נחשב את המכפלה (לפי כפל שברים, thm_fraction_multiplication):
$\frac{c}{d} \cdot \frac{d}{c} = \frac{c \cdot d}{d \cdot c}$

לפי קומוטטיביות הכפל (ax_multiplication_commutativity), $d \cdot c = c \cdot d$, ולכן $\frac{c \cdot d}{d \cdot c} = \frac{c \cdot d}{c \cdot d}$. לפי def_fraction זהו $(c \cdot d) \cdot (c \cdot d)^{-1}$, ולפי איבר הפכי לכפל (ax_multiplicative_inverse) — שכן $c \cdot d \neq 0$ — ביטוי זה שווה ל-$1$.

מכאן $\frac{c}{d} \cdot \frac{d}{c} = 1$, כלומר $\left(\frac{c}{d}\right)^{-1} = \frac{d}{c}$.

כעת לפי הגדרת חילוק (def_division), חילוק במספר שאינו אפס שווה לכפל בהפכי הכפלי:
$\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \cdot \left(\frac{c}{d}\right)^{-1} = \frac{a}{b} \cdot \frac{d}{c}$

לבסוף, לפי כפל שברים (thm_fraction_multiplication):
$\frac{a}{b} \cdot \frac{d}{c} = \frac{a \cdot d}{b \cdot c}$

לסיכום, $\frac{a}{b} \div \frac{c}{d} = \frac{a \cdot d}{b \cdot c}$.

הערה: השימוש באסוציאטיביות הכפל (ax_multiplication_associativity) ובאיבר הניטרלי לכפל (ax_multiplicative_identity) משתמע בתוך הוכחת thm_fraction_multiplication עליה הסתמכנו. $\blacksquare$
