---
id: prf_chinese_remainder_theorem
claim_id: thm_chinese_remainder_theorem
method: informal
status: reviewed
dependencies:
- def_congruence_mod
- thm_bezout_identity
- thm_euclid_lemma
- def_proof_by_induction
is_canonical: true
date_added: '2026-06-28T15:02:41.600551Z'
schema_version: 1
---

**הוכחה קונסטרוקטיבית באינדוקציה על $k$.**

*בסיס ($k = 2$):* נתון $\gcd(n_1, n_2) = 1$. ממשפט בזו קיימים $u, v \in \mathbb{Z}$ כך ש־$1 = n_1 u + n_2 v$. נגדיר $x = a_2 \cdot n_1 u + a_1 \cdot n_2 v$. אז $x \equiv a_1 \cdot n_2 v \equiv a_1 \cdot (1 - n_1 u) \equiv a_1 \pmod{n_1}$, ובדומה $x \equiv a_2 \pmod{n_2}$.

*צעד אינדוקציה:* נניח שהטענה נכונה עבור $k-1$ מודולוסים. בהינתן $n_1, \ldots, n_k$ זרים בזוגות, מהנחת האינדוקציה קיים $y$ הפותר את $k-1$ הקונגרואנציות הראשונות מודולו $M = n_1 \cdots n_{k-1}$. כיוון ש־$n_k$ זר לכל $n_i$ ($i < k$), הוא זר גם למכפלה $M$. נפעיל את מקרה $k=2$ על המערכת $x \equiv y \pmod{M}$, $x \equiv a_k \pmod{n_k}$ ונקבל פתרון $x$. ההסתמכות על עקרון האינדוקציה השלמה מוצדקת לפי סכמת ההוכחה באינדוקציה.

*יחידות מודולו $N = \prod_{i=1}^{k} n_i$:* נניח ש־$x, x'$ שני פתרונות. אז $n_i \mid (x - x')$ לכל $i$. כיוון שה־$n_i$ זרים בזוגות, מלמת אוקלידס (בהפעלה חוזרת) נובע ש־$N = \prod n_i \mid (x - x')$, כלומר $x \equiv x' \pmod{N}$. $\blacksquare$
