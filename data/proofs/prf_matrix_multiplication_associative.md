---
id: prf_matrix_multiplication_associative
claim_id: thm_matrix_multiplication_associative
method: informal
status: reviewed
dependencies:
- def_matrix_multiplication
- ax_addition_associativity
- ax_multiplication_associativity
is_canonical: true
date_added: '2026-06-27T17:22:39.263705Z'
schema_version: 1
---

$((AB)C)_{ij} = \sum_l (AB)_{il} c_{lj} = \sum_l \left(\sum_k a_{ik} b_{kl}\right) c_{lj} = \sum_{k, l} a_{ik} b_{kl} c_{lj}$.

$(A(BC))_{ij} = \sum_k a_{ik} (BC)_{kj} = \sum_k a_{ik} \sum_l b_{kl} c_{lj} = \sum_{k, l} a_{ik} b_{kl} c_{lj}$.

שני האגפים שווים (החלפת סדר סכימה). $\blacksquare$
