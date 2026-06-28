---
id: prf_elimination_method
claim_id: thm_elimination_method
method: informal
status: reviewed
dependencies:
- def_system_of_linear_equations
- ax_additive_inverse
- ax_additive_identity
- ax_distributive_law
- ax_multiplicative_inverse
is_canonical: true
date_added: '2026-06-28T15:49:27.807705Z'
schema_version: 1
---

נתבונן במערכת לפי def_system_of_linear_equations:
$$\begin{cases} a_1 x + b_1 y = c_1 \quad (E_1) \\ a_2 x + b_2 y = c_2 \quad (E_2) \end{cases}$$
יהי $\lambda \neq 0$ קבוע. נראה שהמערכת שקולה למערכת המתקבלת מהחלפת $(E_2)$ ב-$(E_2') := (E_2) + \lambda \cdot (E_1)$, כלומר:
$$(a_2 + \lambda a_1) x + (b_2 + \lambda b_1) y = c_2 + \lambda c_1.$$

**כיוון א' — כל פתרון מקורי הוא פתרון חדש:** יהי $(x_0, y_0)$ פתרון של המערכת המקורית, אז $(E_1)$ ו-$(E_2)$ מתקיימים בו. נכפול את שני אגפי $(E_1)$ ב-$\lambda$:
$$\lambda (a_1 x_0 + b_1 y_0) = \lambda c_1,$$
ולפי ax_distributive_law: $\lambda a_1 x_0 + \lambda b_1 y_0 = \lambda c_1$. נחבר לשני אגפי $(E_2)$:
$$(a_2 x_0 + b_2 y_0) + (\lambda a_1 x_0 + \lambda b_1 y_0) = c_2 + \lambda c_1,$$
ולפי ax_distributive_law שוב: $(a_2 + \lambda a_1) x_0 + (b_2 + \lambda b_1) y_0 = c_2 + \lambda c_1$. זהו בדיוק $(E_2')$. לכן $(x_0, y_0)$ פותר את $(E_1)$ ו-$(E_2')$.

**כיוון ב' — כל פתרון חדש הוא פתרון מקורי:** יהי $(x_0, y_0)$ פתרון של $(E_1)$ ו-$(E_2')$. אז $(E_1)$ מתקיים. נראה ש-$(E_2)$ מתקיים: כתבנו את $(E_2)$ כ-$(E_2') - \lambda \cdot (E_1)$, כלומר נחסר משני אגפי $(E_2')$ את $\lambda$ כפול אגף $(E_1)$:
$$\left[(a_2 + \lambda a_1) x_0 + (b_2 + \lambda b_1) y_0\right] - \lambda (a_1 x_0 + b_1 y_0) = (c_2 + \lambda c_1) - \lambda c_1.$$
לפי ax_distributive_law האגף השמאלי שווה $a_2 x_0 + b_2 y_0$. לפי ax_additive_inverse ו-ax_additive_identity, $\lambda c_1 - \lambda c_1 = 0$ ולכן האגף הימני שווה $c_2$. נקבל $a_2 x_0 + b_2 y_0 = c_2$ — זהו $(E_2)$.

**ביטול משתנה:** אם נבחר $\lambda = -\frac{a_2}{a_1}$ (כאשר $a_1 \neq 0$, השימוש ב-ax_multiplicative_inverse), אז המקדם של $x$ ב-$(E_2')$ מתאפס: $a_2 + \lambda a_1 = a_2 - a_2 = 0$, וקיבלנו משוואה לינארית במשתנה $y$ בלבד. $\blacksquare$
