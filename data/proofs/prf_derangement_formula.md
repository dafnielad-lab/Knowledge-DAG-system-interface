---
id: prf_derangement_formula
claim_id: thm_derangement_formula
method: informal
status: reviewed
dependencies:
- def_derangement
- thm_inclusion_exclusion_general
- thm_maclaurin_exp
is_canonical: true
date_added: '2026-06-27T20:41:51.335588Z'
schema_version: 1
---

תהי $A_i$ קבוצת התמורות $\pi$ המקיימות $\pi(i) = i$ (כלומר $i$ נשאר במקומו). תמורה $\pi$ היא דה-רנג'מנט אם ורק אם $\pi \notin \bigcup_{i=1}^{n} A_i$, אז $!n = n! - \left|\bigcup_{i=1}^{n} A_i\right|$.

**הכלה-הפרדה כללי:** $\left|\bigcup_{i=1}^{n} A_i\right| = \sum_{k=1}^{n} (-1)^{k+1} \sum_{|I|=k} \left|\bigcap_{i \in I} A_i\right|$.

**חישוב כל חיתוך:** $\left|\bigcap_{i \in I} A_i\right| = (n - k)!$ — מספר התמורות שמותירות את כל ה-$k$ אינדקסים שבקבוצה $I$ במקומם (השאר חופשי). מספר תת-קבוצות בגודל $k$ הוא $\binom{n}{k}$.

אז $\left|\bigcup A_i\right| = \sum_{k=1}^{n} (-1)^{k+1} \binom{n}{k} (n-k)! = \sum_{k=1}^{n} (-1)^{k+1} \tfrac{n!}{k!}$.

ולכן $!n = n! - \sum_{k=1}^{n} (-1)^{k+1} \tfrac{n!}{k!} = n! \sum_{k=0}^{n} \tfrac{(-1)^k}{k!}$.

**גבול:** הסדרה הפנימית היא סדרת מקלורן של $e^{-1}$, ולכן $\lim_{n \to \infty} \tfrac{!n}{n!} = e^{-1}$, כלומר $!n \approx \tfrac{n!}{e}$. $\blacksquare$
