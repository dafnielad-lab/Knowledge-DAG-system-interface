---
id: prf_substitution_method
claim_id: thm_substitution_method
method: informal
status: reviewed
dependencies:
- def_system_of_linear_equations
- thm_linear_equation_solution
- ax_additive_inverse
- ax_additive_identity
is_canonical: true
date_added: '2026-06-28T15:49:27.805202Z'
schema_version: 1
---

נתבונן במערכת לפי def_system_of_linear_equations:
$$\begin{cases} a_1 x + b_1 y = c_1 \quad (E_1) \\ a_2 x + b_2 y = c_2 \quad (E_2) \end{cases}$$
נניח $b_1 \neq 0$ כדי לבודד את $y$ מ-$(E_1)$.

**שלב 1 — בידוד $y$:** נחסר $a_1 x$ משני אגפי $(E_1)$. לפי ax_additive_inverse ו-ax_additive_identity, $a_1 x + (-a_1 x) = 0$, ולכן $b_1 y = c_1 - a_1 x$. כעת לפי thm_linear_equation_solution (בהחלפת תפקיד המשתנה), נחלק ב-$b_1 \neq 0$ ונקבל:
$$y = \frac{c_1 - a_1 x}{b_1} =: f(x).$$

**שלב 2 — שקילות הכיוון הראשון:** יהי $(x_0, y_0)$ פתרון של המערכת המקורית. אז $(E_1)$ מתקיים, ולכן בהכרח $y_0 = f(x_0)$ (מהשלב 1, $f$ נגזרת חד-חד-ערכית מ-$(E_1)$). הצבה ב-$(E_2)$ נותנת:
$$a_2 x_0 + b_2 \cdot f(x_0) = c_2,$$
כלומר $x_0$ פותר את המשוואה המצומצמת.

**שלב 3 — שקילות הכיוון ההפוך:** יהי $x_0$ פתרון של המשוואה המצומצמת $a_2 x + b_2 \cdot f(x) = c_2$. נגדיר $y_0 := f(x_0)$. אז:
- מהגדרת $f$, מתקיים $b_1 y_0 = c_1 - a_1 x_0$, כלומר $a_1 x_0 + b_1 y_0 = c_1$ — זהו $(E_1)$.
- מהיות $x_0$ פתרון, מתקיים $a_2 x_0 + b_2 y_0 = c_2$ — זהו $(E_2)$.

לכן $(x_0, y_0)$ פותר את המערכת המקורית.

**מסקנה:** קבוצת הפתרונות של המערכת המקורית היא בדיוק $\{(x, f(x)) : x \text{ פותר את המשוואה המצומצמת}\}$, וכך הוכחה שקילות שתי המערכות. $\blacksquare$
