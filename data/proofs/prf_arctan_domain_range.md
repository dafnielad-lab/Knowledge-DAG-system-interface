---
id: prf_arctan_domain_range
claim_id: thm_arctan_domain_range
method: informal
status: reviewed
dependencies:
- def_arctan
- def_tan
- def_sin
- def_cos
- def_inverse_function
- def_bijection
- def_increasing_function
- thm_sin_special_values
- thm_cos_special_values
is_canonical: true
date_added: '2026-06-28T20:34:16.547150Z'
schema_version: 1
---

**שלב 1 — $\tan$ מוגדר היטב בתחום $(-\pi/2, \pi/2)$.**

לפי `def_tan`, $\tan\theta = \sin\theta / \cos\theta$ מוגדר כאשר $\cos\theta \neq 0$. עבור $\theta \in (-\pi/2, \pi/2)$ הקואורדינטה $x = \cos\theta$ מקיימת $\cos\theta > 0$ (זהו החצי הימני הפתוח של מעגל היחידה לפי `def_cos`), ובפרט $\cos\theta \neq 0$. לכן $\tan$ מוגדר בכל התחום הפתוח.

**שלב 2 — $\tan$ עולה ממש בתחום $(-\pi/2, \pi/2)$.**

בתחום זה $\cos\theta > 0$. נראה שאם $-\pi/2 < \theta_1 < \theta_2 < \pi/2$, אז $\tan\theta_1 < \tan\theta_2$. נחשב:
$$\tan\theta_2 - \tan\theta_1 = \frac{\sin\theta_2}{\cos\theta_2} - \frac{\sin\theta_1}{\cos\theta_1} = \frac{\sin\theta_2 \cos\theta_1 - \cos\theta_2 \sin\theta_1}{\cos\theta_1 \cos\theta_2} = \frac{\sin(\theta_2 - \theta_1)}{\cos\theta_1 \cos\theta_2}.$$
נציין כי $0 < \theta_2 - \theta_1 < \pi$, ולכן הקואורדינטה $y$ של $\theta_2 - \theta_1$ במעגל היחידה חיובית, כלומר $\sin(\theta_2 - \theta_1) > 0$. מאחר ש-$\cos\theta_1 \cos\theta_2 > 0$, נקבל $\tan\theta_2 - \tan\theta_1 > 0$, כדרוש. לפי `def_increasing_function`, $\tan$ עולה ממש, ובפרט חד-חד-ערכית.

**שלב 3 — $\tan$ על $\mathbb{R}$.**

נראה ש-$\tan\theta \to +\infty$ כאשר $\theta \to (\pi/2)^-$, ו-$\tan\theta \to -\infty$ כאשר $\theta \to (-\pi/2)^+$. מ-`thm_sin_special_values` ו-`thm_cos_special_values`, $\sin(\pi/2) = 1$ ו-$\cos(\pi/2) = 0$. כאשר $\theta \to (\pi/2)^-$, $\sin\theta \to 1$ ו-$\cos\theta \to 0^+$ (כי $\cos$ חיובי בתחום הפתוח). לכן $\tan\theta = \sin\theta/\cos\theta \to +\infty$. בדומה $\tan\theta \to -\infty$ כאשר $\theta \to (-\pi/2)^+$. רציפות $\tan$ (כמנת רציפות) ומשפט ערך הביניים מבטיחים שכל $y \in \mathbb{R}$ מתקבל. לכן $\tan$ על.

**שלב 4 — הגדרת ההופכית.**

משלב 2+3, $\tan$ מצומצמת ל-$(-\pi/2, \pi/2)$ היא בייקציה אל $\mathbb{R}$ (`def_bijection`). לכן לפי `def_inverse_function` קיימת לה ההופכית $\arctan: \mathbb{R} \to (-\pi/2, \pi/2)$ — בהתאם ל-`def_arctan`. האקוויולנציה $\arctan(y) = \theta \iff (\tan\theta = y \wedge \theta \in (-\pi/2, \pi/2))$ היא מאפיין הפונקציה ההפוכה.

**שלב 5 — $\arctan$ עולה ממש ואי-זוגית.**

עלייה ממש: ההופכית של פונקציה עולה ממש היא עולה ממש (כמו בשלב 4 של $\arcsin$).

אי-זוגיות: $\tan$ אי-זוגית — $\tan(-\theta) = \sin(-\theta)/\cos(-\theta) = -\sin\theta/\cos\theta = -\tan\theta$ (לפי הסימטריה של $\sin, \cos$ במעגל היחידה). יהי $y \in \mathbb{R}$ ונסמן $\theta = \arctan(y) \in (-\pi/2, \pi/2)$. אז $-\theta \in (-\pi/2, \pi/2)$ ו-$\tan(-\theta) = -\tan\theta = -y$, ולכן $\arctan(-y) = -\theta = -\arctan(y)$.

**שלב 6 — גבולות באינסוף.**

משלב 3 ראינו שכאשר $\theta \to (\pi/2)^-$ אז $\tan\theta \to +\infty$. שקול: $y = \tan\theta \to +\infty \Rightarrow \theta = \arctan(y) \to (\pi/2)^-$. כלומר $\lim_{y \to +\infty} \arctan(y) = \pi/2$. בדומה, $\lim_{y \to -\infty} \arctan(y) = -\pi/2$. $\blacksquare$
