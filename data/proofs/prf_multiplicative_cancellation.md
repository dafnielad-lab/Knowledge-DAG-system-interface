---
id: prf_multiplicative_cancellation
claim_id: thm_multiplicative_cancellation
method: informal
status: reviewed
dependencies:
- ax_multiplicative_inverse
- ax_multiplication_associativity
- ax_multiplication_commutativity
- ax_multiplicative_identity
is_canonical: true
date_added: '2026-06-28T15:49:27.734469Z'
schema_version: 1
---

נתון $a \cdot b = a \cdot c$ ו-$a \neq 0$. לפי `ax_multiplicative_inverse`, מכיוון ש-$a \neq 0$ קיים $a^{-1} \in \mathbb{R}$ כך ש-$a \cdot a^{-1} = 1$.

נכפיל את שני האגפים ב-$a^{-1}$ משמאל:

$$a^{-1} \cdot (a \cdot b) = a^{-1} \cdot (a \cdot c).$$

לפי אסוציאטיביות הכפל (`ax_multiplication_associativity`):

$$(a^{-1} \cdot a) \cdot b = (a^{-1} \cdot a) \cdot c.$$

לפי קומוטטיביות הכפל (`ax_multiplication_commutativity`), $a^{-1} \cdot a = a \cdot a^{-1}$, ולפי `ax_multiplicative_inverse`, $a \cdot a^{-1} = 1$. לכן:

$$1 \cdot b = 1 \cdot c.$$

לפי `ax_multiplicative_identity` (יחד עם קומוטטיביות), $1 \cdot b = b \cdot 1 = b$ וכן $1 \cdot c = c$. מכאן:

$$b = c. \quad \blacksquare$$
