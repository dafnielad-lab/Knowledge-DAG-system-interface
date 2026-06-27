---
id: prf_determinant_product
claim_id: thm_determinant_product
method: informal
status: reviewed
dependencies:
- def_determinant_2x2
- def_matrix_multiplication
is_canonical: true
date_added: '2026-06-27T17:22:39.263705Z'
schema_version: 1
---

**הוכחה ל-$2 \times 2$ (ישירה):** אם $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, $B = \begin{pmatrix} e & f \\ g & h \end{pmatrix}$, אז $AB = \begin{pmatrix} ae+bg & af+bh \\ ce+dg & cf+dh \end{pmatrix}$.

$\det(AB) = (ae+bg)(cf+dh) - (af+bh)(ce+dg) = (ad - bc)(eh - fg) = \det(A)\det(B)$ (פתיחה וצמצום). הכללה ל-$n \times n$ דורשת רב-לינאריות הדטרמיננטה. $\blacksquare$
