---
id: prf_divisibility_test_3_9
claim_id: thm_divisibility_test_3_9
method: informal
status: reviewed
dependencies:
- def_divisibility
- def_integers
- thm_divisibility_linear_combinations
- thm_divisibility_transitivity
is_canonical: true
date_added: '2026-06-28T20:34:16.504583Z'
schema_version: 1
---

**מטרה:** להוכיח ש-$d \mid n \iff d \mid S(n)$ עבור $d \in \{3, 9\}$.

**שלב 1: ייצוג עשרוני.**

לפי `def_integers`, נסתכל על $n \in \mathbb{Z}$. ללא הגבלת הכלליות נניח $n \geq 0$ (כי $d \mid n \iff d \mid (-n)$ ו-$S(n) = S(-n)$). נכתוב:

$$n = \sum_{i=0}^{k} d_i \cdot 10^i = d_k \cdot 10^k + d_{k-1} \cdot 10^{k-1} + \cdots + d_1 \cdot 10 + d_0$$

כאשר $d_i \in \{0, 1, \ldots, 9\}$ הן ספרות $n$. אזי:

$$S(n) = d_k + d_{k-1} + \cdots + d_1 + d_0$$

**שלב 2: זהות מרכזית — $10^i = 9 \cdot M_i + 1$.**

טענה: לכל $i \geq 0$, ניתן לכתוב $10^i = 9 \cdot M_i + 1$ עם $M_i \in \mathbb{Z}$ אי-שלילי. כלומר, $9 \mid (10^i - 1)$.

*הוכחה באינדוקציה על $i$:*

- *בסיס:* $i = 0$: $10^0 - 1 = 1 - 1 = 0 = 9 \cdot 0$, כך ש-$9 \mid (10^0 - 1)$.
- *מעבר:* נניח $10^i - 1 = 9 M_i$. אזי:

$$10^{i+1} - 1 = 10 \cdot 10^i - 1 = 10 \cdot (9 M_i + 1) - 1 = 90 M_i + 10 - 1 = 90 M_i + 9 = 9(10 M_i + 1).$$

לכן $M_{i+1} = 10 M_i + 1 \in \mathbb{Z}$, וההצגה נשמרת.

מכאן, על-פי `def_divisibility`, $9 \mid (10^i - 1)$ לכל $i \geq 0$.

**שלב 3: גם $3 \mid (10^i - 1)$.**

מאחר ש-$3 \mid 9$ (שכן $9 = 3 \cdot 3$) ו-$9 \mid (10^i - 1)$, על-פי `thm_divisibility_transitivity` נקבל $3 \mid (10^i - 1)$.

**שלב 4: כתיבה מחדש של $n - S(n)$.**

נחשב:

$$n - S(n) = \sum_{i=0}^{k} d_i \cdot 10^i - \sum_{i=0}^{k} d_i = \sum_{i=0}^{k} d_i (10^i - 1).$$

**שלב 5: הוכחה ש-$d \mid (n - S(n))$ עבור $d \in \{3, 9\}$.**

משלבים 2-3, $d \mid (10^i - 1)$ לכל $i$. לכן $d \mid d_i(10^i - 1)$ לכל $i$ (כי $d_i \in \mathbb{Z}$).

בשימוש חוזר ב-`thm_divisibility_linear_combinations` (סכום של איברים שכולם מתחלקים ב-$d$ מתחלק ב-$d$), נקבל:

$$d \mid \sum_{i=0}^{k} d_i (10^i - 1) = n - S(n).$$

**שלב 6: שקילות התחלקות $n$ ו-$S(n)$.**

ניצור את צירוף לינארי בשני הכיוונים, על-פי `thm_divisibility_linear_combinations`:

*כיוון $\Rightarrow$:* אם $d \mid n$ וגם $d \mid (n - S(n))$, אז:
$$d \mid \big(n - (n - S(n))\big) = S(n).$$

*כיוון $\Leftarrow$:* אם $d \mid S(n)$ וגם $d \mid (n - S(n))$, אז:
$$d \mid \big(S(n) + (n - S(n))\big) = n.$$

לכן $d \mid n \iff d \mid S(n)$, עבור $d = 3$ ועבור $d = 9$. $\blacksquare$

**דוגמאות מספריות:**

- $n = 1\,234$: $S(n) = 1 + 2 + 3 + 4 = 10$. $3 \nmid 10$ ולכן $3 \nmid 1234$.
- $n = 1\,233$: $S(n) = 1 + 2 + 3 + 3 = 9$. $9 \mid 9$ ולכן $9 \mid 1233$ (ובאמת $1233 = 9 \cdot 137$).
- $n = 4\,567$: $S(n) = 22$, ו-$3 \nmid 22$, $9 \nmid 22$ — לכן $3 \nmid 4567$ ו-$9 \nmid 4567$.
