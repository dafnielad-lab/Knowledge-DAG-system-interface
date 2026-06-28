---
id: prf_rational_root_theorem
claim_id: thm_rational_root_theorem
method: informal
status: reviewed
dependencies:
- def_polynomial
- thm_euclid_lemma
- def_divisibility
is_canonical: true
date_added: '2026-06-28T15:07:55.551049Z'
schema_version: 1
---

נניח $p(p/q) = 0$ עם $\gcd(p, q) = 1$. כפל ב-$q^n$: $a_n p^n + a_{n-1} p^{n-1} q + \cdots + a_0 q^n = 0$.

כל אגף שמאל מתחלק ב-$p$ (חוץ מ-$a_0 q^n$), אז $p \mid a_0 q^n$. כי $\gcd(p, q) = 1$, $p \mid a_0$. סימטרית $q \mid a_n$. $\blacksquare$
