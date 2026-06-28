---
id: prf_de_morgan_logic
claim_id: thm_de_morgan_logic
method: informal
status: reviewed
dependencies: []
is_canonical: true
date_added: '2026-06-28T20:34:16.437094Z'
schema_version: 1
---

מוכיחים בטבלת אמת. כל אחד מהפסוקים $P, Q$ מקבל אחד משני ערכים: T (אמת) או F (שקר). יש $2 \times 2 = 4$ צירופים אפשריים.

**שקילות א'** — $\neg(P \land Q) \iff (\neg P) \lor (\neg Q)$:

| $P$ | $Q$ | $P \land Q$ | $\neg(P \land Q)$ | $\neg P$ | $\neg Q$ | $(\neg P) \lor (\neg Q)$ |
|---|---|---|---|---|---|---|
| T | T | T | F | F | F | F |
| T | F | F | T | F | T | T |
| F | T | F | T | T | F | T |
| F | F | F | T | T | T | T |

העמודות "$\neg(P \land Q)$" ו-"$(\neg P) \lor (\neg Q)$" זהות בכל 4 השורות, אז הפסוקים שקולים לוגית.

**שקילות ב'** — $\neg(P \lor Q) \iff (\neg P) \land (\neg Q)$:

| $P$ | $Q$ | $P \lor Q$ | $\neg(P \lor Q)$ | $\neg P$ | $\neg Q$ | $(\neg P) \land (\neg Q)$ |
|---|---|---|---|---|---|---|
| T | T | T | F | F | F | F |
| T | F | T | F | F | T | F |
| F | T | T | F | T | F | F |
| F | F | F | T | T | T | T |

שוב — שתי העמודות הסופיות זהות, אז הפסוקים שקולים.

**הערה:** אפשר להסיק את גרסת-הקבוצות (thm_demorgan_sets_intersection, thm_demorgan_sets_union) מהגרסה הלוגית הזו על-ידי החלפת $P$ ב-"$x \in A$" ו-$Q$ ב-"$x \in B$". $\blacksquare$
