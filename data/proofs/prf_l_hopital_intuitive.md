---
id: prf_l_hopital_intuitive
claim_id: thm_l_hopital_intuitive
method: informal
status: reviewed
dependencies:
- thm_cauchy_mean_value
- def_function_limit_formal
is_canonical: true
date_added: '2026-06-27T17:14:35.074631Z'
schema_version: 1
---

**הוכחה לצורת $\tfrac{0}{0}$.** נניח $f, g$ גזירות בסביבת $a$, $f(a) = g(a) = 0$ ו-$g'(x) \neq 0$.

לפי משפט קושי לערך הממוצע, עבור כל $x$ קרוב ל-$a$ קיים $\xi$ בין $a$ ל-$x$ כך ש:

$\frac{f(x) - f(a)}{g(x) - g(a)} = \frac{f'(\xi)}{g'(\xi)}$

מ-$f(a) = g(a) = 0$: $\frac{f(x)}{g(x)} = \frac{f'(\xi)}{g'(\xi)}$.

כש-$x \to a$, $\xi \to a$ (כי $\xi$ ביניהם). לכן $\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$, אם הגבול האחרון קיים.

**צורת $\tfrac{\infty}{\infty}$**: הוכחה דומה אבל מורכבת יותר טכנית (משתמשים בקירוב הפיכי). $\blacksquare$
