---
id: prf_polynomial_division_algorithm
claim_id: thm_polynomial_division_algorithm
method: informal
status: reviewed
dependencies:
- def_polynomial
- thm_polynomial_multiplication_degree
is_canonical: true
date_added: '2026-06-27T20:38:28.101554Z'
schema_version: 1
---

**קיום (אינדוקציה על $\deg p$):**

**בסיס:** אם $\deg p < \deg d$, ניקח $q \equiv 0$ ו-$r \equiv p$. אז $p = 0 \cdot d + p$ ו-$\deg r = \deg p < \deg d$.

**צעד:** נניח שהמשפט נכון לכל פולינום מדרגה קטנה מ-$n$, ויהי $\deg p = n \geq \deg d$. נסמן $p(x) = a_n x^n + \ldots$ ו-$d(x) = b_m x^m + \ldots$ עם $b_m \neq 0$. הפולינום $\tilde p(x) := p(x) - \tfrac{a_n}{b_m} x^{n-m} \cdot d(x)$ מבטל את אבר ה-$x^n$, ולכן $\deg \tilde p < n$. לפי הנחת האינדוקציה $\tilde p = \tilde q \cdot d + r$ עם $\deg r < \deg d$, ואז $p = \left(\tfrac{a_n}{b_m} x^{n-m} + \tilde q\right) \cdot d + r$.

**יחידות:** אם $p = q_1 d + r_1 = q_2 d + r_2$, אז $(q_1 - q_2) d = r_2 - r_1$. דרגת אגף שמאל לפחות $\deg d$ (אם $q_1 \neq q_2$), אך דרגת אגף ימין קטנה מ-$\deg d$. סתירה, אלא אם $q_1 = q_2$, וממילא $r_1 = r_2$. $\blacksquare$
