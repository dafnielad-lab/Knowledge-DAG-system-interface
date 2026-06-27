---
id: prf_monotone_convergence
claim_id: thm_monotone_convergence
method: informal
status: reviewed
dependencies:
- def_bounded_sequence
- def_limit_of_sequence
is_canonical: true
date_added: '2026-06-27T18:26:22.743198Z'
schema_version: 1
---

**שימוש בתכונת השלמות של $\mathbb{R}$ (אקסיומת הסופרימום).** סדרה $(a_n)$ עולה חסומה מלמעלה.

תכונת השלמות מבטיחה שלקבוצה $\{a_n : n \in \mathbb{N}\}$, שאינה ריקה וחסומה מלמעלה, יש סופרימום $L$.

**טענה:** $\lim a_n = L$. לכל $\epsilon > 0$, $L - \epsilon$ אינו חסם עליון (קטן מ-$L$), אז קיים $N$ עם $a_N > L - \epsilon$.

מהמונוטוניות, לכל $n \geq N$: $a_n \geq a_N > L - \epsilon$. ומחסם עליון: $a_n \leq L < L + \epsilon$.

כלומר $|a_n - L| < \epsilon$ לכל $n \geq N$, ולכן $\lim a_n = L$.

סימטרית לסדרה יורדת חסומה מלמטה ($\inf$). $\blacksquare$
