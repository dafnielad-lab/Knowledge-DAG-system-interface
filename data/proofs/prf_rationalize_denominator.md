---
id: prf_rationalize_denominator
claim_id: def_rationalize_denominator
method: informal
status: reviewed
dependencies:
- def_square_root
- def_division
- thm_fraction_equality
- thm_difference_of_squares
- thm_sqrt_of_product
- ax_multiplicative_inverse
is_canonical: true
date_added: '2026-06-28T21:06:29.448177Z'
schema_version: 1
---

זוהי הגדרה אופרטיבית של תהליך חישובי; להלן הצדקה למה ההרחבה אכן מסלקת את השורש ולמה תנאי הצמצום הכרחי.

**מקרה (א):** נניח $b > 0$, ולכן $\sqrt{b} > 0$ (לפי def_square_root, השורש הוא אי-שלילי, ואינו אפס שכן ריבועו $b > 0$). הרחבת השבר ב-$\sqrt{b}$ חוקית מכוח thm_fraction_equality (כפל מונה ומכנה באותו מספר שונה מאפס שומר שוויון):
$\dfrac{a}{\sqrt{b}} = \dfrac{a \cdot \sqrt{b}}{\sqrt{b} \cdot \sqrt{b}}$.
מהגדרת השורש הריבועי, $\sqrt{b} \cdot \sqrt{b} = (\sqrt{b})^2 = b$ (לחילופין נובע מ-thm_sqrt_of_product עם $a = b$). מכאן המכנה הופך ל-$b$, שהוא רציונלי כאשר $b$ רציונלי.

**מקרה (ב):** נניח $b > 0$ ושמתקיים $c^2 - d^2 \cdot b \neq 0$. תנאי זה שקול לכך ששני הביטויים $c + d\sqrt{b}$ ו-$c - d\sqrt{b}$ אינם אפסים: שכן לפי הפרש ריבועים (thm_difference_of_squares),
$(c + d\sqrt{b})(c - d\sqrt{b}) = c^2 - (d\sqrt{b})^2 = c^2 - d^2 \cdot (\sqrt{b})^2 = c^2 - d^2 \cdot b$,
ולכן אם המכפלה אינה אפס, אף גורם אינו אפס. בפרט המכנה $c + d\sqrt{b}$ שונה מאפס (אחרת אין משמעות לשבר המקורי) והצמוד $c - d\sqrt{b}$ גם הוא שונה מאפס (אחרת ההרחבה הייתה מכפילה באפס ומאבדת מידע).

תחת תנאי זה, הרחבת השבר בצמוד $c - d\sqrt{b}$ חוקית מכוח thm_fraction_equality:
$\dfrac{a}{c + d\sqrt{b}} = \dfrac{a \cdot (c - d\sqrt{b})}{(c + d\sqrt{b})(c - d\sqrt{b})} = \dfrac{a \cdot (c - d\sqrt{b})}{c^2 - d^2 \cdot b}$.
המכנה $c^2 - d^2 \cdot b$ חופשי משורש.

**הערה על הצורך בתנאי $c^2 - d^2 \cdot b \neq 0$:** אם $b$ הוא ריבוע שלם (למשל $b = 4$) ו-$c = |d| \cdot \sqrt{b}$ (למשל $c = 2, d = 1, b = 4$), אז $c^2 - d^2 \cdot b = 4 - 4 = 0$, ההרחבה מובילה לחילוק באפס, ותהליך הרציונליזציה כושל. במקרים אלה אין צורך ברציונליזציה — הביטוי $c + d\sqrt{b}$ עצמו רציונלי. תנאי $c^2 - d^2 \cdot b \neq 0$ מתקיים אוטומטית כאשר $\sqrt{b}$ אי-רציונלי (שכן אז $|c| = |d|\sqrt{b}$ אפשרי רק אם $d = 0$, ואז המכנה כבר רציונלי), ולכן ברוב הדוגמאות הלימודיות (למשל $b = 2, 3, 5, 7$) התנאי מתקיים מאליו. $\blacksquare$
