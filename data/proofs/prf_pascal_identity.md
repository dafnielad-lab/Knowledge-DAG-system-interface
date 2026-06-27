---
id: prf_pascal_identity
claim_id: thm_pascal_identity
method: informal
status: reviewed
dependencies:
- thm_combinations_formula
is_canonical: true
date_added: '2026-06-27T16:13:44.126814Z'
schema_version: 1
---

**הוכחה אלגברית:** $\binom{n-1}{k-1} + \binom{n-1}{k} = \frac{(n-1)!}{(k-1)!(n-k)!} + \frac{(n-1)!}{k!(n-1-k)!} = \frac{(n-1)! \cdot k + (n-1)! \cdot (n-k)}{k!(n-k)!} = \frac{(n-1)! \cdot n}{k!(n-k)!} = \binom{n}{k}$.

**הוכחה קומבינטורית:** מתוך $n$ איברים, נקבע איבר אחד. בחירה של $k$ איברים מפצלת לפי האם אותו איבר נכלל ($\binom{n-1}{k-1}$) או לא ($\binom{n-1}{k}$). $\blacksquare$
