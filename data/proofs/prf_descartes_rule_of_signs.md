---
id: prf_descartes_rule_of_signs
claim_id: thm_descartes_rule_of_signs
method: informal
status: reviewed
dependencies:
- def_polynomial
- thm_factor_theorem
- thm_fundamental_theorem_of_algebra
is_canonical: true
date_added: '2026-06-27T18:47:27.564532Z'
schema_version: 1
---

**הוכחה אינדוקטיבית על דרגת הפולינום.** נסמן $V(p)$ מספר שינויי הסימן בסדרת מקדמים של $p$.

**טענת עזר:** אם $r > 0$ שורש של $p$, אז $V(p) = V(q) + (2k + 1)$ עבור $k \geq 0$, כאשר $q(x) = p(x)/(x-r)$.

כלומר חלוקה ב-$(x - r)$ (גורם חיובי) מפחיתה את $V$ במספר אי-זוגי. הוכחה ע״י ניתוח השפעת החלוקה הסינתטית על סימני המקדמים.

**הצעד האינדוקטיבי:** אם $p$ דרגה $n$ עם $k$ שורשים חיוביים, חלוקה ב-$(x - r_1) \cdots (x - r_k)$ מפחיתה את $V$ ב-$k$ ועוד מספר זוגי. הפולינום שנשאר אין לו שורשים חיוביים → $V = 0$.

לכן $V(p) = k + 2m$ עבור $m \geq 0$, או $k = V(p) - 2m$. $\blacksquare$
