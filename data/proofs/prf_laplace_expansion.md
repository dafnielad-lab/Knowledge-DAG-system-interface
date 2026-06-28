---
id: prf_laplace_expansion
claim_id: thm_laplace_expansion
method: informal
status: reviewed
dependencies:
- def_determinant_2x2
- def_determinant_3x3
- def_matrix
- def_proof_by_induction
- def_permutation
is_canonical: true
date_added: '2026-06-28T15:07:55.461552Z'
schema_version: 1
---

נוכיח את הפיתוח לאורך השורה הראשונה ($i=1$); המקרה הכללי נובע ממנו על-ידי החלפת שורות (כל חילופי שורות סמוכות הופך את סימן הדטרמיננטה, וזאת בדיוק המשמעות של $(-1)^{i+j}$ בנוסחה), והפיתוח לפי עמודה מתקבל מן הפיתוח לפי שורה של המטריצה המשוחלפת $A^{T}$, שכן $\det(A^{T}) = \det(A)$.

**הגדרת בסיס.** מהגדרת הדטרמיננטה דרך תמורות (ראו [def_permutation]) ניתן לרשום $\det(A) = \sum_{\sigma \in S_n} \mathrm{sgn}(\sigma) \prod_{k=1}^{n} a_{k,\sigma(k)}$. עבור $n=2$ הנוסחה נותנת $a_{11}a_{22} - a_{12}a_{21}$, וזה בדיוק הפיתוח של לפלס לאורך השורה הראשונה: $a_{11} \cdot M_{11} - a_{12} \cdot M_{12}$ עם $M_{11}=a_{22}$, $M_{12}=a_{21}$ — בהתאם להגדרה [def_determinant_2x2]. עבור $n=3$ זוהי בדיוק נוסחת סארוס שמופיעה ב-[def_determinant_3x3]: $a(ei-fh) - b(di-fg) + c(dh-eg)$, כלומר $a_{11}M_{11} - a_{12}M_{12} + a_{13}M_{13}$.

**צעד אינדוקציה (לפי [def_proof_by_induction]).** נניח את הנוסחה לכל מטריצה מסדר $(n-1)\times(n-1)$, ונוכיח עבור $A$ מסדר $n \times n$ (ראו [def_matrix] להגדרת המבנה). נחלק את סכום התמורות לפי הערך $j = \sigma(1)$:
$$\det(A) = \sum_{j=1}^{n} \sum_{\substack{\sigma \in S_n \\ \sigma(1)=j}} \mathrm{sgn}(\sigma) \, a_{1j} \prod_{k=2}^{n} a_{k,\sigma(k)}.$$
לכל $j$ קבוע, צמצום $\sigma$ ל-$\{2,\dots,n\}$ נותן ביז'קציה אל $S_{n-1}$ על הקבוצה $\{1,\dots,n\}\setminus\{j\}$. סימן התמורה $\sigma$ שווה ל-$(-1)^{j-1}$ כפול סימן התמורה המצומצמת, כי דרושים בדיוק $j-1$ חילופים סמוכים כדי להעביר את $j$ אל המקום הראשון. לכן הסכום הפנימי שווה ל-$(-1)^{j-1} a_{1j} \cdot \det(\widetilde{A}_{1j})$, כאשר $\widetilde{A}_{1j}$ היא תת-המטריצה המתקבלת ממחיקת שורה $1$ ועמודה $j$, ודטרמיננטתה היא בדיוק המינור $M_{1j}$. מכיוון ש-$(-1)^{j-1} = (-1)^{1+j}$, מקבלים $\det(A) = \sum_{j=1}^{n} (-1)^{1+j} a_{1j} M_{1j}$, כנדרש. $\blacksquare$
