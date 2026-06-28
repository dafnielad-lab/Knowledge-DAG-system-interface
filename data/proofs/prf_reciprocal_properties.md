---
id: prf_reciprocal_properties
claim_id: thm_reciprocal_properties
method: informal
status: reviewed
dependencies:
- ax_multiplicative_inverse
- ax_multiplication_associativity
- ax_multiplication_commutativity
- ax_multiplicative_identity
- thm_multiplicative_inverse_uniqueness
- thm_product_of_negatives
- thm_negative_times_positive_basic
is_canonical: true
date_added: '2026-06-28T20:34:16.457614Z'
schema_version: 1
---

נשתמש בכך שלפי `thm_multiplicative_inverse_uniqueness` ההפכי הכפלי, אם הוא קיים, יחיד. די אם נראה לכל סעיף שהאיבר המוצע מקיים את משוואת ההפכי, ויחידותו תכריע את השוויון.

**(א) $(a^{-1})^{-1} = a$.** לפי `ax_multiplicative_inverse` ההפכי $a^{-1}$ מקיים $a \cdot a^{-1} = 1$. לפי `ax_multiplication_commutativity` גם $a^{-1} \cdot a = 1$. אך זוהי בדיוק משוואת ההפכי עבור $a^{-1}$ (האיבר שכפול ב-$a^{-1}$ נותן $1$), ולכן לפי יחידות ההפכי (`thm_multiplicative_inverse_uniqueness`)

$$(a^{-1})^{-1} = a.$$

**(ב) $(a \cdot b)^{-1} = a^{-1} \cdot b^{-1}$.** נחשב את המכפלה $(a \cdot b) \cdot (a^{-1} \cdot b^{-1})$ באמצעות `ax_multiplication_associativity` ו-`ax_multiplication_commutativity` כדי לסדר מחדש את הגורמים:

$$(a \cdot b) \cdot (a^{-1} \cdot b^{-1}) = (a \cdot a^{-1}) \cdot (b \cdot b^{-1}) = 1 \cdot 1 = 1,$$

כאשר השוויון האחרון לפי `ax_multiplicative_identity` ו-`ax_multiplicative_inverse`. לכן $a^{-1} \cdot b^{-1}$ הוא הפכי של $a \cdot b$ (שאינו אפס כי שני הגורמים שונים מאפס), ולפי יחידות ההפכי

$$(a \cdot b)^{-1} = a^{-1} \cdot b^{-1}.$$

**(ג) $(-a)^{-1} = -(a^{-1})$.** נחשב את המכפלה $(-a) \cdot (-(a^{-1}))$. לפי `thm_product_of_negatives`,

$$(-a) \cdot (-(a^{-1})) = a \cdot a^{-1} = 1,$$

לפי `ax_multiplicative_inverse`. (לאישוש שהפיתוח אכן מנטרל את שני המינוסים: $(-a) \cdot (-(a^{-1})) = -(a \cdot (-(a^{-1}))) = -(-(a \cdot a^{-1})) = a \cdot a^{-1}$, באמצעות `thm_negative_times_positive_basic` פעמיים.) לכן $-(a^{-1})$ הוא הפכי של $-a$ (שאינו אפס כי $a \neq 0$), ולפי יחידות ההפכי (`thm_multiplicative_inverse_uniqueness`)

$$(-a)^{-1} = -(a^{-1}).$$

$\blacksquare$
