---
id: prf_squares_mod_p
claim_id: thm_squares_mod_p
method: informal
status: reviewed
dependencies:
- def_quadratic_residue
- def_prime
- thm_no_zero_divisors
is_canonical: true
date_added: '2026-06-27T17:22:39.263705Z'
schema_version: 1
---

פונקציית $x \mapsto x^2 \pmod p$ מ-$\{1, \ldots, p-1\}$ אל עצמה. כי $x^2 \equiv y^2 \Leftrightarrow (x-y)(x+y) \equiv 0$ ולכן $x \equiv \pm y$ (לפי אי קיום מחלקי אפס בשדה $\mathbb{Z}_p$).

כל ערך בתמונה מתקבל בדיוק 2 פעמים, ולכן יש $\frac{p-1}{2}$ ערכים שונים בתמונה — אלו הם השאריות הריבועיות. $\blacksquare$
