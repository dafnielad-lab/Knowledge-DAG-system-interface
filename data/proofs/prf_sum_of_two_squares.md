---
id: prf_sum_of_two_squares
claim_id: thm_sum_of_two_squares
method: informal
status: reviewed
dependencies:
- def_prime
- def_congruence_mod
- thm_wilson_theorem
is_canonical: true
date_added: '2026-06-28T15:07:55.558549Z'
schema_version: 1
---

**משפט קלאסי של פרמה.** ($\Leftarrow$) אם $p \equiv 1 \pmod 4$: לפי משפט וילסון ושיקולי שאריות ריבועיות, $-1$ הוא שארית ריבועית מודולו $p$. בעזרת אלגוריתם אוקלידס על $a, p$ עם $a^2 \equiv -1$ מקבלים את הפירוק $p = a^2 + b^2$ ע״י הירידה הסופית.

($\Rightarrow$) אם $p = a^2 + b^2$ ראשוני: ריבועים מודולו $4$ הם $0$ או $1$; סכום שני ריבועים הוא $0, 1, 2$ אבל לא $3$. ראשוני אי-זוגי הוא $\equiv 1$ או $3 \pmod 4$, אז כדי שיהיה סכום שני ריבועים — $p \equiv 1$. $\blacksquare$
