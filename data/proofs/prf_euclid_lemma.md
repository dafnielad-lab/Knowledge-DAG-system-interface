---
id: prf_euclid_lemma
claim_id: thm_euclid_lemma
method: informal
status: reviewed
dependencies:
- def_prime
- def_divisibility
- def_gcd
- thm_bezout_identity
- thm_divisibility_linear_combinations
is_canonical: true
date_added: '2026-06-28T15:07:55.428550Z'
schema_version: 1
---

נניח ש-$p$ ראשוני ו-$p \mid a \cdot b$. נראה שאם $p \nmid a$ אזי בהכרח $p \mid b$.

**שלב 1 — חישוב $\gcd(p, a)$.** לפי [def_prime], המחלקים החיוביים היחידים של $p$ הם $1$ ו-$p$. לכן, לפי [def_gcd], $\gcd(p, a) \in \{1, p\}$: זהו המחלק החיובי הגדול ביותר המשותף ל-$p$ ול-$a$, והוא חייב להיות מחלק חיובי של $p$. אם $\gcd(p, a) = p$, אזי לפי [def_divisibility] $p \mid a$, בניגוד להנחה. נותר $\gcd(p, a) = 1$, כלומר $p$ ו-$a$ זרים.

**שלב 2 — הפעלת זהות בזו.** לפי [thm_bezout_identity], מכיוון ש-$\gcd(p, a) = 1$, קיימים שלמים $x, y$ כך ש-
$$p \cdot x + a \cdot y = 1.$$

**שלב 3 — כפל ב-$b$.** נכפול את שני האגפים ב-$b$:
$$p \cdot (x b) + (a b) \cdot y = b.$$

**שלב 4 — סיום באמצעות צירוף לינארי.** מתקיים $p \mid p$ באופן טריוויאלי, ומההנחה $p \mid a b$. לפי [thm_divisibility_linear_combinations], כל צירוף לינארי שלם של שני מספרים שמתחלקים ב-$p$ גם הוא מתחלק ב-$p$. לכן
$$p \;\Big|\; p \cdot (x b) + (a b) \cdot y = b,$$
כלומר $p \mid b$.

**מסקנה.** הוכחנו: אם $p \nmid a$ אז $p \mid b$. שקול לכך: $p \mid a$ או $p \mid b$, כנדרש. $\blacksquare$
