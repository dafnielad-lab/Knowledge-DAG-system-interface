---
id: prf_inverse_function_exists
claim_id: thm_inverse_function_exists
method: informal
status: reviewed
dependencies:
- def_function
- def_inverse_function
- def_bijection
- def_increasing_function
is_canonical: true
date_added: '2026-06-27T18:26:22.743198Z'
schema_version: 1
---

($\Leftarrow$) אם $f$ חד-חד-ערכית, נגדיר $f^{-1}(y) := $ ה-$x$ היחיד עם $f(x) = y$ (לכל $y$ בטווח). זו פונקציה תקינה.

($\Rightarrow$) אם $f^{-1}$ קיימת ו-$f(x_1) = f(x_2)$, אז $x_1 = f^{-1}(f(x_1)) = f^{-1}(f(x_2)) = x_2$. 

פונקציה מונוטונית: ערכים שונים → תמונות שונות → חד-חד-ערכית. $\blacksquare$
