---
id: prf_logarithmic_differentiation
claim_id: thm_logarithmic_differentiation
method: informal
status: reviewed
dependencies:
- thm_derivative_log_natural
- thm_derivative_chain
- thm_derivative_product
- thm_derivative_quotient
is_canonical: true
date_added: '2026-06-28T15:49:27.956194Z'
schema_version: 1
---

נוכיח את כלל הגזירה הלוגריתמית בשני המקרים המרכזיים: פונקציות חזקה-מערך, ומכפלות/מנות מורכבות.

**מקרה I: $y = f(x)^{g(x)}$, $f(x) > 0$.**

לוקחים $\ln$ משני האגפים:
$$\ln y = \ln \left(f(x)^{g(x)}\right) = g(x) \ln f(x)$$
(בשימוש בתכונת לוגריתם של חזקה).

כעת גוזרים את שני האגפים לפי $x$. אגף שמאל: $\frac{d}{dx} \ln y = \frac{1}{y} \cdot \frac{dy}{dx}$ לפי thm_derivative_chain ו-thm_derivative_log_natural (שלפיו $(\ln u)' = 1/u$).

אגף ימין: $\frac{d}{dx} [g(x) \ln f(x)]$ לפי thm_derivative_product:
$$\frac{d}{dx}[g(x)\ln f(x)] = g'(x) \ln f(x) + g(x) \cdot \frac{d}{dx}\ln f(x).$$
לפי thm_derivative_chain ו-thm_derivative_log_natural: $\frac{d}{dx}\ln f(x) = \frac{f'(x)}{f(x)}$.

לכן:
$$\frac{1}{y} \cdot y' = g'(x)\ln f(x) + \frac{g(x) f'(x)}{f(x)}.$$
כפל ב-$y = f(x)^{g(x)}$:
$$y' = f(x)^{g(x)} \left[g'(x)\ln f(x) + \frac{g(x) f'(x)}{f(x)}\right].$$

**דוגמה ($y = x^x$):** כאן $f(x) = x$, $g(x) = x$, $f'=g'=1$. נקבל:
$$y' = x^x \left[1 \cdot \ln x + \frac{x \cdot 1}{x}\right] = x^x(\ln x + 1).$$

**מקרה II: מכפלות/מנות מורכבות, למשל $y = \frac{u(x) v(x)}{w(x)}$.**

גזירה ישירה תדרוש שילוב של thm_derivative_product ו-thm_derivative_quotient — מסורבל. במקום זה: $\ln y = \ln u + \ln v - \ln w$ (תכונות לוגריתם).

גזירה לפי $x$ (משמאל לפי thm_derivative_chain ו-thm_derivative_log_natural; מימין לפי thm_derivative_log_natural על כל איבר): 
$$\frac{y'}{y} = \frac{u'}{u} + \frac{v'}{v} - \frac{w'}{w}.$$
ומכאן:
$$y' = y \left[\frac{u'}{u} + \frac{v'}{v} - \frac{w'}{w}\right] = \frac{uv}{w}\left[\frac{u'}{u} + \frac{v'}{v} - \frac{w'}{w}\right].$$

**נכונות השיטה:** ההצדקה ההלכתית — לקיחת $\ln$ הופכת את הכפל לסכום ואת החזקה לכפל פשוט, כך שהנגזרת דורשת רק את thm_derivative_sum (סכום) ו-thm_derivative_chain עם thm_derivative_log_natural — במקום שילוב מסובך של thm_derivative_quotient עם נגזרת חזקה כללית. עבור ערכים שליליים יש לעבוד עם $\ln|y|$, אבל הנוסחה הסופית זהה. $\blacksquare$
