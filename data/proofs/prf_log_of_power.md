---
id: prf_log_of_power
claim_id: thm_log_of_power
method: informal
status: reviewed
dependencies:
- def_logarithm
- def_exponential_function
- thm_log_inverse_of_exp
is_canonical: true
date_added: '2026-06-27T20:41:51.335588Z'
schema_version: 1
---

**שלב 1 — שינוי בסיס לטבעי:** לכל $y > 0$ ולכל $b > 0$, $b \neq 1$:

מצד אחד $y = e^{\ln y}$ (הופכי של ln). מצד שני $y = b^{\log_b y}$ (הופכי של log_b לפי ההגדרה), ולפי הגדרת חזקה כללית $b^{\log_b y} = e^{\log_b y \cdot \ln b}$.

מהשוויון $e^{\ln y} = e^{\log_b y \cdot \ln b}$ ומחד-חד-ערכיות של $\exp$: $\ln y = \log_b y \cdot \ln b$, כלומר $\log_b y = \tfrac{\ln y}{\ln b}$. (זו נוסחת שינוי בסיס.)

**שלב 2 — לוגריתם של חזקה:** לפי הגדרת חזקה כללית $x^n = e^{n \ln x}$. אז:

$\log_b(x^n) = \tfrac{\ln(x^n)}{\ln b} = \tfrac{\ln(e^{n \ln x})}{\ln b}$ (שלב 1)

$= \tfrac{n \ln x}{\ln b}$ (לפי הופכי $\ln(e^t) = t$)

$= n \cdot \tfrac{\ln x}{\ln b} = n \log_b x$ (שלב 1 הפוך). $\blacksquare$
