---
id: prf_vector_angle_formula
claim_id: thm_vector_angle_formula
method: informal
status: reviewed
dependencies:
- def_angle_between_vectors
- def_dot_product
- def_vector_magnitude
- def_vector_2d
is_canonical: true
date_added: '2026-06-28T15:49:27.944194Z'
schema_version: 1
---

הנוסחה נובעת מהצבה ישירה של ההגדרות הקואורדינטיות של מכפלה סקלרית וגודל וקטור בהגדרה הכללית של הזווית בין וקטורים.

**שלב 1 — תזכורת ההגדרה:** לפי def_angle_between_vectors, הזווית $\theta \in [0, \pi]$ בין שני וקטורים שונים מאפס $\vec{u}, \vec{v}$ מוגדרת על ידי $\cos \theta = \frac{\vec{u} \cdot \vec{v}}{|\vec{u}|\,|\vec{v}|}$.

**שלב 2 — חישוב המונה:** הוקטורים $\vec{u}, \vec{v} \in \mathbb{R}^2$ לפי def_vector_2d. לפי def_dot_product במקרה הדו-מימדי: $\vec{u} \cdot \vec{v} = u_1 v_1 + u_2 v_2$.

**שלב 3 — חישוב המכנה:** לפי def_vector_magnitude (גודל וקטור = שורש סכום ריבועי הרכיבים): $|\vec{u}| = \sqrt{u_1^2 + u_2^2}$ ו-$|\vec{v}| = \sqrt{v_1^2 + v_2^2}$. שני הוקטורים שונים מאפס, ולכן גדליהם חיוביים והמכנה $|\vec{u}|\,|\vec{v}| = \sqrt{u_1^2 + u_2^2}\, \sqrt{v_1^2 + v_2^2} > 0$ — אין חלוקה באפס.

**שלב 4 — הצבה:** בהצבת התוצאות מהשלבים הקודמים בנוסחת הזווית: $\cos \theta = \frac{\vec{u} \cdot \vec{v}}{|\vec{u}|\,|\vec{v}|} = \frac{u_1 v_1 + u_2 v_2}{\sqrt{u_1^2 + u_2^2}\, \sqrt{v_1^2 + v_2^2}}$. זוהי בדיוק הנוסחה המבוקשת.

**שלב 5 — חישוב הזווית עצמה:** מכיוון ש-$\cos$ חד-חד-ערכית על $[0, \pi]$, ניתן לבודד $\theta = \arccos\!\left( \frac{u_1 v_1 + u_2 v_2}{\sqrt{u_1^2 + u_2^2}\, \sqrt{v_1^2 + v_2^2}} \right)$. מקרים מיוחדים מאמתים את הנוסחה: וקטורים מאונכים — $u_1 v_1 + u_2 v_2 = 0$, כלומר $\cos \theta = 0$ ולכן $\theta = \pi/2$; וקטורים באותו כיוון בדיוק — $\vec{v} = k \vec{u}$ עם $k > 0$, אז $\cos \theta = \frac{k(u_1^2 + u_2^2)}{(u_1^2 + u_2^2) \cdot k} = 1$ ולכן $\theta = 0$ כצפוי. $\blacksquare$
