---
id: prf_orthocenter_vector_identity
claim_id: thm_orthocenter_vector_identity
method: informal
status: reviewed
dependencies:
- def_circumcenter
- def_orthocenter
- def_vector_2d
- def_dot_product
- def_perpendicular_vectors
- def_vector_magnitude
- thm_perpendicular_bisectors_concur
is_canonical: true
date_added: '2026-06-28T15:07:55.425063Z'
schema_version: 1
---

נסמן ב-$R$ את רדיוס המעגל החוסם. לפי [def_circumcenter] $O$ הוא מרכז המעגל החוסם, ולפי [thm_perpendicular_bisectors_concur] $O$ מרוחקת באותה מידה $R$ משלושת הקודקודים. מאחר ש-$O$ הוצב בראשית, וקטור המקום של כל קודקוד הוא הוקטור מ-$O$ אליו, ולכן לפי [def_vector_magnitude]:
$$|\vec{A}|^2 = |\vec{B}|^2 = |\vec{C}|^2 = R^2.$$

נגדיר את הוקטור $\vec{P} := \vec{A} + \vec{B} + \vec{C}$, ונראה כי $P$ מצויה על שלושת הגבהים — ומכאן לפי [def_orthocenter] $P$ זהה לאורתוצנטר.

**הגובה מ-$A$.** הגובה מ-$A$ הוא המאונך מ-$A$ לצלע $BC$. וקטור הצלע הוא $\vec{C} - \vec{B}$ (לפי הגדרת חיסור וקטורים), והוקטור מ-$A$ ל-$P$ הוא
$$\vec{P} - \vec{A} = \vec{B} + \vec{C}.$$
נבדוק אנכיות באמצעות מכפלה סקלרית [def_dot_product]:
$$(\vec{B} + \vec{C}) \cdot (\vec{C} - \vec{B}) = \vec{B}\cdot\vec{C} - \vec{B}\cdot\vec{B} + \vec{C}\cdot\vec{C} - \vec{C}\cdot\vec{B} = |\vec{C}|^2 - |\vec{B}|^2 = R^2 - R^2 = 0,$$
תוך שימוש בקומוטטיביות $\vec{B}\cdot\vec{C} = \vec{C}\cdot\vec{B}$ ובזהות $\vec{X}\cdot\vec{X} = |\vec{X}|^2$ הנובעת מ-[def_vector_magnitude] ו-[def_dot_product]. לפי [def_perpendicular_vectors] נובע ש-$\vec{P} - \vec{A} \perp \vec{C} - \vec{B}$, כלומר $P$ מצויה על הגובה מ-$A$ (בפרט, הקו $AP$ מאונך ל-$BC$). שיקול זה נכון כל עוד $\vec{P} \neq \vec{A}$; במקרה הקצה $\vec{P} = \vec{A}$ מתקיים $\vec{B} + \vec{C} = \vec{0}$, ואז $B, C$ דיאמטרליים ו-$A$ עצמו האורתוצנטר.

**הגובהים מ-$B$ ומ-$C$.** באופן סימטרי לחלוטין:
$$(\vec{P} - \vec{B}) \cdot (\vec{C} - \vec{A}) = (\vec{A}+\vec{C})\cdot(\vec{C}-\vec{A}) = |\vec{C}|^2 - |\vec{A}|^2 = 0,$$
$$(\vec{P} - \vec{C}) \cdot (\vec{B} - \vec{A}) = (\vec{A}+\vec{B})\cdot(\vec{B}-\vec{A}) = |\vec{B}|^2 - |\vec{A}|^2 = 0.$$
לכן $P$ מצויה גם על הגובה מ-$B$ וגם על הגובה מ-$C$.

נקודה זו, שמצויה על שלושת הגבהים, היא לפי [def_orthocenter] האורתוצנטר $H$. לכן
$$\vec{H} = \vec{P} = \vec{A} + \vec{B} + \vec{C}. \qquad \blacksquare$$

הערת אגב: ההוכחה מראה במובלע גם את קיום האורתוצנטר (קוקנקורנטיות הגבהים), שכן הצגנו נקודה מפורשת המצויה על שלושתם.
