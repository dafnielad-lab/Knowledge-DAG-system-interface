---
id: prf_definite_integral_additivity
claim_id: thm_definite_integral_additivity
method: informal
status: reviewed
dependencies:
- def_definite_integral
- def_riemann_sum
- thm_limit_sum
is_canonical: true
date_added: '2026-06-28T15:07:55.573050Z'
schema_version: 1
---

נוכיח ישירות מהגדרת האינטגרל כגבול סכומי רימן, ללא שימוש במשפט היסודי.

תהי $P_1: a = x_0 < x_1 < \cdots < x_n = b$ חלוקה של $[a,b]$ ו-$P_2: b = y_0 < y_1 < \cdots < y_m = c$ חלוקה של $[b,c]$, עם נקודות מדגם $\xi_i \in [x_{i-1}, x_i]$ ו-$\eta_j \in [y_{j-1}, y_j]$. איחוד החלוקות $P := P_1 \cup P_2$ הוא חלוקה של $[a,c]$ (שכן $b$ הוא נקודת קצה משותפת), עם נקודות מדגם $\{\xi_i\} \cup \{\eta_j\}$. סכום רימן עבור $P$ הוא בדיוק

$$S(P) = \sum_{i=1}^n f(\xi_i)(x_i - x_{i-1}) + \sum_{j=1}^m f(\eta_j)(y_j - y_{j-1}) = S(P_1) + S(P_2),$$

שכן הסכימה על איחוד החלוקה מתפצלת לשני הסכומים מעל $[a,b]$ ומעל $[b,c]$ בלי חפיפה (לפי הגדרת סכום רימן).

כעת ניקח גבול כאשר ה-mesh של שתי החלוקות שואף לאפס. אז ה-mesh של $P$ גם שואף לאפס, ולכן לפי הגדרת האינטגרל המסוים:

$$\lim S(P_1) = \int_a^b f \, dx, \quad \lim S(P_2) = \int_b^c f \, dx, \quad \lim S(P) = \int_a^c f \, dx.$$

לפי משפט גבול הסכום, $\lim (S(P_1) + S(P_2)) = \lim S(P_1) + \lim S(P_2)$. משילוב השוויון $S(P) = S(P_1) + S(P_2)$ עם הגבולות לעיל מתקבל

$$\int_a^c f \, dx = \int_a^b f \, dx + \int_b^c f \, dx. \; \blacksquare$$
