---
id: prf_wilson_theorem
claim_id: thm_wilson_theorem
method: informal
status: reviewed
dependencies:
- def_prime
- def_congruence_mod
- thm_no_zero_divisors
- ax_multiplicative_inverse
is_canonical: true
date_added: '2026-06-27T20:41:51.335588Z'
schema_version: 1
---

יהי $p$ ראשוני. נסתכל במכפלה $(p-1)! = 1 \cdot 2 \cdots (p-1)$ מודולו $p$.

**זיווג בהפכיים:** כל $a \in \{1, \ldots, p-1\}$ הוא בעל הפכי כפלי מודולו $p$ (כי $\gcd(a, p) = 1$). נזווג כל $a$ עם $a^{-1}$ ב-$\{1, \ldots, p-1\}$. כל זוג כזה תורם $a \cdot a^{-1} = 1$ למכפלה.

**איברים שזוויגו עם עצמם:** $a^2 \equiv 1 \pmod p$, כלומר $(a-1)(a+1) \equiv 0 \pmod p$. כיוון ש-$p$ ראשוני אין מחלקי אפס מודולו $p$, ולכן $a \equiv 1$ או $a \equiv -1 \equiv p-1$.

כלומר רק $1$ ו-$p-1$ הם המכפילים העצמיים. שאר האיברים $\{2, 3, \ldots, p-2\}$ מתחלקים לזוגות $(a, a^{-1})$ עם $a \neq a^{-1}$, וכל זוג תורם $1$.

אז $(p-1)! \equiv 1 \cdot (p-1) \cdot \underbrace{1 \cdot 1 \cdots 1}_{\text{זוגות}} \equiv (p-1) \equiv -1 \pmod p$. $\blacksquare$
