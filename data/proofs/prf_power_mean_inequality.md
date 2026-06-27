---
id: prf_power_mean_inequality
claim_id: thm_power_mean_inequality
method: informal
status: reviewed
dependencies:
- thm_jensen_inequality
- def_convex_function
- def_concave_function
is_canonical: true
date_added: '2026-06-27T18:48:38.235747Z'
schema_version: 1
---

**הוכחה (לפי ינסן).** עבור $r > s > 0$, הפונקציה $\phi(t) = t^{r/s}$ קמורה (כי $\phi'' \geq 0$ ע״י חישוב).

הפעלת אי-שוויון ינסן על המספרים $a_i^s$ עם משקלים שווים $1/n$:

$\phi\!\left(\frac{\sum a_i^s}{n}\right) \leq \frac{\sum \phi(a_i^s)}{n} = \frac{\sum a_i^r}{n}$

$\left(\frac{\sum a_i^s}{n}\right)^{r/s} \leq \frac{\sum a_i^r}{n}$

מעלים שני האגפים בחזקת $1/r$:

$\left(\frac{\sum a_i^s}{n}\right)^{1/s} \leq \left(\frac{\sum a_i^r}{n}\right)^{1/r}$, כלומר $M_s(a) \leq M_r(a)$.

טיפול בערכים שליליים של $s, r$ (לרבות HM כש-$s = -1$) דומה ע״י אותו טיעון. $\blacksquare$
