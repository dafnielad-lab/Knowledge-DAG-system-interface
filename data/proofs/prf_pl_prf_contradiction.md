---
id: prf_pl_prf_contradiction
claim_id: pl_prf_contradiction
method: informal
status: reviewed
dependencies:
- pl_cls_contradiction
- pl_sem_clause_neg
- pl_eqv_excluded_middle
- pl_eqv_double_neg
is_canonical: true
date_added: '2026-07-10T20:18:36.348345Z'
schema_version: 1
---

נצדיק את השיטה. נניח שהצלחנו להראות שמן ההנחה $\neg\varphi$ נובעת נוסחה $\chi$ ששקולה ל־$\bot$, כלומר סתירה במובן של `pl_cls_contradiction`. מאחר שאין השמת אמת שבה $\chi$ מקבל ערך $T$, לא ייתכן שקיימת השמה $v$ שבה $v(\neg\varphi) = T$: אילו הייתה, היינו מקבלים $v(\chi) = T$ בסתירה להיות $\chi$ סתירה. לכן בכל השמה $v(\neg\varphi) = F$, ולפי `pl_sem_clause_neg` הדבר שקול לכך ש־$v(\varphi) = T$ בכל השמה — כלומר $\varphi$ טאוטולוגיה של ההוכחה. ניתן להצדיק את המהלך גם תחבירית: מ־`pl_eqv_excluded_middle` יודעים ש־$\varphi \vee \neg\varphi$ היא טאוטולוגיה, וכיוון שהאפשרות $\neg\varphi$ הובילה לסתירה, נותרת רק האפשרות $\varphi$. לחלופין, הגרירה $\neg\varphi \to \bot$ מקנה את $\neg\neg\varphi$, ולפי `pl_eqv_double_neg` שקילות זו נותנת בדיוק $\varphi$.
