---
id: prf_negation_of_quantifiers
claim_id: thm_negation_of_quantifiers
method: informal
status: reviewed
dependencies:
- def_universal_quantifier
- def_existential_quantifier
is_canonical: true
date_added: '2026-06-28T20:34:16.434089Z'
schema_version: 1
---

נוכיח את שתי השקילויות מהגדרת כל כמת (def_universal_quantifier, def_existential_quantifier).

**שקילות א'** — $\neg (\forall x \in A,\ P(x)) \iff \exists x \in A,\ \neg P(x)$:

לפי def_universal_quantifier, $\forall x \in A,\ P(x)$ הוא אמת בדיוק כאשר $P(x)$ מתקיים לכל $x \in A$. השלילה — $\neg (\forall x \in A,\ P(x))$ — אמת בדיוק כאשר $P(x)$ **לא** מתקיים לכל $x \in A$, כלומר: יש לפחות $x \in A$ אחד שעבורו $P(x)$ שקרי, כלומר $\neg P(x)$ אמת. לפי def_existential_quantifier, זה בדיוק $\exists x \in A,\ \neg P(x)$.

**שקילות ב'** — $\neg (\exists x \in A,\ P(x)) \iff \forall x \in A,\ \neg P(x)$:

לפי def_existential_quantifier, $\exists x \in A,\ P(x)$ אמת בדיוק כאשר קיים לפחות $x$ אחד עם $P(x)$ אמת. השלילה אמת בדיוק כאשר **אין** אף $x \in A$ עם $P(x)$ אמת, כלומר לכל $x \in A$ הביטוי $P(x)$ שקרי, כלומר $\neg P(x)$ אמת לכל $x$. לפי def_universal_quantifier, זה $\forall x \in A,\ \neg P(x)$.

**הערה — כמתים מקוננים:** הכלל מורחב לכמתים שרשרתיים על-ידי הפעלה חוזרת:
$$\neg (\forall x\, \exists y\, P(x,y)) \iff \exists x\, \forall y\, \neg P(x,y).$$
כל $\forall$ הופך ל-$\exists$, כל $\exists$ הופך ל-$\forall$, והכי פנימי הופך מ-$P$ ל-$\neg P$. $\blacksquare$
