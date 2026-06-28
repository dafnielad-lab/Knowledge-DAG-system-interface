---
id: prf_decimal_fraction_conversion
claim_id: thm_decimal_fraction_conversion
method: informal
status: reviewed
dependencies:
- def_decimal
- def_fraction
- thm_fraction_addition
- thm_fraction_simplification
- def_natural_power
is_canonical: true
date_added: '2026-06-28T20:34:16.475019Z'
schema_version: 1
---

**כיוון 1: ממספר עשרוני סופי לשבר.**

לפי הגדרת מספר עשרוני (def_decimal), המספר $a.d_1 d_2 \ldots d_n$ (כאשר $d_i = 0$ עבור $i > n$) הוא הסכום:
$$a + \sum_{i=1}^{n} d_i \cdot 10^{-i} = a + \frac{d_1}{10} + \frac{d_2}{10^2} + \cdots + \frac{d_n}{10^n}$$
(לפי def_fraction, $10^{-i} = \frac{1}{10^i}$, וההגדרה של חזקה טבעית def_natural_power מבטיחה ש-$10^i$ מוגדר היטב לכל $i \in \mathbb{N}$.)

נכפול ונחלק כל מחובר ב-$10^n$ כדי לאחד תחת אותו מכנה. לפי פישוט שברים (thm_fraction_simplification):
$$\frac{d_i}{10^i} = \frac{d_i \cdot 10^{n-i}}{10^i \cdot 10^{n-i}} = \frac{d_i \cdot 10^{n-i}}{10^n}$$
(השתמשנו ב-$10^i \cdot 10^{n-i} = 10^n$, חוק חזקות שניתן להוכיח ישירות מ-def_natural_power באינדוקציה.)

גם $a$ נכתב כ-$\frac{a \cdot 10^n}{10^n}$.

כעת לפי חיבור שברים (thm_fraction_addition) המוחל $n+1$ פעמים (או באינדוקציה), כל המחוברים בעלי המכנה $10^n$ מתאחדים:
$$\frac{a \cdot 10^n}{10^n} + \frac{d_1 \cdot 10^{n-1}}{10^n} + \cdots + \frac{d_n}{10^n} = \frac{a \cdot 10^n + d_1 \cdot 10^{n-1} + \cdots + d_n}{10^n}$$

זוהי בדיוק הצורה הנדרשת.

**כיוון 2: משבר $\frac{N}{10^n}$ למספר עשרוני סופי.**

ניתן שבר $\frac{N}{10^n}$ עם $N \in \mathbb{Z}$ ו-$n \in \mathbb{N}$. נכתוב את $N$ בייצוג עשרוני: לכל מספר שלם $N$ קיימת הצגה $N = a_k a_{k-1} \ldots a_1 a_0$ בבסיס 10, כלומר $N = \sum_{j=0}^{k} a_j \cdot 10^j$ עם $a_j \in \{0, \ldots, 9\}$ (זהו תכונת הצגה בבסיס 10, נושא בהגדרת def_decimal).

כעת:
$$\frac{N}{10^n} = \frac{\sum_{j=0}^{k} a_j \cdot 10^j}{10^n} = \sum_{j=0}^{k} \frac{a_j \cdot 10^j}{10^n} = \sum_{j=0}^{k} a_j \cdot 10^{j-n}$$

אם $j \geq n$, מקבלים את החלק השלם; אם $j < n$, מקבלים $a_j \cdot 10^{j-n} = \frac{a_j}{10^{n-j}}$, שזה תרומת ספרה במקום השברי $(n-j)$ אחרי הנקודה. הסכום הוא מספר עשרוני סופי עם לכל היותר $n$ ספרות אחרי הנקודה, לפי def_decimal.

לדוגמה: $\frac{125}{100} = 1.25$ (כאן $N = 125$, $n = 2$). $\blacksquare$
