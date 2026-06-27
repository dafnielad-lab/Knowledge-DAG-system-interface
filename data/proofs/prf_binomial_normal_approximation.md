---
id: prf_binomial_normal_approximation
claim_id: thm_binomial_normal_approximation
method: informal
status: reviewed
dependencies:
- def_binomial_distribution
- thm_central_limit_theorem_intuitive
- def_normal_distribution
is_canonical: true
date_added: '2026-06-27T18:47:27.564532Z'
schema_version: 1
---

$\text{Bin}(n, p)$ היא סכום של $n$ ברנולים בלתי-תלויים. לפי משפט הגבול המרכזי, סכום נטוי לנורמלית כש-$n \to \infty$.

עם תוחלת $np$ ושונות $np(1-p)$, $X \approx N(np, np(1-p))$. $\blacksquare$
