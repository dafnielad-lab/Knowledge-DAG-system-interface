---
id: prf_pl_sem_truth_table
claim_id: pl_sem_truth_table
method: informal
status: reviewed
dependencies:
- pl_sem_valuation
- pl_syn_wff
- pl_syn_prop_var
- pl_sem_clause_neg
- pl_sem_clause_conj
- pl_sem_clause_disj
- pl_sem_clause_impl
- pl_sem_clause_bicond
is_canonical: true
date_added: '2026-07-10T20:18:36.210845Z'
schema_version: 1
---

הבניית טבלת האמת מתבצעת בשני שלבים אלגוריתמיים. **שלב א' — יצירת ההשמות:** בהינתן $n$ משתנים פסוקיים $p_1, \ldots, p_n$ (`pl_syn_prop_var`), נבנות כל $2^n$ ההשמות האפשריות שלהם. לכל משתנה שתי אפשרויות ($T$ או $F$), והבחירות בלתי־תלויות; לכן לפי כלל המכפלה מספר ההשמות הכולל הוא $2 \cdot 2 \cdots 2 = 2^n$. סידור מקובל: ההשמות רשומות בסדר בינארי מ־$0$ עד $2^n - 1$. **שלב ב' — חישוב ערך הנוסחה:** לכל השמה $v$, מחשבים את ערך $v(\varphi)$ על־ידי הפעלה חוזרת של חמשת כללי הסמנטיקה: `pl_sem_clause_neg` עבור $\neg$, `pl_sem_clause_conj` עבור $\wedge$, `pl_sem_clause_disj` עבור $\vee$, `pl_sem_clause_impl` עבור $\to$, ו־`pl_sem_clause_bicond` עבור $\leftrightarrow$. החישוב מתבצע רקורסיבית לפי מבנה הפירוק של $\varphi$ לתת־נוסחאות. השלב מסתיים בצעדים סופיים משום שכל נוסחה תקינה (`pl_syn_wff`) בנויה במספר סופי של יישומי קשרים, וההרחבה של $v$ לכל הנוסחה מובטחת יחידה על־פי `pl_sem_valuation`. **חשיבות הכלי:** טבלת האמת היא הכלי המעשי המרכזי בלוגיקה הפסוקית — היא מזהה טאוטולוגיות, סתירות ושקילויות באופן אלגוריתמי (סופי, אך בזמן אקספוננציאלי במספר המשתנים).
