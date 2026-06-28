---
id: prf_linearity_of_expectation
claim_id: thm_linearity_of_expectation
method: informal
status: reviewed
dependencies:
- def_expected_value
- def_discrete_random_variable
- def_random_variable
- def_probability_function
- ax_probability_total
- ax_distributive_law
- ax_addition_commutativity
- ax_addition_associativity
is_canonical: true
date_added: '2026-06-28T20:34:16.556654Z'
schema_version: 1
---

**הוכחה.** יהי $\Omega$ מרחב מדגם סופי (או בן-מנייה), ויהיו $X, Y: \Omega \to \mathbb{R}$ משתנים מקריים בדידים (לפי def_random_variable ו-def_discrete_random_variable). נגדיר את המשתנה המקרי החדש $Z := aX + bY$, כלומר לכל $\omega \in \Omega$: $$Z(\omega) = a \cdot X(\omega) + b \cdot Y(\omega).$$ **שלב 1 — ביטוי התוחלת כסכום על נקודות המדגם.** לפי הגדרת התוחלת def_expected_value, עבור משתנה מקרי בדיד $W$ עם ערכים $w_1, w_2, \ldots$ והסתברויות $p_i = P(W = w_i)$, $$E[W] = \sum_i w_i \, P(W = w_i).$$ קיבוץ נקודות המדגם לפי ערכי $W$ נותן ניסוח שקול: $$E[W] = \sum_{\omega \in \Omega} W(\omega) \cdot P(\{\omega\}),$$ שכן $P(W = w_i) = \sum_{\omega : W(\omega) = w_i} P(\{\omega\})$ לפי הגדרת פונקציית ההסתברות def_probability_function ואקסיומת הנורמליזציה ax_probability_total המבטיחה ש-$P$ מוגדרת היטב על תת-קבוצות. **שלב 2 — חישוב $E[Z]$.** נחיל את הניסוח לעיל על $Z = aX + bY$: $$E[Z] = \sum_{\omega \in \Omega} Z(\omega) \cdot P(\{\omega\}) = \sum_{\omega \in \Omega} \bigl(a \cdot X(\omega) + b \cdot Y(\omega)\bigr) \cdot P(\{\omega\}).$$ לפי חוק הפילוג ax_distributive_law (המופעל בכל מחובר בסכום), $$\bigl(a X(\omega) + b Y(\omega)\bigr) P(\{\omega\}) = a \cdot X(\omega) \cdot P(\{\omega\}) + b \cdot Y(\omega) \cdot P(\{\omega\}).$$ **שלב 3 — פיצול הסכום.** לפי חוק החילוף ax_addition_commutativity וחוק הקיבוץ ax_addition_associativity של החיבור, ניתן לפצל סכום סופי (או בן-מנייה מתכנס בהחלט) של שני מחוברים לשני סכומים נפרדים, ולהוציא קבוע מתוך הסכום: $$E[Z] = \sum_{\omega} \bigl(a X(\omega) P(\{\omega\}) + b Y(\omega) P(\{\omega\})\bigr) = a \sum_{\omega} X(\omega) P(\{\omega\}) + b \sum_{\omega} Y(\omega) P(\{\omega\}).$$ **שלב 4 — זיהוי המרכיבים.** בכל אחד משני הסכומים בצד ימין מופיע בדיוק הביטוי לתוחלת לפי def_expected_value: $$\sum_{\omega} X(\omega) P(\{\omega\}) = E[X], \qquad \sum_{\omega} Y(\omega) P(\{\omega\}) = E[Y].$$ לכן $$E[aX + bY] = a \cdot E[X] + b \cdot E[Y].$$ **הערה — אי-תלות אינה נדרשת.** בהוכחה לא השתמשנו בשום שלב בעובדה ש-$X$ ו-$Y$ בלתי-תלויים. הסכימה נעשתה על נקודות $\omega \in \Omega$ עצמן, כך שהזהות תקפה גם כאשר המשתנים תלויים זה בזה לחלוטין. זאת בניגוד ל-$E[XY] = E[X] \cdot E[Y]$ שדורש אי-תלות. **מסקנות מיידיות.** בהצבת $a = b = 1$: $E[X + Y] = E[X] + E[Y]$. בהצבת $b = 0$: $E[aX] = a \cdot E[X]$ (הוצאת קבוע מהתוחלת). בהכללה באינדוקציה: $E\!\left[\sum_{i=1}^n a_i X_i\right] = \sum_{i=1}^n a_i E[X_i]$ לכל קבועים $a_1, \ldots, a_n$. $\blacksquare$
