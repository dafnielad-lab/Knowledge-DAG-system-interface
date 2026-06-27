---
id: prf_derivative_chain
claim_id: thm_derivative_chain
method: informal
status: reviewed
dependencies:
- def_derivative_at_point
- thm_differentiable_implies_continuous
is_canonical: true
date_added: '2026-06-27T16:20:58.288163Z'
schema_version: 1
---

$\frac{f(g(x+h)) - f(g(x))}{h} = \frac{f(g(x+h)) - f(g(x))}{g(x+h) - g(x)} \cdot \frac{g(x+h) - g(x)}{h}$ (כאשר ההפרש במונה האמצעי שונה מאפס).

כאשר $h \to 0$: $g(x+h) \to g(x)$ (רציפות), והגורם הראשון שואף ל-$f'(g(x))$, השני ל-$g'(x)$. לכן הנגזרת היא $f'(g(x)) \cdot g'(x)$.

(טיפול בנקודות שבהן $g(x+h) = g(x)$ נעשה בנפרד.) $\blacksquare$
