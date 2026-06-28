---
id: prf_division_algorithm
claim_id: thm_division_algorithm
method: informal
status: reviewed
dependencies:
- def_integers
- ax_order_trichotomy
- thm_well_ordering_principle
is_canonical: true
date_added: '2026-06-28T15:07:55.500050Z'
schema_version: 1
---

**קיום:** נסתכל בקבוצה $S = \{a - b \cdot k : k \in \mathbb{Z}, a - b \cdot k \geq 0\}$. $S$ אינה ריקה (לדוגמה, עבור $k = -|a|$). לפי עקרון הסדר הטוב במספרים הטבעיים, ל-$S$ יש איבר מינימלי $r = a - b \cdot q$. ברור $r \geq 0$. אם $r \geq b$ אז $r - b = a - b(q+1) \geq 0$ ב-$S$ וקטן מ-$r$, סתירה. לכן $0 \leq r < b$.

**יחידות:** אם $a = b q_1 + r_1 = b q_2 + r_2$ אז $b(q_1 - q_2) = r_2 - r_1$. אבל $|r_2 - r_1| < b$, אז בהכרח $q_1 = q_2$ ו-$r_1 = r_2$. $\blacksquare$
