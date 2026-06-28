---
id: prf_inverse_via_adjugate
claim_id: thm_inverse_via_adjugate
method: informal
status: reviewed
dependencies:
- def_invertible_matrix
- def_matrix_multiplication
- def_identity_matrix
- def_matrix_transpose
- def_determinant_3x3
is_canonical: true
date_added: '2026-06-28T15:07:55.464551Z'
schema_version: 1
---

נסמן $B := \operatorname{adj}(A)$, כלומר $b_{ij} = C_{ji} = (-1)^{i+j} \det(M_{ji})$ (לפי `def_matrix_transpose`, השחלוף הופך אינדקסים). נוכיח כי $A \cdot B = \det(A) \cdot I$; ואז מחלוקה ב-$\det(A) \neq 0$ והגדרת ההפיכות (`def_invertible_matrix`) ינבעו ש-$\frac{1}{\det(A)} B = A^{-1}$.

**חישוב הכניסה $(i,k)$ של $AB$.** לפי הגדרת כפל מטריצות (`def_matrix_multiplication`):
$$(AB)_{ik} = \sum_{j=1}^{n} a_{ij} \, b_{jk} = \sum_{j=1}^{n} a_{ij} \, (-1)^{k+j} \det(M_{kj}).$$

**מקרה $i = k$ (אלכסון).** הביטוי $\sum_{j} a_{ij} (-1)^{i+j} \det(M_{ij})$ הוא בדיוק פיתוח לפלס של $\det(A)$ לפי שורה $i$. עבור $n=3$ זהו פיתוח השורה הראשונה כפי שמופיע במפורש ב-`def_determinant_3x3` (הכלל $a(ei-fh) - b(di-fg) + c(dh-eg)$ הוא $\sum_j a_{1j}(-1)^{1+j}\det(M_{1j})$); באופן כללי לכל $n$ זוהי ההגדרה הרקורסיבית של הדטרמיננטה. לכן $(AB)_{ii} = \det(A)$.

**מקרה $i \neq k$ (מחוץ לאלכסון).** הסכום $\sum_{j} a_{ij} (-1)^{k+j} \det(M_{kj})$ הוא פיתוח לפלס לפי שורה $k$ של מטריצה $A'$ המתקבלת מ-$A$ על ידי החלפת שורה $k$ בשורה $i$ (כי הקופקטורים $\det(M_{kj})$ לא תלויים בשורה $k$ עצמה, אלא רק במחיקתה). אך ב-$A'$ שורה $i$ ושורה $k$ זהות, ולכן $\det(A') = 0$ (לכל $n \geq 2$ מתחלף סימן הדטרמיננטה כשמחליפים שתי שורות, ולכן דטרמיננטה עם שתי שורות שוות מתאפסת). לכן $(AB)_{ik} = 0$ עבור $i \neq k$.

**סיכום.** קיבלנו $(AB)_{ik} = \det(A) \cdot \delta_{ik}$, כלומר $AB = \det(A) \cdot I$ ($I$ לפי `def_identity_matrix`). מאחר ש-$\det(A) \neq 0$, חלוקה נותנת $A \cdot \left(\frac{1}{\det(A)} B\right) = I$. חישוב סימטרי לחלוטין על $BA$ (פיתוח לפי עמודה במקום שורה) נותן $\left(\frac{1}{\det(A)} B\right) \cdot A = I$. לפי `def_invertible_matrix` זוהי בדיוק ההגדרה של $A^{-1}$, ולכן $A^{-1} = \frac{1}{\det(A)} \operatorname{adj}(A)$. $\blacksquare$
