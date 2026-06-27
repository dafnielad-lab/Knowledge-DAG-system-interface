---
id: prf_bernoulli_inequality
claim_id: thm_bernoulli_inequality
method: informal
status: reviewed
dependencies:
- def_proof_by_induction
is_canonical: true
date_added: '2026-06-27T18:47:27.564532Z'
schema_version: 1
---

**אינדוקציה על $n$.** בסיס $n=1$: $(1+x)^1 = 1 + x$. ✓

צעד: $(1+x)^{n+1} = (1+x)(1+x)^n \geq (1+x)(1 + nx) = 1 + (n+1)x + nx^2 \geq 1 + (n+1)x$ (כי $nx^2 \geq 0$ ו-$1 + x \geq 0$). $\blacksquare$
