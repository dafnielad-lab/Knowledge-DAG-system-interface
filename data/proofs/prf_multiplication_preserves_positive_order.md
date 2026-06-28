---
id: prf_multiplication_preserves_positive_order
claim_id: thm_multiplication_preserves_positive_order
method: informal
status: reviewed
dependencies:
- ax_positive_multiplication_preserves_order
is_canonical: true
date_added: '2026-06-28T15:49:27.741471Z'
schema_version: 1
---

המשפט הוא בדיוק הניסוח של אקסיומת שימור הסדר בכפל בחיובי. נראה זאת בפירוט:

נניח את שלוש ההנחות: $a, b, c \in \mathbb{R}$, $c > 0$, ו-$a < b$.

לפי האקסיומה $ax\_positive\_multiplication\_preserves\_order$ (שימור סדר בכפל בחיובי), נתון לנו במפורש: אם $a < b$ ו-$c > 0$, אז $a \cdot c < b \cdot c$.

ההנחות שלנו תואמות בדיוק את הנחות האקסיומה: $a < b$ מתקיים (הנחה שנייה), $c > 0$ מתקיים (הנחה ראשונה). לכן מסקנת האקסיומה תופסת ישירות, ואנו מקבלים $a \cdot c < b \cdot c$.

הערה על המעמד התיאורטי: בחלק מהמערכות האקסיומטיות לסדר על שדה ממשי, התכונה הזו נלקחת כאקסיומה (כפי שעשינו כאן). במערכות אחרות מגדירים את החיוביות $P \subseteq \mathbb{R}$ כקבוצה הסגורה לחיבור וכפל, ואז מקבלים את התכונה הזו ממשפט: אם $a < b$ אז $b - a \in P$; ואם גם $c \in P$ (כי $c > 0$ פירושו $c \in P$), אז $(b-a) \cdot c \in P$ (סגירות $P$ לכפל), ומחוק הפילוג $b \cdot c - a \cdot c \in P$, כלומר $a \cdot c < b \cdot c$.

במערכת שלנו האקסיומה נלקחה כנתון בסיסי, ולכן המשפט הוא אכן ציטוט ישיר של האקסיומה. $\blacksquare$
