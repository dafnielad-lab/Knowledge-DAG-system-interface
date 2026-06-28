---
id: prf_real_numbers
claim_id: def_real_numbers
method: informal
status: reviewed
dependencies:
- ax_completeness_axiom
- ax_order_trichotomy
- ax_addition_preserves_order
- def_rational_numbers
is_canonical: true
date_added: '2026-06-28T15:49:27.738471Z'
schema_version: 1
---

ההגדרה של $\mathbb{R}$ אקסיומטית — אנו מאפיינים את $\mathbb{R}$ על-ידי התכונות שהוא מקיים, ולא בנייה מפורשת. נראה שההגדרה עקבית ושהיא באמת מבדילה את $\mathbb{R}$ מ-$\mathbb{Q}$.

**א. $\mathbb{R}$ הוא שדה סדור.** $\mathbb{R}$ מקיים את אקסיומות החיבור והכפל (שדה), ואת אקסיומות הסדר — בפרט טריכוטומיה (ax_order_trichotomy), המבטיחה שלכל שני ממשיים $a, b$ מתקיים בדיוק אחד מ-$a < b$, $a = b$, $a > b$, ושימור סדר בחיבור (ax_addition_preserves_order). תכונות אלו משותפות גם ל-$\mathbb{Q}$ (def_rational_numbers).

**ב. ההבדל מ-$\mathbb{Q}$ — אקסיומת השלמות.** הרציונליים $\mathbb{Q}$ אינם מקיימים את אקסיומת השלמות (ax_completeness_axiom). דוגמה: הקבוצה $A = \{q \in \mathbb{Q} : q^2 < 2\}$ חסומה מלמעלה ב-$\mathbb{Q}$ (למשל על-ידי $2$), אך אין לה חסם עליון רציונלי — החסם העליון 'הטבעי' הוא $\sqrt{2}$, שאינו רציונלי. ב-$\mathbb{R}$, לעומת זאת, $\sup A = \sqrt{2} \in \mathbb{R}$ קיים.

**ג. אי-רציונליים.** מכאן ש-$\mathbb{R} \setminus \mathbb{Q} \neq \emptyset$ — קיימים מספרים ממשיים שאינם רציונליים, הנקראים **אי-רציונליים**. דוגמאות: $\sqrt{2}, \sqrt{3}, \pi, e, \log_2 3$.

**ד. הצגה גיאומטרית.** קיימת התאמה חד-חד-ערכית ועל בין $\mathbb{R}$ ובין נקודות ציר המספרים. כל נקודה על הציר מתאימה למספר ממשי יחיד, ולהפך — תכונה שאינה מתקיימת ב-$\mathbb{Q}$ (לציר הרציונלי יש 'חורים').

**ה. שילובים בסיסיים.** $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$, כאשר כל הכלה היא ממש. $\mathbb{R}$ סגור תחת חיבור, חיסור, כפל וחילוק (פרט לחילוק ב-0), ומקיים את כל אקסיומות השדה הסדור השלם.
