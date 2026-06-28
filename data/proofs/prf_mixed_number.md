---
id: prf_mixed_number
claim_id: def_mixed_number
method: informal
status: reviewed
dependencies:
- def_fraction
- def_natural_numbers
- def_rational_numbers
is_canonical: true
date_added: '2026-06-28T20:34:16.460616Z'
schema_version: 1
---

זוהי הגדרה של סוג מסוים של הצגה למספר רציונלי, ולכן יש לאמת שהיא קוהרנטית — כלומר שלכל בחירה של $a, b, c$ העונים על התנאים, אכן מתקבל מספר רציונלי יחיד ומוגדר היטב.

לפי הגדרת מספרים טבעיים (def_natural_numbers), $a, b, c \in \mathbb{N}$ הם מספרים מוגדרים היטב; התנאי $c > 0$ מבטיח ש-$c \neq 0$.

לפי הגדרת שבר (def_fraction), $\frac{b}{c} = b \cdot c^{-1}$ הוא מספר מוגדר היטב כאשר $c \neq 0$. התנאי $0 \leq b < c$ מבטיח שהשבר $\frac{b}{c}$ הוא מספר בטווח $[0, 1)$ (השבר אינו עולה על 1).

הסכום $a + \frac{b}{c}$ הוא סכום של מספר טבעי ושל שבר; שניהם מספרים רציונליים (def_rational_numbers), שכן $a = \frac{a}{1}$ הוא מנה של שלמים ו-$\frac{b}{c}$ הוא בהגדרה מנה של שלמים. סכום של שני רציונליים הוא רציונלי. כלומר, ההצגה $a\frac{b}{c}$ מייצגת בדיוק מספר רציונלי אחד.

לדוגמה: $2\frac{3}{4}$ מייצג את המספר $2 + \frac{3}{4} = \frac{11}{4}$, שהוא רציונלי. $\blacksquare$
