---
id: prf_modular_inverse_computation
claim_id: thm_modular_inverse_computation
method: informal
status: reviewed
dependencies:
- thm_bezout_identity
- thm_euler_theorem
- def_congruence_mod
is_canonical: true
date_added: '2026-06-27T18:26:22.743198Z'
schema_version: 1
---

($\Leftarrow$) אם $\gcd(a, n) = 1$: מזהות בזו $1 = ax + ny$. מודולו $n$: $ax \equiv 1$, אז $x \equiv a^{-1}$.

אלטרנטיבית מאוילר: $a^{\varphi(n)} \equiv 1 \pmod n$, אז $a^{-1} \equiv a^{\varphi(n) - 1}$.

($\Rightarrow$) אם $a^{-1}$ קיים: $a \cdot a^{-1} \equiv 1 \pmod n$, כלומר $a a^{-1} - 1 = n k$. לכן $\gcd(a, n) \mid 1$, וזה $1$. $\blacksquare$
