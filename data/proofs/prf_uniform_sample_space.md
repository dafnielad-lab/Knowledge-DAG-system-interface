---
id: prf_uniform_sample_space
claim_id: def_uniform_sample_space
method: informal
status: reviewed
dependencies:
- def_sample_space
- def_event
- def_probability_measure
- ax_probability_total
- ax_probability_additivity
is_canonical: true
date_added: '2026-06-28T15:49:27.886704Z'
schema_version: 1
---

מדובר בהגדרה של מודל הסתברותי מסוים (מרחב אחיד); יש לוודא שההגדרה עקבית עם אקסיומות ההסתברות ושהנוסחה $P(A) = |A|/|\Omega|$ נובעת ממנה.

**עקביות עם האקסיומות.** נתון $\Omega = \{\omega_1, \ldots, \omega_n\}$ סופי (לפי `def_sample_space`) עם $P(\{\omega_i\}) = 1/n$ לכל $i$. נבדוק את שלוש דרישות `def_probability_measure`:
- אי-שליליות: $1/n > 0$ עבור $n \geq 1$. ✓
- נורמליזציה: כל התוצאות היסודיות $\{\omega_1\}, \ldots, \{\omega_n\}$ זרות בזוגות (כל אחת היא יחידון נפרד), ואיחודן הוא $\Omega$. לפי `ax_probability_additivity` ו-`ax_probability_total`:
$$P(\Omega) = \sum_{i=1}^{n} P(\{\omega_i\}) = \sum_{i=1}^{n} \frac{1}{n} = n \cdot \frac{1}{n} = 1. ✓$$
כלומר, הבחירה $1/n$ היא הבחירה היחידה הסימטרית המתיישבת עם נורמליזציה.
- אדיטיביות: מתקיימת אוטומטית כי כל מאורע מתפרק לאיחוד זר של יחידונים.

**הנוסחה $P(A) = |A|/|\Omega|$.** יהי $A \subseteq \Omega$ מאורע (לפי `def_event`). נסמן $|A| = k$, ונכתוב $A = \{\omega_{i_1}, \omega_{i_2}, \ldots, \omega_{i_k}\}$. אז $A$ הוא איחוד זר של $k$ יחידונים:
$$A = \{\omega_{i_1}\} \cup \{\omega_{i_2}\} \cup \cdots \cup \{\omega_{i_k}\}.$$

לפי `ax_probability_additivity`:
$$P(A) = \sum_{j=1}^{k} P(\{\omega_{i_j}\}) = \sum_{j=1}^{k} \frac{1}{n} = \frac{k}{n} = \frac{|A|}{|\Omega|}.$$

**הפרשנות החינוכית.** מרחב אחיד מתאים לניסויים סימטריים: הטלת מטבע הוגן ($n=2$), הטלת קובייה הוגנת ($n=6$), שליפה אקראית של קלף מחפיסה ($n=52$), בחירת מספר ב-הגרלה. בכל אלו, היעדר עדיפות לתוצאה אחת על אחרת מצדיק את ההנחה הסימטרית $P(\{\omega_i\}) = 1/n$. תחת הנחה זו, חישוב הסתברות מתמצה בספירה: כמה תוצאות 'מצליחות' (גודל $A$) ביחס לכמה תוצאות אפשריות (גודל $\Omega$) — מכאן השימוש הנרחב בקומבינטוריקה בחישובי הסתברות תיכוניים. $\blacksquare$
