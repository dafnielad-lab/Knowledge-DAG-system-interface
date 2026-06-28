---
id: prf_negative_multiplication_flips_inequality
claim_id: thm_negative_multiplication_flips_inequality
method: informal
status: reviewed
dependencies:
- ax_positive_multiplication_preserves_order
- ax_addition_preserves_order
- ax_additive_inverse
- ax_additive_identity
- ax_addition_commutativity
- ax_addition_associativity
- ax_distributive_law
- thm_multiplication_by_negative_one
- thm_inequality_negation_flips
is_canonical: true
date_added: '2026-06-28T15:49:27.744470Z'
schema_version: 1
---

נתון: $a < b$ ו-$c < 0$.

**שלב 1: $-c > 0$.** מ-$c < 0$ נוסיף $-c$ לשני האגפים לפי אקסיומת שימור הסדר בחיבור $ax\_addition\_preserves\_order$: $c + (-c) < 0 + (-c)$. מאיבר נגדי $ax\_additive\_inverse$ האגף השמאלי הוא $0$, ומאיבר ניטרלי $ax\_additive\_identity$ וקומוטטיביות החיבור $ax\_addition\_commutativity$ האגף הימני הוא $-c$. לכן $0 < -c$, כלומר $-c > 0$.

**שלב 2: $a \cdot (-c) < b \cdot (-c)$.** מההנחה $a < b$ ומשלב 1 $-c > 0$, נפעיל את אקסיומת שימור הסדר בכפל בחיובי $ax\_positive\_multiplication\_preserves\_order$ עם הכופל $-c$, ונקבל $a \cdot (-c) < b \cdot (-c)$.

**שלב 3: זיהוי $a \cdot (-c) = -(a \cdot c)$ ובדומה ל-$b$.** ממשפט הכפל ב-$-1$ $thm\_multiplication\_by\_negative\_one$, $-c = (-1) \cdot c$. לכן $a \cdot (-c) = a \cdot ((-1) \cdot c)$, ובאסוציאטיביות וקומוטטיביות הכפל זה שווה ל-$(-1) \cdot (a \cdot c) = -(a \cdot c)$ (שוב $thm\_multiplication\_by\_negative\_one$). באופן דומה $b \cdot (-c) = -(b \cdot c)$.

לכן שלב 2 הופך ל-$-(a \cdot c) < -(b \cdot c)$.

**שלב 4: היפוך באמצעות נגדי.** ממשפט היפוך אי-שוויון בניוד $thm\_inequality\_negation\_flips$: אם $-(a \cdot c) < -(b \cdot c)$ אז $-(-(b \cdot c)) < -(-(a \cdot c))$, כלומר $b \cdot c < a \cdot c$ (לפי תכונת הנגדי הכפול, $-(-x) = x$, הנובעת מיחידות הנגדי ב-$ax\_additive\_inverse$).

כלומר $a \cdot c > b \cdot c$. $\blacksquare$
