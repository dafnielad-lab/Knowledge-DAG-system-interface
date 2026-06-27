---
id: prf_bezout_identity
claim_id: thm_bezout_identity
method: informal
status: reviewed
dependencies:
- thm_euclidean_algorithm
- def_gcd
- def_integers
is_canonical: true
date_added: '2026-06-27T16:34:26.423690Z'
schema_version: 1
---

מבצעים את אלגוריתם אוקלידס. בכל שלב הוא יוצר משוואה $r_i = r_{i-2} - q_i \cdot r_{i-1}$.

ע״י החלפה לאחור, מבטאים את ה-GCD (הוא $r_{k}$ האחרון לפני $r = 0$) כצירוף לינארי שלם של $a$ ו-$b$: $\gcd(a, b) = a x + b y$. $\blacksquare$
