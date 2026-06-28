---
id: prf_harmonic_addition_form
claim_id: def_harmonic_addition_form
method: informal
status: reviewed
dependencies:
- thm_harmonic_addition
- def_arctan
- def_unit_circle
- def_sin
- def_cos
is_canonical: true
date_added: '2026-06-28T20:34:16.550151Z'
schema_version: 1
---

**הצדקת ההגדרה — קיום ויחידות של $R$ ו-$\varphi$.**

במשפט `thm_harmonic_addition` הוכח שלכל $a, b \in \mathbb{R}$ לא שניהם אפס מתקיים $a \sin x + b \cos x = R \sin(x + \varphi)$ עם $R = \sqrt{a^2 + b^2}$ ו-$\tan\varphi = b/a$ (עם תיקון רביע). הגדרה זו מעניקה משמעות גיאומטרית מדויקת ל-$\varphi$:

**יחידות $R$:** השוואת הביטויים בנקודה שבה $\sin(x + \varphi) = 1$ נותנת $R = \max_x(a \sin x + b \cos x)$, וערך זה חיובי ויחיד. לכן $R = \sqrt{a^2 + b^2}$ הוא היחיד.

**יחידות $\varphi$:** משוואת הזיהוי $a \sin x + b \cos x = R(\cos\varphi \sin x + \sin\varphi \cos x)$ דורשת $\cos\varphi = a/R$ ו-$\sin\varphi = b/R$. הזוג $(a/R, b/R)$ מקיים $(a/R)^2 + (b/R)^2 = 1$, ולכן הוא נקודה על מעגל היחידה (`def_unit_circle`). לפי `def_sin` ו-`def_cos`, כל נקודה על מעגל היחידה מתאימה לזווית יחידה $\varphi \in (-\pi, \pi]$.

**חישוב $\varphi$ דרך $\arctan$:**

*מקרה $a > 0$:* הנקודה $(a/R, b/R)$ נמצאת בחצי הימני של מעגל היחידה ($x$-קואורדינטה חיובית), כלומר $\varphi \in (-\pi/2, \pi/2)$. בתחום זה $\arctan$ נותן ערך יחיד (`def_arctan`), ו-$\varphi = \arctan(b/a)$.

*מקרה $a < 0$, $b \geq 0$:* הנקודה ברביע השני, $\varphi \in (\pi/2, \pi]$, ו-$\varphi = \arctan(b/a) + \pi$.

*מקרה $a < 0$, $b < 0$:* הנקודה ברביע השלישי, $\varphi \in (-\pi, -\pi/2)$, ו-$\varphi = \arctan(b/a) - \pi$.

*מקרה $a = 0$:* אם $b > 0$, $\varphi = \pi/2$; אם $b < 0$, $\varphi = -\pi/2$.

בכל מקרה הזווית $\varphi$ נקבעת יחיד, מה שמצדיק את ההגדרה. $\blacksquare$
