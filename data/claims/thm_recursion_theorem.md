---
id: thm_recursion_theorem
kind: theorem
status: canonical
course: math_foundations
topic: שיטות הוכחה ולוגיקה
date_added: '2026-06-28T20:34:16.444600Z'
schema_version: 1
---

**משפט הרקורסיה (לסדרות):** תהי $X$ קבוצה לא-ריקה, $a \in X$ נקודה התחלתית, ו-$g: X \to X$ פונקציה כלשהי. אז קיימת **פונקציה יחידה** $f: \mathbb{N} \to X$ המקיימת: $$f(0) = a, \quad f(n+1) = g(f(n)) \quad \text{לכל } n \in \mathbb{N}.$$ זהו ההצדקה הפורמלית לכך שהגדרות רקורסיביות כמו $a_1 = c,\ a_{n+1} = \Phi(a_n)$ אכן מגדירות פונקציה — קיום ויחידות אינם אקסיומה אלא משפט.
