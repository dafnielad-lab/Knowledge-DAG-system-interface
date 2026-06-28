---
id: prf_contrapositive_equivalence
claim_id: thm_contrapositive_equivalence
method: informal
status: reviewed
dependencies: []
is_canonical: true
date_added: '2026-06-28T20:34:16.440592Z'
schema_version: 1
---

**הוכחה בטבלת אמת.** הגרירה $A \Rightarrow B$ מוגדרת כשקרית רק במקרה אחד: $A$ אמת ו-$B$ שקר; בכל שאר 3 המקרים היא אמת.

| $P$ | $Q$ | $\neg P$ | $\neg Q$ | $P \Rightarrow Q$ | $\neg Q \Rightarrow \neg P$ |
|---|---|---|---|---|---|
| T | T | F | F | T | T |
| T | F | F | T | F | F |
| F | T | T | F | T | T |
| F | F | T | T | T | T |

**בדיקת השורה השנייה** (היחידה שבה הגרירה שקרית): $P$ אמת, $Q$ שקרי, אז $P \Rightarrow Q$ שקר. עבור הניגוד: $\neg Q$ אמת, $\neg P$ שקר, אז $\neg Q \Rightarrow \neg P$ שקר. שני הצדדים שקריים — מסכימים.

**בכל שאר השורות** שני הצדדים אמת. לכן בכל אחד מ-4 המקרים האפשריים, שני הפסוקים חולקים אותו ערך אמת — הם שקולים לוגית.

**מסקנה — השימוש הפרקטי:** אם רוצים להוכיח $P \Rightarrow Q$ (כאשר $\neg Q$ קל יותר להניח מאשר $P$), מותר במקום זה להניח $\neg Q$ ולהוכיח $\neg P$. למשל, להוכיח "אם $n^2$ זוגי אז $n$ זוגי" — מוכיחים שקול-הניגוד: "אם $n$ אי-זוגי אז $n^2$ אי-זוגי" (ישיר וקל). $\blacksquare$
