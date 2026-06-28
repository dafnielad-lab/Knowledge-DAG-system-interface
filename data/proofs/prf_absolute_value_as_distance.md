---
id: prf_absolute_value_as_distance
claim_id: def_absolute_value_as_distance
method: informal
status: reviewed
dependencies:
- def_absolute_value
- def_subtraction
- thm_absolute_value_nonnegative
- thm_absolute_value_zero_iff
is_canonical: true
date_added: '2026-06-28T15:49:27.787705Z'
schema_version: 1
---

זוהי הגדרה גיאומטרית של הערך המוחלט. נראה שההגדרה עקבית עם המשמעות האינטואיטיבית של מרחק, ושהיא מתחייבת מההגדרה האלגברית הקיימת.

לפי **def_absolute_value**, $|x| = x$ כאשר $x \geq 0$, ו-$|x| = -x$ כאשר $x < 0$. לפי **def_subtraction**, $a - b := a + (-b)$.

נדרשות שלוש תכונות יסוד למושג מרחק $d(a,b)$ על הישר:

(1) **אי-שליליות:** $d(a,b) \geq 0$ לכל $a, b$. אכן, לפי **thm_absolute_value_nonnegative** מתקיים $|a - b| \geq 0$ לכל $a, b \in \mathbb{R}$.

(2) **אפסיות בדיוק כשהנקודות זהות:** $d(a,b) = 0$ אם ורק אם $a = b$. לפי **thm_absolute_value_zero_iff**, $|a - b| = 0$ אם ורק אם $a - b = 0$, כלומר $a = b$.

(3) **התאמה עם המקרים הפשוטים:** אם $a \geq b$, אז $a - b \geq 0$, ולפי ההגדרה $|a - b| = a - b$ — בדיוק האורך של הקטע מ-$b$ ל-$a$. אם $a < b$, אז $a - b < 0$, ולפי ההגדרה $|a - b| = -(a - b) = b - a$ — בדיוק האורך של הקטע מ-$a$ ל-$b$.

בכל מקרה, $|a - b|$ נותן את אורך הקטע (אי-שלילי) שבין שתי הנקודות.

המקרה הפרטי: עבור $b = 0$ מקבלים $|a - 0| = |a|$, שהוא המרחק מ-$a$ לראשית. $\blacksquare$
