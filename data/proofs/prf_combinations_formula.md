---
id: prf_combinations_formula
claim_id: thm_combinations_formula
method: informal
status: reviewed
dependencies:
- def_combination
- def_permutation
- def_factorial
is_canonical: true
date_added: '2026-06-27T16:13:44.126814Z'
schema_version: 1
---

מספר התמורות של $n$ אלמנטים הוא $n!$.

אם בוחרים $k$ מתוך $n$ ומסדרים, מקבלים $\frac{n!}{(n-k)!}$ תמורות. כל בחירה לא-מסודרת מופיעה $k!$ פעמים (כי יש $k!$ סידורים של אותם $k$ איברים).

לכן מספר הבחירות הוא $\binom{n}{k} = \frac{n!}{k!(n-k)!}$. $\blacksquare$
