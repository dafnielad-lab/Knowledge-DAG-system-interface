---
id: prf_square_of_difference_identity
claim_id: thm_square_of_difference_identity
method: informal
status: reviewed
dependencies:
- def_subtraction
- thm_square_of_sum_identity
- thm_negative_times_positive_basic
- def_natural_power
- ax_addition_commutativity
is_canonical: true
date_added: '2026-06-28T15:49:27.768194Z'
schema_version: 1
---

לפי הגדרת החיסור ($\texttt{def\_subtraction}$): $a - b = a + (-b)$. לכן:

$(a - b)^2 = (a + (-b))^2$.

נציב $b \to -b$ בזהות ריבוע הסכום ($\texttt{thm\_square\_of\_sum\_identity}$), שלפיה $(x+y)^2 = x^2 + 2xy + y^2$ לכל $x, y \in \mathbb{R}$:

$(a + (-b))^2 = a^2 + 2 \cdot a \cdot (-b) + (-b)^2$.

כעת נחשב את שני האיברים האחרונים בנפרד.

ראשית, לפי הזהות "מינוס חיובי שלילי" ($\texttt{thm\_negative\_times\_positive\_basic}$), המוסיפה ש-$(-x) \cdot y = -(x \cdot y)$ לכל $x, y \in \mathbb{R}$, מתקיים $a \cdot (-b) = -(a \cdot b) = -ab$. לכן:

$2 \cdot a \cdot (-b) = 2 \cdot (-(a \cdot b)) = -(2ab) = -2ab$.

שנית, נחשב את $(-b)^2$. לפי הגדרת חזקה טבעית ($\texttt{def\_natural\_power}$), $(-b)^2 = (-b) \cdot (-b)$. לפי $\texttt{thm\_negative\_times\_positive\_basic}$, $(-b) \cdot (-b) = -(b \cdot (-b))$. ושוב לפי אותה זהות (וקומוטטיביות הכפל), $b \cdot (-b) = -(b \cdot b) = -b^2$. לכן $(-b)^2 = -(-b^2) = b^2$.

נציב חזרה:

$(a - b)^2 = a^2 + (-2ab) + b^2 = a^2 - 2ab + b^2$,

כאשר ההמרה האחרונה היא לפי הגדרת חיסור ($\texttt{def\_subtraction}$) וקומוטטיביות החיבור ($\texttt{ax\_addition\_commutativity}$). $\blacksquare$
