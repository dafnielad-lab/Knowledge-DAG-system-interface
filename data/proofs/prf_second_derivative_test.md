---
id: prf_second_derivative_test
claim_id: thm_second_derivative_test
method: informal
status: reviewed
dependencies:
- def_second_derivative
- thm_increasing_test
- thm_decreasing_test
- thm_fermat_extremum
is_canonical: true
date_added: '2026-06-27T20:41:51.335588Z'
schema_version: 1
---

תהי $f$ פונקציה גזירה פעמיים בנקודה פנימית $c$ עם $f'(c) = 0$ (לפי def_second_derivative הנגזרת השנייה מוגדרת היטב בנקודה).

**מקסימום ($f''(c) < 0$):** המשמעות היא שהנגזרת של $f'$ ב-$c$ שלילית, ולכן לפי thm_decreasing_test, המופעל על הפונקציה $f'$ במקום $f$, $f'$ יורדת בסביבת $c$. ביחד עם $f'(c) = 0$ מקבלים $f' > 0$ משמאל ל-$c$ ו-$f' < 0$ מימין לה — כלומר $f$ עולה ואז יורדת, אז $c$ מקסימום מקומי.

**מינימום ($f''(c) > 0$):** סימטרית, לפי thm_increasing_test (מופעל על $f'$) $f'$ עולה בסביבת $c$. אז $f' < 0$ משמאל ל-$c$ ו-$f' > 0$ מימין — $f$ יורדת ואז עולה, אז $c$ מינימום מקומי.

(הקיום של אקסטרמום ב-$c$ עצמו עוקב מ-thm_fermat_extremum.) $\blacksquare$
