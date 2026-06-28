---
id: prf_divisibility_test_2
claim_id: thm_divisibility_test_2
method: informal
status: reviewed
dependencies:
- def_divisibility
- def_integers
- thm_divisibility_linear_combinations
- thm_division_algorithm
is_canonical: true
date_added: '2026-06-28T20:34:16.501573Z'
schema_version: 1
---

**מטרה:** להוכיח ש-$2 \mid n$ אם ורק אם ספרת היחידות של $n$ היא $\{0, 2, 4, 6, 8\}$.

**שלב 1: ייצוג עשרוני של מספר שלם.**

לפי `def_integers`, $n \in \mathbb{Z}$. נכתוב את $n$ במערכת העשרונית בצורה $n = d_k d_{k-1} \cdots d_1 d_0$ (כאשר $d_i$ הן ספרות $0$ עד $9$, ו-$d_0$ היא ספרת היחידות). אזי:

$$n = d_k \cdot 10^k + d_{k-1} \cdot 10^{k-1} + \cdots + d_1 \cdot 10 + d_0$$

**שלב 2: הפרדה לפי החלוקה ב-$10$.**

נגדיר $M := d_k \cdot 10^{k-1} + d_{k-1} \cdot 10^{k-2} + \cdots + d_1$, כך ש:

$$n = 10 \cdot M + d_0$$

זהו ייצוג של $n$ על-פי `thm_division_algorithm` עם $b = 10$, $q = M$, $r = d_0$ (כאשר $0 \leq d_0 < 10$).

**שלב 3: $10$ מתחלק ב-$2$.**

לפי `def_divisibility`, $2 \mid 10$ כי $10 = 2 \cdot 5$. לכן לכל $M \in \mathbb{Z}$, גם $2 \mid (10 \cdot M)$, כי $10 \cdot M = 2 \cdot (5M)$.

**שלב 4: שימוש בצירוף לינארי.**

לפי `thm_divisibility_linear_combinations`: אם $2 \mid a$ ו-$2 \mid b$ אז $2 \mid (a + b)$.

*כיוון $\Leftarrow$:* נניח שספרת היחידות $d_0 \in \{0, 2, 4, 6, 8\}$. אזי $2 \mid d_0$ (כי $0 = 2 \cdot 0$, $2 = 2 \cdot 1$, $4 = 2 \cdot 2$, $6 = 2 \cdot 3$, $8 = 2 \cdot 4$). מאחר ש-$2 \mid 10M$ ו-$2 \mid d_0$, נקבל מ-`thm_divisibility_linear_combinations` ש-$2 \mid (10M + d_0) = n$.

*כיוון $\Rightarrow$:* נניח $2 \mid n$. נכתוב $d_0 = n - 10M$. מאחר ש-$2 \mid n$ ו-$2 \mid 10M$, מ-`thm_divisibility_linear_combinations` עם $m=1, n=-1$ נקבל $2 \mid (n - 10M) = d_0$. מאחר ש-$0 \leq d_0 \leq 9$, האפשרויות היחידות הן $d_0 \in \{0, 2, 4, 6, 8\}$ (הספרות הזוגיות בין $0$ ל-$9$).

**שלב 5: הערה על מספרים שליליים.**

עבור $n < 0$, נכתוב $n = -|n|$. מאחר ש-$2 \mid n \iff 2 \mid (-n) = |n|$, וספרת היחידות של $|n|$ זהה לזו של $n$ (בהתעלם מסימן המינוס), הטענה נשמרת.

$\blacksquare$
