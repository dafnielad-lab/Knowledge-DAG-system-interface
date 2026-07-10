---
id: prf_fol_existential_commutativity
claim_id: fol_existential_commutativity
method: informal
status: reviewed
dependencies:
- fol_existential_quantifier
- fol_equivalence
is_canonical: true
date_added: '2026-07-10T20:41:42.979245Z'
schema_version: 1
---

יהי $D$ תחום דיון. לפי fol_existential_quantifier מופעל פעמיים, שני הצדדים תלויים באותו תנאי: 'קיים $a \in D$ וקיים $b \in D$ כך ש-$\varphi(a, b) = T$'. תנאי זה הוא סימטרי בסדר של $a$ ו-$b$. לכן ערך הנוסחה בשני הצדדים זהה תחת כל תחום ופרשנות. $\blacksquare$

**הערה חשובה:** החלפת סדר בין כמת כללי לכמת פרטי אינה בהכרח שקולה: $\forall x \, \exists y \, \varphi(x, y)$ שונה בכלל מ-$\exists y \, \forall x \, \varphi(x, y)$. השני חזק יותר (מבטיח אותו $y$ אחיד לכל $x$).
