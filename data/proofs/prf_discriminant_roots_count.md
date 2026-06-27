---
id: prf_discriminant_roots_count
claim_id: thm_discriminant_roots_count
method: informal
status: reviewed
dependencies:
- thm_quadratic_formula
- def_discriminant
- def_square_root
- ax_order_trichotomy
is_canonical: true
date_added: '2026-06-27T16:03:56.115377Z'
schema_version: 1
---

לפי הנוסחה הריבועית $x = \tfrac{-b \pm \sqrt{\Delta}}{2a}$:

- אם $\Delta > 0$: $\sqrt{\Delta} > 0$, ולכן $+\sqrt{\Delta}$ ו-$-\sqrt{\Delta}$ נותנים שני פתרונות שונים.

- אם $\Delta = 0$: $\sqrt{\Delta} = 0$, ולכן $+0$ ו-$-0$ זה אותו פתרון $x = -\tfrac{b}{2a}$ (פתרון יחיד, נקרא 'כפול').

- אם $\Delta < 0$: השורש $\sqrt{\Delta}$ אינו ממשי, לכן אין פתרון ממשי. $\blacksquare$
