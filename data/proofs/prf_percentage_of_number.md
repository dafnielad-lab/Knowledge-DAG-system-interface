---
id: prf_percentage_of_number
claim_id: thm_percentage_of_number
method: informal
status: reviewed
dependencies:
- def_percentage
- def_fraction
- ax_multiplication_associativity
is_canonical: true
date_added: '2026-06-28T15:49:27.782201Z'
schema_version: 1
---

**שלב 1 — פירוש הביטוי "של":** המילה "של" בהקשר של אחוזים (כמו במשפט "רבע של 80") מתורגמת לפעולת כפל. כלומר "$x\%$ של $a$" פירושו $x\% \cdot a$.

**שלב 2 — הצבת הגדרת האחוז:** לפי `def_percentage`, $x\% = \frac{x}{100}$. לכן:
$$ x\% \text{ של } a = x\% \cdot a = \frac{x}{100} \cdot a $$

**שלב 3 — צורה שקולה:** לפי `def_fraction`, $\frac{x}{100} = x \cdot 100^{-1}$, ולכן:
$$ \frac{x}{100} \cdot a = (x \cdot 100^{-1}) \cdot a $$
לפי אסוציאטיביות הכפל (`ax_multiplication_associativity`):
$$ (x \cdot 100^{-1}) \cdot a = x \cdot (100^{-1} \cdot a) = \frac{x \cdot a}{100} $$
כלומר ניתן לכתוב את התוצאה גם בצורה $\frac{x \cdot a}{100}$.

**דוגמאות:**
- $20\%$ של $50$: $\frac{20}{100} \cdot 50 = \frac{1000}{100} = 10$.
- $15\%$ של $200$: $\frac{15}{100} \cdot 200 = \frac{3000}{100} = 30$.
- $7\%$ של $1000$: $\frac{7}{100} \cdot 1000 = \frac{7000}{100} = 70$.
- $100\%$ של $a$: $\frac{100}{100} \cdot a = 1 \cdot a = a$ (השלם).
- $200\%$ של $30$: $\frac{200}{100} \cdot 30 = 2 \cdot 30 = 60$ (פעמיים).

**הערה — קישור לפרופורציה:** ניתן לראות את חישוב האחוזים גם כפרופורציה: "$x\%$ של $a$" שווה ל-$y$ אם ורק אם $\frac{y}{a} = \frac{x}{100}$. לפי כפל הצלבי (`thm_proportion_cross_multiply`, אם משתמשים), $100 \cdot y = x \cdot a$, ומכאן $y = \frac{x \cdot a}{100}$ — בדיוק התוצאה שקיבלנו. זוהי גישה חלופית לחישוב המקובלת במיוחד בכיתות נמוכות. $\blacksquare$
