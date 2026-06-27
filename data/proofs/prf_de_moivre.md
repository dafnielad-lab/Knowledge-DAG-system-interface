---
id: prf_de_moivre
claim_id: thm_de_moivre
method: informal
status: reviewed
dependencies:
- def_polar_form_complex
- thm_complex_multiplication
- thm_cos_addition_formula
- thm_sin_addition_formula
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

אינדוקציה על $n$. בסיס $n = 1$: טריוויאלי.

צעד: $(\cos\theta + i\sin\theta)^{n+1} = (\cos\theta + i\sin\theta)^n \cdot (\cos\theta + i\sin\theta)$

$= (\cos n\theta + i\sin n\theta)(\cos\theta + i\sin\theta)$ (לפי הנחת האינדוקציה)

$= (\cos n\theta \cos\theta - \sin n\theta \sin\theta) + i(\sin n\theta \cos\theta + \cos n\theta \sin\theta)$

$= \cos((n+1)\theta) + i \sin((n+1)\theta)$ (לפי נוסחאות חיבור). $\blacksquare$
