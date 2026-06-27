---
id: prf_euler_theorem
claim_id: thm_euler_theorem
method: informal
status: reviewed
dependencies:
- def_euler_totient
- def_congruence_mod
- thm_modular_arithmetic_properties
is_canonical: true
date_added: '2026-06-27T17:22:39.263705Z'
schema_version: 1
---

**הכללה של פרמה הקטן.** סדר השלמים הזרים ל-$n$ במודולו $n$: $\{r_1, \ldots, r_{\varphi(n)}\}$. כפל ב-$a$ (זר ל-$n$) נותן פרמוטציה של אותה קבוצה.

לכן $\prod a r_i \equiv \prod r_i \pmod n$, כלומר $a^{\varphi(n)} \prod r_i \equiv \prod r_i$. צמצום (כי המכפלה זרה ל-$n$): $a^{\varphi(n)} \equiv 1 \pmod n$. $\blacksquare$
