---
id: prf_chinese_remainder_theorem
claim_id: thm_chinese_remainder_theorem
method: informal
status: reviewed
dependencies:
- def_congruence_mod
- thm_bezout_identity
is_canonical: true
date_added: '2026-06-27T17:22:39.263705Z'
schema_version: 1
---

**הוכחה קונסטרוקטיבית.** עבור $k = 2$: $n_1, n_2$ זרים, אז זהות בזו נותנת $1 = n_1 u + n_2 v$. הפתרון: $x = a_2 \cdot n_1 u + a_1 \cdot n_2 v$.

אינדוקציה על $k$. יחידות מודולו $N = \prod n_i$ ממשפט פרמטר וזרות מודולוסים.  $\blacksquare$
