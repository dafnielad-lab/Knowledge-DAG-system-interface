---
id: prf_arithmetic_sum
claim_id: thm_arithmetic_sum
method: informal
status: reviewed
dependencies:
- def_arithmetic_sequence
- thm_arithmetic_nth_term
is_canonical: true
date_added: '2026-06-27T16:13:44.126814Z'
schema_version: 1
---

הטריק של גאוס: נכתוב $S_n = a_1 + a_2 + \cdots + a_n$ ושוב $S_n = a_n + a_{n-1} + \cdots + a_1$. בסכימה איבר-איבר, כל זוג נותן $a_1 + a_n$, ויש $n$ זוגות:

$2 S_n = n(a_1 + a_n)$, ולכן $S_n = \frac{n(a_1 + a_n)}{2}$.

הצבה $a_n = a_1 + (n-1)d$ נותנת את הצורה השנייה. $\blacksquare$
