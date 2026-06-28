---
id: prf_common_denominator
claim_id: def_common_denominator
method: informal
status: reviewed
dependencies:
- def_fraction
- thm_fraction_simplification
- def_lcm
is_canonical: true
date_added: '2026-06-28T20:34:16.466011Z'
schema_version: 1
---

נראה שההגדרה היא בעלת משמעות: כלומר, אם $m$ הוא כפולה משותפת של $b$ ו-$d$, אז ניתן לכתוב את $\frac{a}{b}$ ו-$\frac{c}{d}$ בצורה שבה למונה יש מכנה $m$.

נניח $m = b \cdot k = d \cdot \ell$ עבור שלמים חיוביים $k, \ell$. לפי פישוט שברים (thm_fraction_simplification), עבור כל $k \neq 0$:
$$\frac{a}{b} = \frac{a \cdot k}{b \cdot k} = \frac{a \cdot k}{m}$$

ובאופן דומה:
$$\frac{c}{d} = \frac{c \cdot \ell}{d \cdot \ell} = \frac{c \cdot \ell}{m}$$

כלומר, $a' = a \cdot k$ ו-$c' = c \cdot \ell$. שניהם שלמים, וכעת לשני השברים יש את אותו מכנה $m$ (לפי הגדרת שבר, def_fraction).

באשר למינימליות: לפי הגדרת LCM (def_lcm), $\text{lcm}(b, d)$ הוא המספר החיובי הקטן ביותר שגם $b$ וגם $d$ מחלקים אותו. לכן כל מכנה משותף $m$ של $\frac{a}{b}$ ו-$\frac{c}{d}$ מקיים $\text{lcm}(b, d) \mid m$, ובפרט $m \geq \text{lcm}(b, d)$. מכאן ש-$\text{lcm}(b, d)$ הוא אכן המכנה המשותף המינימלי.

לדוגמה: עבור $\frac{1}{6}$ ו-$\frac{1}{4}$, $\text{lcm}(6, 4) = 12$, ולכן $\frac{1}{6} = \frac{2}{12}$ ו-$\frac{1}{4} = \frac{3}{12}$. $\blacksquare$
