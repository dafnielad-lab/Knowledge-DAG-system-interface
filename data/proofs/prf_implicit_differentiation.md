---
id: prf_implicit_differentiation
claim_id: thm_implicit_differentiation
method: informal
status: reviewed
dependencies:
- thm_derivative_chain
is_canonical: true
date_added: '2026-06-27T17:14:35.075131Z'
schema_version: 1
---

אם $F(x, y(x)) = 0$ ו-$y$ גזירה, נגזור את שני האגפים לפי $x$:

$\frac{\partial F}{\partial x} + \frac{\partial F}{\partial y} \cdot y' = 0$ (כלל השרשרת).

פתרון: $y' = -\frac{\partial F / \partial x}{\partial F / \partial y}$ (כאשר המכנה לא אפס). $\blacksquare$
