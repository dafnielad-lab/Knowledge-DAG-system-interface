---
id: prf_square_of_sum_identity
claim_id: thm_square_of_sum_identity
method: informal
status: reviewed
dependencies:
- def_natural_power
- ax_distributive_law
- thm_right_distributive_law
- ax_addition_commutativity
- ax_addition_associativity
is_canonical: true
date_added: '2026-06-28T15:49:27.765195Z'
schema_version: 1
---

לפי הגדרת חזקה טבעית ($\texttt{def\_natural\_power}$): $(a+b)^2 = (a+b) \cdot (a+b)$.

נפעיל את חוק הפילוג הימני ($\texttt{thm\_right\_distributive\_law}$) על המכפלה $(a+b) \cdot (a+b)$, כאשר נתייחס לגורם הראשון $(a+b)$ כסכום של שני איברים:

$(a+b) \cdot (a+b) = a \cdot (a+b) + b \cdot (a+b)$.

כעת נפעיל את חוק הפילוג השמאלי ($\texttt{ax\_distributive\_law}$) על כל אחד משני המחוברים:

$a \cdot (a+b) = a \cdot a + a \cdot b$,

$b \cdot (a+b) = b \cdot a + b \cdot b$.

לכן:

$(a+b)^2 = a \cdot a + a \cdot b + b \cdot a + b \cdot b$.

לפי הגדרת חזקה טבעית, $a \cdot a = a^2$ ו-$b \cdot b = b^2$. בנוסף, לפי חוק החילוף בכפל (נובע מקומוטטיביות הכפל), $b \cdot a = a \cdot b$. נשתמש גם בקומוטטיביות החיבור ($\texttt{ax\_addition\_commutativity}$) וחוק הקיבוץ ($\texttt{ax\_addition\_associativity}$) כדי לקבץ את שני האיברים $a \cdot b$:

$(a+b)^2 = a^2 + a \cdot b + a \cdot b + b^2 = a^2 + 2 \cdot (a \cdot b) + b^2 = a^2 + 2ab + b^2$.

כאן השתמשנו בכך ש-$a \cdot b + a \cdot b = (1+1) \cdot (a \cdot b) = 2 \cdot (a \cdot b)$ לפי חוק הפילוג הימני ($\texttt{thm\_right\_distributive\_law}$). $\blacksquare$
