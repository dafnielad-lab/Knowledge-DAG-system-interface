---
id: prf_multinomial_theorem
claim_id: thm_multinomial_theorem
method: informal
status: reviewed
dependencies:
- def_permutation_with_repetition
- thm_binomial_theorem
is_canonical: true
date_added: '2026-06-27T17:22:39.263705Z'
schema_version: 1
---

**הוכחה קומבינטורית.** $(x_1 + \cdots + x_m)^n$ — מכפילים $n$ סוגריים, כל סוגריים בוחר אחד מ-$x_i$.

איבר $x_1^{n_1} x_2^{n_2} \cdots x_m^{n_m}$ (עם $\sum n_i = n$) נוצר בכמה דרכים שניתן לבחור איזה סוגריים נותן $x_1$ (יש $\binom{n}{n_1}$), אז איזה נותן $x_2$ מהשאר, וכו'. סך הכל $\frac{n!}{n_1! n_2! \cdots n_m!}$. $\blacksquare$
