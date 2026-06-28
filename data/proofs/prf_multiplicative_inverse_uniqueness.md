---
id: prf_multiplicative_inverse_uniqueness
claim_id: thm_multiplicative_inverse_uniqueness
method: informal
status: reviewed
dependencies:
- ax_multiplication_associativity
- ax_multiplication_commutativity
- ax_multiplicative_identity
- ax_multiplicative_inverse
is_canonical: true
date_added: '2026-06-28T15:49:27.730975Z'
schema_version: 1
---

יהי $a \in \mathbb{R}$ עם $a \neq 0$. לפי `ax_multiplicative_inverse` קיים לפחות איבר אחד $a^{-1}$ המקיים $a \cdot a^{-1} = 1$. נראה שהוא יחיד.

נניח ש-$b$ ו-$c$ שניהם הפכיים של $a$, כלומר:

$$a \cdot b = 1 \quad \text{וגם} \quad a \cdot c = 1.$$

אז נחשב:

$$b = b \cdot 1 \quad \text{(לפי \;`ax\_multiplicative\_identity`)}.$$

נציב $1 = a \cdot c$ ונקבל:

$$b = b \cdot (a \cdot c).$$

לפי אסוציאטיביות הכפל (`ax_multiplication_associativity`):

$$b \cdot (a \cdot c) = (b \cdot a) \cdot c.$$

לפי קומוטטיביות הכפל (`ax_multiplication_commutativity`), $b \cdot a = a \cdot b$, ולכן:

$$(b \cdot a) \cdot c = (a \cdot b) \cdot c = 1 \cdot c.$$

לפי `ax_multiplicative_identity` (יחד עם קומוטטיביות) $1 \cdot c = c \cdot 1 = c$. שירשור השוויונות נותן:

$$b = b \cdot 1 = b \cdot (a \cdot c) = (b \cdot a) \cdot c = (a \cdot b) \cdot c = 1 \cdot c = c.$$

כלומר $b = c$, וההפכי של $a$ הוא יחיד. $\blacksquare$
