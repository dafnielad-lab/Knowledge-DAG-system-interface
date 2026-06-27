---
id: prf_fermat_little
claim_id: thm_fermat_little
method: informal
status: reviewed
dependencies:
- def_prime
- def_congruence_mod
- thm_modular_arithmetic_properties
is_canonical: true
date_added: '2026-06-27T17:14:35.075131Z'
schema_version: 1
---

**הוכחה קלאסית.** $\{a, 2a, 3a, \ldots, (p-1)a\}$ מודולו $p$ הם פרמוטציה של $\{1, 2, \ldots, p - 1\}$ (כי $\gcd(a, p) = 1$).

לכן מכפלותיהם שוות: $a \cdot 2a \cdots (p-1)a \equiv 1 \cdot 2 \cdots (p-1) \pmod p$, כלומר $a^{p-1} (p-1)! \equiv (p-1)! \pmod p$.

כי $\gcd((p-1)!, p) = 1$, מצמצמים: $a^{p-1} \equiv 1 \pmod p$. $\blacksquare$
