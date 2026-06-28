---
id: prf_conditional_probability_formula
claim_id: thm_conditional_probability_formula
method: informal
status: reviewed
dependencies:
- def_probability_measure
- ax_probability_additivity
- ax_probability_total
- def_set_intersection
is_canonical: true
date_added: '2026-06-28T15:49:27.883697Z'
schema_version: 1
---

ניתן להבין את הנוסחה בשני אופנים: (א) כהגדרה מוטיבית של הסתברות מותנית, או (ב) כטענה הניתנת להוכחה אם מקבלים את הפרשנות האינטואיטיבית — 'מצמצמים את מרחב המדגם ל-$B$'. נציג את שתי הזוויות, ונראה שהן עקביות.

**מוטיבציה — צמצום מרחב המדגם.** נתון שאירע המאורע $B$. כעת הניסוי מתבצע כאילו מרחב המדגם הוא $B$ בלבד (כל תוצאה שאינה ב-$B$ נפסלת). המאורע 'התרחש $A$' הופך, בתוך המרחב הזה, ל-'התרחש $A \cap B$' (לפי `def_set_intersection`, אלו התוצאות שהן גם ב-$A$ וגם ב-$B$). לכן ההסתברות החדשה ל-$A$ צריכה להיות פרופורציונלית ל-$P(A \cap B)$.

**דרישת נורמליזציה.** נסמן את ההסתברות המצומצמת ב-$Q(A) := P(A \mid B)$. כדי ש-$Q$ תהיה פונקציית הסתברות לפי `def_probability_measure`, היא חייבת לקיים $Q(B) = 1$ (האירוע הוודאי במרחב המצומצם הוא $B$). אם נציב $Q(A) = c \cdot P(A \cap B)$ עבור קבוע נורמליזציה $c$ כלשהו, אז דרישת $Q(B) = 1$ נותנת
$$1 = Q(B) = c \cdot P(B \cap B) = c \cdot P(B),$$
ומכיוון ש-$P(B) > 0$ ניתן לחלק:
$$c = \frac{1}{P(B)}.$$

לכן
$$P(A \mid B) = Q(A) = c \cdot P(A \cap B) = \frac{P(A \cap B)}{P(B)}.$$

**בדיקת תקינות.** נוודא ש-$Q$ אכן פונקציית הסתברות על המאורעות $A \subseteq \Omega$:
- אי-שליליות: $P(A \cap B) \geq 0$ ו-$P(B) > 0$, אז $Q(A) \geq 0$. 
- נורמליזציה: בהינתן $\Omega$, $Q(\Omega) = P(\Omega \cap B)/P(B) = P(B)/P(B) = 1$ (משתמשים ב-`ax_probability_total` במובן ש-$\Omega \cap B = B$).
- אדיטיביות: אם $A_1, A_2$ זרים אז גם $A_1 \cap B$ ו-$A_2 \cap B$ זרים, ולפי `ax_probability_additivity`:
$$Q(A_1 \cup A_2) = \frac{P((A_1 \cup A_2) \cap B)}{P(B)} = \frac{P((A_1 \cap B) \cup (A_2 \cap B))}{P(B)} = \frac{P(A_1 \cap B) + P(A_2 \cap B)}{P(B)} = Q(A_1) + Q(A_2).$$

אם כך, $Q$ אכן פונקציית הסתברות לגיטימית, והגדרת/נוסחת ההסתברות המותנית $P(A \mid B) = P(A \cap B)/P(B)$ היא הבחירה הטבעית והיחידה המקיימת את התנאי 'בהינתן $B$, $B$ הוא הוודאי'. הדרישה $P(B) > 0$ הכרחית כדי שהחילוק יהיה מוגדר. $\blacksquare$
