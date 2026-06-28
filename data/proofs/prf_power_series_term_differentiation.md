---
id: prf_power_series_term_differentiation
claim_id: thm_power_series_term_differentiation
method: informal
status: reviewed
dependencies:
- def_power_series
- def_radius_of_convergence
- def_derivative_function
- def_series_convergence
- thm_derivative_power
- thm_derivative_sum
- thm_geometric_series_convergence
is_canonical: true
date_added: '2026-06-28T15:07:55.473551Z'
schema_version: 1
---

**הוכחה.** נסמן $g(x) = \sum_{n=1}^{\infty} n \, a_n (x - c)^{n-1}$ את הטור הנגזר פורמלית (לפי [thm_derivative_power](thm_derivative_power) על כל איבר $a_n (x-c)^n$ ולפי [thm_derivative_sum](thm_derivative_sum) המוכלל לטור).

**שלב 1 — שוויון רדיוסי ההתכנסות.** יהי $|x - c| < R$. נבחר $\rho$ עם $|x - c| < \rho < R$. כיוון ש-$\sum a_n \rho^n$ מתכנס (לפי [def_radius_of_convergence](def_radius_of_convergence)), איבריו חסומים: קיים $M$ כך ש-$|a_n| \rho^n \leq M$ לכל $n$. נסמן $r = |x-c|/\rho < 1$. אזי
$$|n \, a_n (x-c)^{n-1}| = \frac{n}{\rho} \cdot |a_n| \rho^n \cdot r^{n-1} \cdot \rho \leq \frac{M}{|x-c|} \cdot n \, r^n.$$
הטור $\sum n r^n$ מתכנס עבור $|r| < 1$ (השוואה לטור הנדסי $\sum r^n$ לפי [thm_geometric_series_convergence](thm_geometric_series_convergence) ומבחן המנה: $\frac{(n+1)r^{n+1}}{n r^n} \to r < 1$). לכן $g(x)$ מתכנס בהחלט (לפי [def_series_convergence](def_series_convergence)). בכיוון השני, אם $|x-c| > R$ אזי $a_n(x-c)^n$ אינו חסום, וכן $n a_n (x-c)^{n-1}$. לכן הרדיוס של $g$ הוא בדיוק $R$.

**שלב 2 — $f'(x) = g(x)$.** קבע $x$ עם $|x-c| < R$, ובחר $\rho$ עם $|x-c| < \rho < R$. לכל $h \neq 0$ עם $|x+h-c| < \rho$ ובאמצעות הזהות $a^n - b^n = (a-b)\sum_{k=0}^{n-1} a^{n-1-k} b^k$:
$$\frac{f(x+h) - f(x)}{h} - g(x) = \sum_{n=1}^{\infty} a_n \left[ \sum_{k=0}^{n-1}(x+h-c)^{n-1-k}(x-c)^k - n(x-c)^{n-1} \right].$$
כל איבר בסוגריים שואף ל-$0$ כאשר $h \to 0$ (כי $(x+h-c)^j \to (x-c)^j$), וחסום ב-$2n \rho^{n-1}$. מתורת הטור $\sum n |a_n| \rho^{n-1}$ שהוכחנו מתכנס בשלב 1, מבחן ה-M של ויירשטראס מאפשר החלפת סדר הגבול והסכום, ולכן הביטוי שואף ל-$0$. מכאן, לפי [def_derivative_function](def_derivative_function), $f'(x) = g(x)$. $\blacksquare$
