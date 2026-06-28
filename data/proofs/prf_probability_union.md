---
id: prf_probability_union
claim_id: thm_probability_union
method: informal
status: reviewed
dependencies:
- def_probability_measure
- ax_probability_additivity
- def_set_union
- def_set_intersection
is_canonical: true
date_added: '2026-06-28T15:49:27.881195Z'
schema_version: 1
---

נסתמך על שלוש האקסיומות של פונקציית ההסתברות כפי שמסוכמות ב-`def_probability_measure`, ובפרט על אדיטיביות עבור איחוד זר (`ax_probability_additivity`).

**רעיון: לפרק את האיחוד ואת $B$ לאיחודי קבוצות זרות.** נסמן $B \setminus A = \{x \in B : x \notin A\}$ (החלק של $B$ שאינו ב-$A$).

**פירוק 1 — איחוד.** לכל $x \in A \cup B$ (לפי `def_set_union`, $x$ ב-$A$ או ב-$B$) מתקיים בדיוק אחד משני המקרים: $x \in A$, או $x \in B$ ו-$x \notin A$ (כלומר $x \in B \setminus A$). לכן
$$A \cup B = A \cup (B \setminus A),$$
והאיחוד הזה זר: $A \cap (B \setminus A) = \emptyset$ (אם $x \in A$ אז $x \notin B \setminus A$).

לפי `ax_probability_additivity` (לאיחוד זר של שני מאורעות):
$$P(A \cup B) = P(A) + P(B \setminus A). \quad (\ast)$$

**פירוק 2 — את $B$.** לכל $x \in B$ מתקיים בדיוק אחד מהמקרים: $x \in A$ (ואז $x \in A \cap B$ לפי `def_set_intersection`), או $x \notin A$ (ואז $x \in B \setminus A$). לכן
$$B = (A \cap B) \cup (B \setminus A),$$
והאיחוד זר: $(A \cap B) \cap (B \setminus A) = \emptyset$ (איבר ב-$A \cap B$ נמצא ב-$A$, ואיבר ב-$B \setminus A$ אינו ב-$A$).

לפי `ax_probability_additivity`:
$$P(B) = P(A \cap B) + P(B \setminus A),$$
ומכאן
$$P(B \setminus A) = P(B) - P(A \cap B). \quad (\ast\ast)$$

**הצבה.** מהצבת $(\ast\ast)$ ב-$(\ast)$:
$$P(A \cup B) = P(A) + P(B) - P(A \cap B). \quad \blacksquare$$

שימו לב: כאשר $A, B$ זרים, $P(A \cap B) = P(\emptyset) = 0$ והנוסחה מתלכדת עם אדיטיביות הסטנדרטית.
