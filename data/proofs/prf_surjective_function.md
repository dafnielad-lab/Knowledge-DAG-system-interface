---
id: prf_surjective_function
claim_id: def_surjective_function
method: informal
status: reviewed
dependencies:
- def_function
- def_range
is_canonical: true
date_added: '2026-06-28T21:06:29.412567Z'
schema_version: 1
---

ההגדרה מסתמכת על def_function, שמספקת את המבנה $f: A \to B$ — שם $B$ הוא הקודומיין: היעד הצהוּר של ההתאמה. התנאי 'לכל $b \in B$ קיים $a \in A$ כך ש-$f(a)=b$' הוא צמצום של תכונת הקיום ל-$B$ כולו. השוויון לטווח (תמונה) מתקבל מ-def_range: הטווח מוגדר כ-$\{f(x): x \in A\} \subseteq B$, ולכן הוא שווה ל-$B$ אם ורק אם כל איבר של $B$ מתקבל — שזו בדיוק תכונת ה'על'. הניסוח באמצעות 'קודומיין $B$' מסיר את הסתירה שעלולה להופיע אם משתמשים במילה 'טווח' (שמשמעותה הטכנית היא התמונה, לא $B$).
