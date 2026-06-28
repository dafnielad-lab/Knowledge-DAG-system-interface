---
id: prf_similarity_area_ratio
claim_id: thm_similarity_area_ratio
method: informal
status: reviewed
dependencies:
- thm_similarity_ratio_property
- thm_triangle_area_base_height
- def_similar_triangles
is_canonical: true
date_added: '2026-06-28T15:49:27.866705Z'
schema_version: 1
---

נסמן ב-$h$ את הגובה מהקודקוד $C$ אל הצלע $AB$ במשולש $\triangle ABC$, וב-$h'$ את הגובה המתאים מהקודקוד $C'$ אל הצלע $A'B'$ במשולש $\triangle A'B'C'$.

**שלב 1 — יחס הצלעות.** לפי **thm_similarity_ratio_property**, מאחר שהמשולשים דומים עם יחס $k$, מתקיים $A'B' = k \cdot AB$.

**שלב 2 — יחס הגבהים שווה ליחס הדמיון.** נראה כי גם $h' = k \cdot h$. נסמן ב-$H$ את רגל הגובה מ-$C$ על הישר $AB$, וב-$H'$ את רגל הגובה המתאימה ב-$\triangle A'B'C'$. המשולשים $\triangle ACH$ ו-$\triangle A'C'H'$ מקיימים: זווית $\angle CAH = \angle C'A'H'$ (זוויות מתאימות במשולשים דומים, לפי **def_similar_triangles**), והזווית ב-$H$ וב-$H'$ ישרה ($90°$). שתי זוויות שוות, ולכן המשולשים הקטנים האלה דומים זה לזה (לפי קריטריון AA — מובלע ב-def_similar_triangles). לכן $\frac{h'}{h} = \frac{C'H'}{CH} = \frac{A'C'}{AC} = k$, כאשר השוויון האחרון הוא יחס הדמיון מהמשולשים המקוריים. כלומר $h' = k \cdot h$.

**שלב 3 — חישוב יחס השטחים.** לפי **thm_triangle_area_base_height**, שטח המשולשים הוא:
$$S_{ABC} = \tfrac{1}{2} \cdot AB \cdot h, \qquad S_{A'B'C'} = \tfrac{1}{2} \cdot A'B' \cdot h'.$$

נציב את $A'B' = k \cdot AB$ ואת $h' = k \cdot h$:
$$S_{A'B'C'} = \tfrac{1}{2} \cdot (k \cdot AB) \cdot (k \cdot h) = k^2 \cdot \tfrac{1}{2} \cdot AB \cdot h = k^2 \cdot S_{ABC}.$$

לכן $\frac{S_{A'B'C'}}{S_{ABC}} = k^2$, כנדרש.

**משמעות גיאומטרית:** כאשר מגדילים משולש פי $k$ בכל המידות הליניאריות, שטחו גדל פי $k^2$. למשל, אם יחס הדמיון הוא $3$, יחס השטחים הוא $9$. $\blacksquare$
