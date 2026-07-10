---
id: prf_pl_eqv_substitution
claim_id: pl_eqv_substitution
method: informal
status: reviewed
dependencies:
- pl_eqv_def
- pl_syn_wff
- pl_sem_valuation
- pl_sem_clause_neg
- pl_sem_clause_conj
- pl_sem_clause_disj
- pl_sem_clause_impl
- pl_sem_clause_bicond
is_canonical: true
date_added: '2026-07-10T20:18:36.245348Z'
schema_version: 1
---

תהי $v$ השמה שרירותית. נוכיח באינדוקציה על מבנה $\chi$ (pl_syn_wff) שהחלפת מופע של $\varphi$ ב־$\psi$ אינה משנה את ערכה של $\chi$ תחת $v$.

**בסיס.** אם המופע המוחלף הוא כל $\chi$ עצמה, אזי $\chi = \varphi$ ו־$\chi' = \psi$. מהנחת השקילות pl_eqv_def, $v(\varphi) = v(\psi)$, ולכן $v(\chi) = v(\chi')$.

**צעד.** אם המופע נמצא בתוך תת־נוסחה של $\chi$, אזי $\chi$ נבנתה מתת־נוסחאות באמצעות קשר לוגי.

- אם $\chi = \neg \alpha$ ו־$\alpha'$ מתקבלת מ־$\alpha$ בהחלפת המופע, אז לפי הנחת האינדוקציה $v(\alpha) = v(\alpha')$, ולפי pl_sem_clause_neg מתקיים $v(\neg \alpha) = v(\neg \alpha')$.

- אם $\chi = \alpha \circ \beta$ עבור קשר בינארי $\circ \in \{\wedge, \vee, \rightarrow, \leftrightarrow\}$, המופע המוחלף נמצא באחד הצדדים; נניח ב־$\alpha$ (המקרה השני סימטרי). לפי הנחת האינדוקציה $v(\alpha) = v(\alpha')$, ולפי סמנטיקת הקשר המתאים (pl_sem_clause_conj, pl_sem_clause_disj, pl_sem_clause_impl או pl_sem_clause_bicond) הערך $v(\alpha \circ \beta)$ תלוי רק ב־$v(\alpha)$ וב־$v(\beta)$; לפיכך $v(\alpha \circ \beta) = v(\alpha' \circ \beta)$.

מאחר ש־$v(\chi) = v(\chi')$ עבור כל השמה $v$, מ־pl_eqv_def נובע $\chi \equiv \chi'$.
