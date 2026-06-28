---
id: prf_repeating_decimal_to_fraction
claim_id: thm_repeating_decimal_to_fraction
method: informal
status: reviewed
dependencies:
- def_repeating_decimal
- def_decimal
- thm_fraction_subtraction
- thm_geometric_series_convergence
- def_rational_numbers
- def_natural_power
is_canonical: true
date_added: '2026-06-28T20:34:16.480529Z'
schema_version: 1
---

**שיטה: הכפלה ב-$10^p$ וחיסור.**

יהי $x = 0.\overline{d_1 d_2 \ldots d_p}$ עשרוני חוזר טהור (ללא חלק לא-מחזורי), כאשר ספרות המחזור הן $d_1, d_2, \ldots, d_p$ (לפי def_repeating_decimal).

לפי הגדרת מספר עשרוני (def_decimal) ולפי המחזוריות:
$$x = \sum_{j=0}^{\infty} \left( \sum_{i=1}^{p} d_i \cdot 10^{-i} \right) \cdot 10^{-jp} = \left( \sum_{i=1}^{p} d_i \cdot 10^{-i} \right) \cdot \sum_{j=0}^{\infty} 10^{-jp}$$

הסכום הפנימי $\sum_{i=1}^{p} d_i \cdot 10^{-i} = \frac{N}{10^p}$ כאשר $N = d_1 \cdot 10^{p-1} + d_2 \cdot 10^{p-2} + \cdots + d_p$ הוא המספר השלם שספרותיו הן $d_1 d_2 \ldots d_p$ (לפי def_natural_power).

הסכום החיצוני הוא טור הנדסי עם מנה $q = 10^{-p}$ ו-$|q| < 1$, ולכן מתכנס לפי משפט התכנסות טור הנדסי (thm_geometric_series_convergence):
$$\sum_{j=0}^{\infty} 10^{-jp} = \frac{1}{1 - 10^{-p}}$$

לכן:
$$x = \frac{N}{10^p} \cdot \frac{1}{1 - 10^{-p}} = \frac{N}{10^p \cdot (1 - 10^{-p})} = \frac{N}{10^p - 1}$$

(במעבר האחרון השתמשנו ב-$10^p \cdot (1 - 10^{-p}) = 10^p - 10^p \cdot 10^{-p} = 10^p - 1$.)

אלטרנטיבית, ניתן להראות את אותו דבר בלי טורים: נסמן $y = 10^p \cdot x$. הספרות של $y$ אחרי הנקודה הן שוב אותן ספרות מחזור $d_1 d_2 \ldots d_p$ חוזרות (כיוון ש-$x$ מחזורי באורך $p$), והחלק השלם של $y$ הוא $N$. כלומר $y = N + x$. נחסר את $x$ משני האגפים (thm_fraction_subtraction אינו נחוץ כאן ישירות אלא חוקי שדה בסיסיים — לחילופין, נסתפק בכך שזו אופציה אינטואיטיבית):
$$10^p \cdot x - x = N \implies (10^p - 1) \cdot x = N \implies x = \frac{N}{10^p - 1}$$

$N$ הוא שלם (סכום של מכפלות שלמים), ו-$10^p - 1$ הוא שלם חיובי (לפי def_natural_power), כלומר $10^p - 1 \neq 0$. לפיכך $x$ נכתב כשבר של שלמים, ולפי הגדרת מספרים רציונליים (def_rational_numbers), $x \in \mathbb{Q}$.

**מקרה כללי (עם חלק לא-מחזורי):** אם $x = a.d_1 \ldots d_k \overline{e_1 \ldots e_p}$, אז $10^k \cdot x = (a d_1 \ldots d_k).\overline{e_1 \ldots e_p}$, וניתן להפעיל את הטיעון לעיל על $10^k \cdot x$ פחות החלק השלם, לקבל ערך רציונלי, ולחלק חזרה ב-$10^k$ כדי לקבל את $x$.

**דוגמאות:**
- $0.\overline{3}$: $N = 3$, $p = 1$, $x = \frac{3}{10 - 1} = \frac{3}{9} = \frac{1}{3}$.
- $0.\overline{142857}$: $N = 142857$, $p = 6$, $x = \frac{142857}{999999} = \frac{1}{7}$.
- $0.\overline{9}$: $N = 9$, $p = 1$, $x = \frac{9}{9} = 1$ (תוצאה ידועה).

$\blacksquare$
