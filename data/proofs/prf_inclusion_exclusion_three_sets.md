---
id: prf_inclusion_exclusion_three_sets
claim_id: thm_inclusion_exclusion_three_sets
method: informal
status: reviewed
dependencies:
- thm_inclusion_exclusion_two_sets
- def_set_union
- def_set_intersection
is_canonical: true
date_added: '2026-06-27T17:22:39.263705Z'
schema_version: 1
---

$|A \cup B \cup C| = |(A \cup B) \cup C| = |A \cup B| + |C| - |(A \cup B) \cap C|$.

פיתוח: $(A \cup B) \cap C = (A \cap C) \cup (B \cap C)$. הפעלה שוב של הכלה-הפרדה: $|(A \cup B) \cap C| = |A \cap C| + |B \cap C| - |A \cap B \cap C|$.

הצבה והחלפת $|A \cup B|$ נותנת את הזהות. $\blacksquare$
