---
id: prf_difference_to_product_sin
claim_id: thm_difference_to_product_sin
method: informal
status: reviewed
dependencies:
- thm_sin_addition_formula
- thm_sin_subtraction_formula
is_canonical: true
date_added: '2026-06-28T15:07:55.444051Z'
schema_version: 1
---

נסמן $\alpha = A + B$, $\beta = A - B$ (כך ש-$A = \frac{\alpha+\beta}{2}$, $B = \frac{\alpha-\beta}{2}$).

לפי נוסחת הסינוס של סכום זוויות (thm_sin_addition_formula):
$\sin(A+B) = \sin A \cos B + \cos A \sin B$.

לפי נוסחת הסינוס של הפרש זוויות (thm_sin_subtraction_formula):
$\sin(A-B) = \sin A \cos B - \cos A \sin B$.

נחסר את הזהות השנייה מן הראשונה:
$\sin(A+B) - \sin(A-B) = (\sin A \cos B + \cos A \sin B) - (\sin A \cos B - \cos A \sin B) = 2 \cos A \sin B$.

בהצבת הסימונים $\alpha = A+B$, $\beta = A-B$, ובהתאם $A = \frac{\alpha+\beta}{2}$ ו-$B = \frac{\alpha-\beta}{2}$, מתקבל:
$\sin\alpha - \sin\beta = 2 \cos\frac{\alpha+\beta}{2} \sin\frac{\alpha-\beta}{2}$.

ההצבה $A = \frac{\alpha+\beta}{2}$, $B = \frac{\alpha-\beta}{2}$ הפיכה לכל זוג $\alpha,\beta$ ממשיים, ולכן הזהות תקפה לכל $\alpha,\beta$. $\blacksquare$
