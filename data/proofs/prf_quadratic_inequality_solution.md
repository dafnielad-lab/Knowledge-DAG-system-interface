---
id: prf_quadratic_inequality_solution
claim_id: thm_quadratic_inequality_solution
method: informal
status: reviewed
dependencies:
- def_quadratic_inequality
- def_quadratic_function
- def_discriminant
- thm_quadratic_formula
- thm_discriminant_roots_count
- thm_factoring_quadratic
- thm_quadratic_vertex
- ax_positive_multiplication_preserves_order
- thm_negative_multiplication_flips_inequality
- ax_order_trichotomy
is_canonical: true
date_added: '2026-06-28T15:49:27.857705Z'
schema_version: 1
---

נסמן $f(x) = a x^2 + b x + c$ (def_quadratic_function, def_quadratic_inequality). נוכיח את סימן $f$ בשלושה מקרים לפי סימן הדיסקרימיננטה $\Delta = b^2 - 4ac$ (def_discriminant). מסקנות עבור $\leq, >, <$ נובעות באופן זהה מאי-שוויון על $f(x)$, וטרילמת הסדר (ax_order_trichotomy) קובעת ש-$f(x)$ הוא חיובי, שלילי או אפס.

**מקרה א': $\Delta > 0$.** לפי thm_discriminant_roots_count יש שני שורשים ממשיים שונים, ובלי הגבלת הכלליות $x_1 < x_2$, נתונים על-ידי הנוסחה הריבועית (thm_quadratic_formula). לפי משפט הפירוק לגורמים (thm_factoring_quadratic):
$$f(x) = a (x - x_1)(x - x_2).$$
נבחן את סימן $(x - x_1)(x - x_2)$:
• אם $x < x_1 < x_2$: שני הגורמים שליליים, מכפלתם חיובית.
• אם $x_1 < x < x_2$: $x - x_1 > 0$ ו-$x - x_2 < 0$, מכפלתם שלילית.
• אם $x > x_2 > x_1$: שני הגורמים חיוביים, מכפלתם חיובית.
כאשר $a > 0$: כפל בחיובי שומר על סימן (ax_positive_multiplication_preserves_order), ולכן $f(x) > 0$ עבור $x < x_1$ או $x > x_2$, ו-$f(x) < 0$ עבור $x_1 < x < x_2$. כאשר $a < 0$: כפל בשלילי הופך סימן (thm_negative_multiplication_flips_inequality), ולכן הסימנים מתהפכים. בנקודות $x = x_1, x_2$ מתקיים $f(x) = 0$.

**מקרה ב': $\Delta = 0$.** יש שורש כפול $x_0 = -\tfrac{b}{2a}$ (thm_quadratic_formula). לפי thm_factoring_quadratic: $f(x) = a(x - x_0)^2$. הביטוי $(x - x_0)^2 \geq 0$ תמיד, ושווה ל-$0$ רק ב-$x = x_0$. לכן $f(x)$ בעל סימן $a$ עבור כל $x \neq x_0$, ושווה ל-$0$ ב-$x_0$.

**מקרה ג': $\Delta < 0$.** אין שורשים ממשיים (thm_discriminant_roots_count). ממשפט הקודקוד (thm_quadratic_vertex) נקבל בהשלמת ריבוע: $f(x) = a\!\left(x + \tfrac{b}{2a}\right)^2 + \tfrac{4ac - b^2}{4a} = a\!\left(x + \tfrac{b}{2a}\right)^2 - \tfrac{\Delta}{4a}$. הביטוי בסוגריים בריבוע אינו שלילי, וכן $-\tfrac{\Delta}{4a}$ הוא בעל סימן $a$ (כי $-\Delta > 0$). לכן $\tfrac{f(x)}{a} = \left(x + \tfrac{b}{2a}\right)^2 + \tfrac{-\Delta}{4a^2} > 0$, ומכך $f(x)$ בעל סימן $a$ לכל $x$.

בכל אחד מן המקרים מצאנו במדויק היכן $f(x) > 0$, $f(x) < 0$, $f(x) = 0$, ולכן ניתן לקרוא את פתרון כל אחד מארבעת סוגי אי-השוויון. $\blacksquare$
