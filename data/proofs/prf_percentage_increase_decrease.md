---
id: prf_percentage_increase_decrease
claim_id: thm_percentage_increase_decrease
method: informal
status: reviewed
dependencies:
- def_percentage
- thm_percentage_of_number
- ax_distributive_law
- ax_multiplicative_identity
is_canonical: true
date_added: '2026-06-28T20:34:16.496063Z'
schema_version: 1
---

**הוכחת (1) — עלייה ב-$p\%$:** מ-`def_percentage`, האחוז $p\%$ הוא השבר $\frac{p}{100}$. מ-`thm_percentage_of_number` (חישוב אחוז ממספר), $p\%$ של $a$ הוא $\frac{p}{100} \cdot a$. עלייה ב-$p$ אחוזים פירושה הוספת חלק זה לערך המקורי:
$$a_{\text{עלייה}} = a + \frac{p}{100} \cdot a.$$
נפעיל פירוק לגורם משותף — בדיוק `ax_distributive_law` הפועל אחורה — תוך שימוש ב-`ax_multiplicative_identity` ($a = 1 \cdot a$):
$$a + \frac{p}{100} \cdot a = 1 \cdot a + \frac{p}{100} \cdot a = \left(1 + \frac{p}{100}\right) \cdot a.$$

**הוכחת (2) — הנחה ב-$p\%$:** באופן אנלוגי, הנחה פירושה גריעת $p\%$ מהערך המקורי:
$$a_{\text{הנחה}} = a - \frac{p}{100} \cdot a.$$
כפי שהוסבר, ניתן לרשום $a = 1 \cdot a$ ולהשתמש בחוק הפילוג (`ax_distributive_law`) על חיסור (השווה ל-`ax_distributive_law` יחד עם איבר נגדי):
$$1 \cdot a - \frac{p}{100} \cdot a = \left(1 - \frac{p}{100}\right) \cdot a.$$

**הוכחת (3) — עליות רצופות:** נסמן את הערך לאחר העלייה הראשונה ב-$a_1$ ולאחר השנייה ב-$a_2$. לפי חלק (1):
$$a_1 = a \cdot \left(1 + \frac{p_1}{100}\right).$$
כעת מפעילים את אותו הכלל על $a_1$ עם אחוז $p_2$:
$$a_2 = a_1 \cdot \left(1 + \frac{p_2}{100}\right) = a \cdot \left(1 + \frac{p_1}{100}\right) \cdot \left(1 + \frac{p_2}{100}\right).$$
שימוש באסוציאטיביות הכפל מבטיח שהמכפלה מוגדרת היטב.

**הסבר מדוע $p_1 + p_2$ לא מתאים בדרך כלל:** נפתח את המכפלה:
$$\left(1 + \frac{p_1}{100}\right)\left(1 + \frac{p_2}{100}\right) = 1 + \frac{p_1}{100} + \frac{p_2}{100} + \frac{p_1 \cdot p_2}{100^2}.$$
האיבר $\frac{p_1 \cdot p_2}{10000}$ הוא ה"איבר הצולב" שמראה שסך השינוי הוא $p_1 + p_2 + \frac{p_1 \cdot p_2}{100}$ אחוזים — לא $p_1 + p_2$. דוגמה: עלייה של $50\%$ ואז עוד $50\%$ נותנת $1.5 \cdot 1.5 = 2.25$, כלומר עלייה כוללת של $125\%$, לא $100\%$.

**מקרה פרטי חשוב — עלייה והנחה זהות מבטלות את עצמן? לא!** עלייה ב-$p\%$ ואחריה הנחה ב-$p\%$ נותנת:
$$a \cdot \left(1 + \frac{p}{100}\right) \cdot \left(1 - \frac{p}{100}\right) = a \cdot \left(1 - \frac{p^2}{10000}\right) < a$$
(עבור $p \neq 0$), לפי נוסחת הפרש ריבועים. למשל עלייה של $10\%$ ואחריה הנחה של $10\%$ מחזירה ל-$99\%$ מהערך המקורי, לא ל-$100\%$. $\blacksquare$
