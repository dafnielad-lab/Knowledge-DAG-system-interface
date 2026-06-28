---
id: prf_distance_between_parallel_lines_2d
claim_id: thm_distance_between_parallel_lines_2d
method: informal
status: reviewed
dependencies:
- def_line_equation_general_form
- thm_distance_point_to_line_2d
- def_parallel_lines
- thm_parallel_lines_equal_slopes
is_canonical: true
date_added: '2026-06-28T20:34:16.579717Z'
schema_version: 1
---

**הוכחה.** ראשית, שני הישרים אכן מקבילים: לפי `def_line_equation_general_form` שיפועו של ישר $ax+by+c=0$ (כאשר $b \neq 0$) הוא $m = -a/b$, ולכן שני הישרים בעלי שיפוע זהה ולפי `thm_parallel_lines_equal_slopes` הם מקבילים (במקרה $b = 0$ שניהם אנכיים: $x = -c_1/a$ ו-$x = -c_2/a$, ולכן גם כאן מקבילים לפי `def_parallel_lines`).

כעת נחשב את המרחק. נבחר נקודה כלשהי $P_0 = (x_0, y_0)$ על הישר $\ell_1$, כלומר $a x_0 + b y_0 + c_1 = 0$, ומכאן $a x_0 + b y_0 = -c_1$. המרחק בין הישרים המקבילים שווה למרחק מ-$P_0$ אל $\ell_2$ (שכן המרחק נמדד לאורך הנורמל המשותף). לפי `thm_distance_point_to_line_2d`,

$$d(P_0, \ell_2) = \frac{|a x_0 + b y_0 + c_2|}{\sqrt{a^2 + b^2}} = \frac{|-c_1 + c_2|}{\sqrt{a^2 + b^2}} = \frac{|c_2 - c_1|}{\sqrt{a^2 + b^2}} = \frac{|c_1 - c_2|}{\sqrt{a^2 + b^2}}.$$

המרחק אינו תלוי בבחירת $P_0$ על $\ell_1$ (התוצאה תלויה רק במקדמים), ולכן מוגדר היטב כמרחק בין שני הישרים המקבילים. $\blacksquare$
