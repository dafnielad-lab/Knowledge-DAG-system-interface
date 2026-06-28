---
id: prf_perpendicular_bisector_characterization
claim_id: thm_perpendicular_bisector_characterization
method: informal
status: reviewed
dependencies:
- ax_sas_congruence
- ax_sss_congruence
- def_congruent_triangles
is_canonical: true
date_added: '2026-06-28T15:49:27.869704Z'
schema_version: 1
---

נסמן ב-$M$ את אמצע הקטע $AB$, וב-$\ell$ את האנך האמצעי — הישר העובר דרך $M$ ניצב ל-$AB$. הטענה דו-כיוונית, ונוכיח כל כיוון בנפרד.

**כיוון ראשון: אם $P \in \ell$, אז $|PA| = |PB|$.**

תהי $P$ נקודה כלשהי על האנך האמצעי $\ell$. אם $P = M$, אז $|PA| = |MA| = |MB| = |PB|$ באופן ישיר מהגדרת אמצע הקטע. נניח אם כן $P \neq M$ ונבחן את המשולשים $\triangle PMA$ ו-$\triangle PMB$:

- $|MA| = |MB|$ — שני הקטעים שווים כי $M$ אמצע $AB$.
- $\angle PMA = \angle PMB = 90°$ — שתי הזוויות ישרות כי $\ell$ ניצב ל-$AB$.
- $|PM| = |PM|$ — צלע משותפת.

לפי **ax_sas_congruence** (שתי צלעות והזווית הכלואה ביניהן), $\triangle PMA \cong \triangle PMB$. לפי **def_congruent_triangles**, צלעות מתאימות במשולשים חופפים שוות, ולכן $|PA| = |PB|$.

**כיוון שני: אם $|PA| = |PB|$, אז $P \in \ell$.**

תהי $P$ נקודה כלשהי המקיימת $|PA| = |PB|$. שוב נסתכל על המשולשים $\triangle PMA$ ו-$\triangle PMB$:

- $|PA| = |PB|$ — הנתון.
- $|MA| = |MB|$ — $M$ אמצע $AB$.
- $|PM| = |PM|$ — צלע משותפת.

לפי **ax_sss_congruence** (שלוש צלעות), $\triangle PMA \cong \triangle PMB$. שוב לפי **def_congruent_triangles**, זוויות מתאימות שוות: $\angle PMA = \angle PMB$. אך שתי הזוויות הללו צמודות ויחד יוצרות זווית שטוחה $180°$ (כי $A$, $M$, $B$ על אותו ישר), לכן כל אחת מהן שווה ל-$90°$. הישר $PM$ ניצב ל-$AB$ ועובר דרך $M$ — כלומר $P$ נמצא על האנך האמצעי $\ell$.

שני הכיוונים ביחד נותנים את האפיון המלא: $P \in \ell \iff |PA| = |PB|$.

תוצאה זו היא יסוד גיאומטרי חשוב, ובאמצעותה מוכיחים שאנכי אמצע במשולש נחתכים ב-מרכז המעגל החוסם, וגם משמשת בפתרון בעיות בנייה ואופטימיזציה. $\blacksquare$
