---
id: prf_equivalence_relation
claim_id: def_equivalence_relation
method: informal
status: reviewed
dependencies:
- def_set
- def_subset
- def_cartesian_product
is_canonical: true
date_added: '2026-06-28T21:06:29.416562Z'
schema_version: 1
---

ההגדרה בנויה מהפרימיטיבים הבאים: def_set מספקת את המושג של הקבוצה $A$; def_cartesian_product מגדירה את $A \times A$ כאוסף הזוגות הסדורים $(a,b)$ עם $a,b \in A$; def_subset מאפשרת לזהות את היחס $\sim$ עם תת-קבוצה $R \subseteq A \times A$, כאשר הסימון $a \sim b$ הוא קיצור ל-$(a,b) \in R$. שלוש התכונות — רפלקסיביות, סימטריה, וטרנזיטיביות — הן תנאים על איברי תת-הקבוצה $R$: רפלקסיביות דורשת $(a,a) \in R$ לכל $a$; סימטריה דורשת $(a,b) \in R \Rightarrow (b,a) \in R$; טרנזיטיביות דורשת ש-$(a,b),(b,c) \in R \Rightarrow (a,c) \in R$. כאשר כל שלוש התכונות מתקיימות, אומרים ש-$\sim$ הוא יחס שקילות. ההגדרה היא הגדרה טהורה — אין כאן טענה הדורשת הוכחה, רק רשימה מוסכמת של תכונות.
