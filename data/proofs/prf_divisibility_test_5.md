---
id: prf_divisibility_test_5
claim_id: thm_divisibility_test_5
method: informal
status: reviewed
dependencies:
- def_divisibility
- def_integers
- thm_divisibility_linear_combinations
- thm_division_algorithm
is_canonical: true
date_added: '2026-06-28T20:34:16.507583Z'
schema_version: 1
---

**מטרה:** להוכיח ש-$5 \mid n$ אם ורק אם ספרת היחידות $d_0 \in \{0, 5\}$.

**שלב 1: ייצוג עשרוני של $n$.**

לפי `def_integers`, $n \in \mathbb{Z}$. נכתוב את $n$ בצורה $n = d_k \cdot 10^k + \cdots + d_1 \cdot 10 + d_0$, כאשר $d_i$ הן הספרות העשרוניות ו-$d_0$ ספרת היחידות.

נגדיר $M := d_k \cdot 10^{k-1} + \cdots + d_1$, ואזי:

$$n = 10 \cdot M + d_0$$

זהו אלגוריתם החילוק (`thm_division_algorithm`) עם $b = 10$, $q = M$, $r = d_0$, $0 \leq d_0 < 10$.

**שלב 2: $5 \mid 10$.**

לפי `def_divisibility`, $5 \mid 10$ כי $10 = 5 \cdot 2$. לכן לכל $M \in \mathbb{Z}$, $5 \mid (10M)$, שכן $10M = 5 \cdot (2M)$.

**שלב 3: כיוון $\Leftarrow$.**

נניח $d_0 \in \{0, 5\}$. אזי $5 \mid d_0$ (כי $0 = 5 \cdot 0$, $5 = 5 \cdot 1$). מאחר ש-$5 \mid 10M$ ו-$5 \mid d_0$, על-פי `thm_divisibility_linear_combinations` (עם $m = n = 1$):

$$5 \mid (10M + d_0) = n.$$

**שלב 4: כיוון $\Rightarrow$.**

נניח $5 \mid n$. נכתוב $d_0 = n - 10M$. על-פי `thm_divisibility_linear_combinations` (עם $m = 1, n' = -1$): מאחר ש-$5 \mid n$ וגם $5 \mid 10M$, נקבל:

$$5 \mid (n - 10M) = d_0.$$

כעת $0 \leq d_0 \leq 9$ מהאלגוריתם (`thm_division_algorithm`). הכפולות של $5$ בטווח $[0, 9]$ הן $0$ ו-$5$ בלבד. לכן $d_0 \in \{0, 5\}$.

**שלב 5: מספרים שליליים.**

עבור $n < 0$, ספרת היחידות מוגדרת באמצעות $|n|$. מאחר ש-$5 \mid n \iff 5 \mid (-n)$, ו-$|n|$ ו-$-n$ הם אותו מספר, הטענה תקפה גם עבור שליליים.

$\blacksquare$

**דוגמאות:**

- $n = 245$: ספרת היחידות $5$, ולכן $5 \mid 245$ (אכן $245 = 5 \cdot 49$).
- $n = 730$: ספרת היחידות $0$, ולכן $5 \mid 730$ (אכן $730 = 5 \cdot 146$).
- $n = 123$: ספרת היחידות $3 \notin \{0,5\}$, ולכן $5 \nmid 123$.
