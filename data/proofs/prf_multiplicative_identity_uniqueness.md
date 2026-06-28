---
id: prf_multiplicative_identity_uniqueness
claim_id: thm_multiplicative_identity_uniqueness
method: informal
status: reviewed
dependencies:
- ax_multiplicative_identity
- ax_multiplication_commutativity
is_canonical: true
date_added: '2026-06-28T15:49:27.725974Z'
schema_version: 1
---

נניח שגם $1$ וגם $1'$ הם איברים ניטרליים לכפל. כלומר, לכל $a \in \mathbb{R}$ מתקיים $a \cdot 1 = a$ ו-$a \cdot 1' = a$ (לפי `ax_multiplicative_identity`, כשמיישמים את התכונה גם על $1'$ בנפרד).

נציב $a = 1$ בתכונה הניטרליות של $1'$, ונקבל:

$$1 \cdot 1' = 1.$$

מצד שני, נציב $a = 1'$ בתכונה הניטרליות של $1$, ונקבל:

$$1' \cdot 1 = 1'.$$

לפי קומוטטיביות הכפל (`ax_multiplication_commutativity`), $1 \cdot 1' = 1' \cdot 1$. לכן שני האגפים השמאליים זהים, ומכאן שגם האגפים הימניים זהים:

$$1 = 1 \cdot 1' = 1' \cdot 1 = 1'.$$

קיבלנו $1 = 1'$, ולכן האיבר הניטרלי לכפל יחיד. $\blacksquare$
