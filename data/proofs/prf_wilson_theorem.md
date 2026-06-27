---
id: prf_wilson_theorem
claim_id: thm_wilson_theorem
method: informal
status: reviewed
dependencies:
- def_prime
- def_congruence_mod
- thm_fermat_little
is_canonical: true
date_added: '2026-06-27T17:22:39.263705Z'
schema_version: 1
---

**$\Rightarrow$:** עבור $p$ ראשוני, כל $a \in \{1, \ldots, p-1\}$ הוא הפיך מודולו $p$. רוב הזוגות $(a, a^{-1})$ שונים והם מתבטלים במכפלה. הם זהים רק כש-$a = \pm 1$. אז $(p-1)! \equiv 1 \cdot (-1) \equiv -1 \pmod p$.

**$\Leftarrow$:** אם $n$ פריק, $n = ab$ עם $1 < a, b < n$, אז $a \mid (n-1)!$ ולכן לא ייתכן $(n-1)! \equiv -1 \pmod n$. $\blacksquare$
