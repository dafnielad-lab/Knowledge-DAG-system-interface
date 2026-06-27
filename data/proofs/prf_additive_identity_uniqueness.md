---
id: prf_additive_identity_uniqueness
claim_id: thm_additive_identity_uniqueness
method: informal
status: reviewed
dependencies:
- ax_additive_identity
- ax_addition_commutativity
is_canonical: true
date_added: '2026-06-27T15:32:36.129981Z'
schema_version: 1
---

נניח שגם $0$ וגם $0'$ הם איברים ניטרליים לחיבור: $a + 0 = a$ ו-$a + 0' = a$ לכל $a$.

אז $0 = 0 + 0'$ (לפי הניטרליות של $0'$), ו-$0 + 0' = 0' + 0$ (קומוטטיביות), ו-$0' + 0 = 0'$ (ניטרליות של $0$).

מכאן $0 = 0'$. $\blacksquare$
