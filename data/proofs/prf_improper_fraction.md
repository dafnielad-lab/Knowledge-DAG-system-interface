---
id: prf_improper_fraction
claim_id: def_improper_fraction
method: informal
status: reviewed
dependencies:
- def_fraction
- def_natural_numbers
is_canonical: true
date_added: '2026-06-28T20:34:16.463507Z'
schema_version: 1
---

זוהי הגדרה טרמינולוגית המסווגת שברים חיוביים לפי היחס בין המונה למכנה.

לפי הגדרת שבר (def_fraction), $\frac{a}{b} = a \cdot b^{-1}$ עבור $b \neq 0$. אצלנו $a, b \in \mathbb{N}$ ו-$b > 0$ ולכן $b \neq 0$ והשבר מוגדר היטב.

ההגדרה מסווגת לפי השוואה בין $a$ ל-$b$. השוואה זו אפשרית תמיד עבור מספרים טבעיים (def_natural_numbers) שכן הם מסודרים לינארית, ולכן בדיוק אחת מהאפשרויות הבאות מתקיימת: $a < b$, $a = b$, או $a > b$. במקרה $a < b$ מקבלים שבר ממש; במקרים $a \geq b$ מקבלים שבר לא ממש.

פרשנות: כאשר $a \geq b$ מתקיים $\frac{a}{b} \geq 1$. למשל $\frac{5}{3}$ הוא שבר לא ממש (ערכו $\approx 1.67$), בעוד $\frac{2}{3}$ הוא שבר ממש (ערכו $\approx 0.67$).

כל שבר לא ממש ניתן לכתיבה כמספר מעורב, ולהפך: $\frac{5}{3} = 1\frac{2}{3}$. לחילוף כזה נדרשת חלוקה עם שארית (אלגוריתם החלוקה), נושא הנידון בנפרד. $\blacksquare$
