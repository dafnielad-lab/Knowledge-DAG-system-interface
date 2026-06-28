---
id: prf_addition_preserves_order_basic
claim_id: thm_addition_preserves_order_basic
method: informal
status: reviewed
dependencies:
- ax_addition_preserves_order
is_canonical: true
date_added: '2026-06-28T15:49:27.747470Z'
schema_version: 1
---

המשפט הוא ניסוח ישיר של אקסיומת שימור הסדר בחיבור.

נניח את ההנחות: $a, b, c \in \mathbb{R}$ ו-$a < b$.

לפי האקסיומה $ax\_addition\_preserves\_order$ (שימור סדר בחיבור): אם $a < b$, אז $a + c < b + c$ לכל $c \in \mathbb{R}$. ההנחה $a < b$ מתקיימת, ו-$c \in \mathbb{R}$ נתון. לכן המסקנה תופסת ישירות: $a + c < b + c$.

הערה: ניתן לראות את שני הניסוחים (האקסיומה והמשפט) כשקולים תחבירית; ההבחנה היא מתודולוגית בלבד — האקסיומה מבטאת תכונה בסיסית של הסדר על השדה, והמשפט מציג אותה תחת הנושא 'אי-שוויונים' עם כותרת מתאימה לתלמיד.

במערכות אקסיומטיות שמגדירות את הסדר דרך קבוצת חיוביים $P$ עם $a < b \iff b - a \in P$, התכונה הזו נובעת באופן מיידי: $(b + c) - (a + c) = b - a \in P$ (חישוב אלגברי בעזרת אסוציאטיביות, קומוטטיביות ונגדי). אצלנו האקסיומה משמשת כנתון ישיר, וההוכחה היא ציטוט שלה. $\blacksquare$
