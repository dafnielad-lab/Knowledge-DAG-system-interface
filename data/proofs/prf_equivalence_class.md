---
id: prf_equivalence_class
claim_id: def_equivalence_class
method: informal
status: reviewed
dependencies:
- def_set
- def_equivalence_relation
is_canonical: true
date_added: '2026-06-28T21:06:29.442178Z'
schema_version: 1
---

ההגדרה משתמשת ב-def_set (קבוצה $A$ עם איברים) וב-def_equivalence_relation (היחס $\sim$ עם שלוש התכונות: רפלקסיביות, סימטריה, טרנזיטיביות). $[a]$ מוגדרת באמצעות סכמת ההפרדה: היא תת-קבוצה של $A$ המכילה בדיוק את האיברים $x$ המקיימים את התנאי $x \sim a$. תכונה בסיסית: לכל $a \in A$ מתקיים $a \in [a]$, מכוח רפלקסיביות ($a \sim a$); לכן אף מחלקה אינה ריקה. למה: אם $b \in [a]$ אזי $[a] = [b]$. נימוק קצר: $b \in [a]$ פירושו $b \sim a$, ולכן גם $a \sim b$ לפי סימטריה. עבור $x \in [a]$ מתקיים $x \sim a$ ובצירוף $a \sim b$ נקבל לפי טרנזיטיביות $x \sim b$, כלומר $x \in [b]$; אז $[a] \subseteq [b]$. ההכלה ההפוכה זהה עם החלפת תפקידים ($a \sim b$ נותן $b \sim a$ באותו אופן), ולכן $[a] = [b]$. כל שלוש התכונות של יחס שקילות נדרשות כאן — וזו בדיוק הסיבה שמחלקות שקילות יוצרות חלוקה של $A$.
