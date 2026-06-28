---
id: prf_alternating_series_leibniz
claim_id: thm_alternating_series_leibniz
method: informal
status: reviewed
dependencies:
- def_partial_sum
- def_series_convergence
- def_limit_of_sequence
- thm_monotone_convergence
is_canonical: true
date_added: '2026-06-28T15:07:55.479550Z'
schema_version: 1
---

**הוכחה.** נסמן $S_n$ סכום חלקי. $S_{2n+2} = S_{2n} + (a_{2n+1} - a_{2n+2}) \geq S_{2n}$ (כי $a_n$ יורדת), אז תת-סדרת $S_{2n}$ עולה. בדומה $S_{2n+1}$ יורדת. הן חסומות זו על-ידי זו: $S_{2n} \leq S_{2n+1}$.

שתי תת-הסדרות מונוטוניות וחסומות, ולכן מתכנסות. ההפרש שלהן: $S_{2n+1} - S_{2n} = a_{2n+1} \to 0$, אז הגבולות שלהן שווים. מכאן $S_n$ מתכנסת. $\blacksquare$
