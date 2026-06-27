---
id: prf_law_of_tangents
claim_id: thm_law_of_tangents
method: informal
status: reviewed
dependencies:
- thm_law_of_sines
- thm_sin_addition_formula
- thm_sin_subtraction_formula
- thm_sum_to_product_sin
is_canonical: true
date_added: '2026-06-27T18:28:08.122596Z'
schema_version: 1
---

ממשפט הסינוסים $a = 2R \sin A$, $b = 2R \sin B$. אז $\frac{a-b}{a+b} = \frac{\sin A - \sin B}{\sin A + \sin B}$.

לפי נוסחאות סכום-למכפלה: $\sin A - \sin B = 2 \cos\frac{A+B}{2} \sin\frac{A-B}{2}$, $\sin A + \sin B = 2 \sin\frac{A+B}{2} \cos\frac{A-B}{2}$.

חילוק: $\frac{\sin\frac{A-B}{2} / \cos\frac{A-B}{2}}{\sin\frac{A+B}{2} / \cos\frac{A+B}{2}} = \frac{\tan\frac{A-B}{2}}{\tan\frac{A+B}{2}}$. $\blacksquare$
