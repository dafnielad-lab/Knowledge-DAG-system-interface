---
id: prf_limit_sin_over_x
claim_id: thm_limit_sin_over_x
method: informal
status: reviewed
dependencies:
- def_sin
- thm_sin_cos_pythagorean
- thm_squeeze_theorem
- def_unit_circle
is_canonical: true
date_added: '2026-06-27T17:14:35.074631Z'
schema_version: 1
---

במעגל היחידה עבור $0 < x < \frac{\pi}{2}$, חישובי שטח של גזרה ושני משולשים נותנים $\sin x \leq x \leq \tan x$.

חלוקה ב-$\sin x$: $1 \leq \frac{x}{\sin x} \leq \frac{1}{\cos x}$.

כש-$x \to 0$, $\cos x \to 1$, ולפי משפט הסנדוויץ׳ $\frac{x}{\sin x} \to 1$, ולכן $\frac{\sin x}{x} \to 1$. (סימטריה ל-$x < 0$ כי $\sin$ אי-זוגית.) $\blacksquare$
