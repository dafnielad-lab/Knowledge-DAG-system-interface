---
id: prf_pythagoras
claim_id: thm_pythagoras
method: informal
status: reviewed
dependencies:
- def_right_triangle
- def_triangle
- thm_triangle_angle_sum
- thm_square_nonnegative
- ax_distributive_law
- thm_right_distributive_law
- ax_addition_commutativity
is_canonical: true
date_added: '2026-06-27T15:58:40.082207Z'
schema_version: 1
---

הוכחה גאומטרית-אלגברית (סידור ריבועים):

ניקח ריבוע עם צלע $a + b$. נסדר בתוכו ארבעה משולשים ישרי-זווית חופפים (ניצבים $a, b$, יתר $c$) כך שיתריהם יוצרים ריבוע פנימי עם צלע $c$.

**חישוב שטח הריבוע הגדול בשתי דרכים:**

1. $(a + b)^2 = a^2 + 2ab + b^2$ (פתיחת בינום).

2. שטח 4 משולשים + ריבוע פנימי = $4 \cdot \frac{ab}{2} + c^2 = 2ab + c^2$.

השוואה: $a^2 + 2ab + b^2 = 2ab + c^2$, ולכן $a^2 + b^2 = c^2$. $\blacksquare$
