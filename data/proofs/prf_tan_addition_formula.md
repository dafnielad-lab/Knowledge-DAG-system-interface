---
id: prf_tan_addition_formula
claim_id: thm_tan_addition_formula
method: informal
status: reviewed
dependencies:
- thm_sin_addition_formula
- thm_cos_addition_formula
- def_tan
is_canonical: true
date_added: '2026-06-27T18:26:22.743198Z'
schema_version: 1
---

$\tan(\alpha + \beta) = \frac{\sin(\alpha + \beta)}{\cos(\alpha + \beta)} = \frac{\sin\alpha\cos\beta + \cos\alpha\sin\beta}{\cos\alpha\cos\beta - \sin\alpha\sin\beta}$. נחלק מונה ומכנה ב-$\cos\alpha\cos\beta$: $= \frac{\tan\alpha + \tan\beta}{1 - \tan\alpha\tan\beta}$. $\blacksquare$
