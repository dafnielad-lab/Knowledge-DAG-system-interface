---
id: prf_rearrangement_inequality
claim_id: thm_rearrangement_inequality
method: informal
status: reviewed
dependencies:
- def_permutation
is_canonical: true
date_added: '2026-06-27T18:48:38.235747Z'
schema_version: 1
---

**הוכחה ע״י החלפה.** נניח $\sigma$ אינו זהות, אז קיימים $i < j$ עם $\sigma(i) > \sigma(j)$. החלפת ערכי $\sigma$ ב-$i, j$ משנה את הסכום ב: $a_i (b_{\sigma(j)} - b_{\sigma(i)}) + a_j (b_{\sigma(i)} - b_{\sigma(j)}) = (a_j - a_i)(b_{\sigma(i)} - b_{\sigma(j)}) \geq 0$.

כלומר ההחלפה לסידור עולה מגדילה (או שומרת) את הסכום. $\blacksquare$
