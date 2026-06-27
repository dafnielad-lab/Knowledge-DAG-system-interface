---
id: prf_inclusion_exclusion_general
claim_id: thm_inclusion_exclusion_general
method: informal
status: reviewed
dependencies:
- def_proof_by_induction
- thm_inclusion_exclusion_two_sets
is_canonical: true
date_added: '2026-06-27T20:38:28.101554Z'
schema_version: 1
---

**אינדוקציה על $n$.**

**בסיס $n = 2$:** זה בדיוק עקרון ההכלה וההפרדה לשתי קבוצות: $|A_1 \cup A_2| = |A_1| + |A_2| - |A_1 \cap A_2|$.

**צעד $n \to n+1$:** נסמן $B := A_1 \cup \cdots \cup A_n$. מבסיס $n=2$:

$|B \cup A_{n+1}| = |B| + |A_{n+1}| - |B \cap A_{n+1}|$.

לפי הנחת האינדוקציה, $|B|$ נתון בידי הנוסחה ל-$n$ קבוצות. עבור $B \cap A_{n+1} = \bigcup_{i=1}^{n} (A_i \cap A_{n+1})$, גם הוא איחוד של $n$ קבוצות, ולכן ניתן לפיתוח לפי הנחת האינדוקציה (כל איבר $|A_{i_1} \cap \cdots \cap A_{i_k} \cap A_{n+1}|$).

חיבור שני הפיתוחים תוך הקפדה על סימן ה-$(-1)^{k+1}$ נותן בדיוק את הנוסחה ל-$n+1$ קבוצות: כל החיתוכים שאינם כוללים את $A_{n+1}$ מגיעים מ-$|B|$, החיתוכים שכוללים את $A_{n+1}$ מגיעים מ-$-|B \cap A_{n+1}|$ (עם היפוך סימן שתואם את הנוסחה), והאיבר היחיד $|A_{n+1}|$ מתווסף בנפרד. $\blacksquare$
