---
id: prf_pl_eqv_def
claim_id: pl_eqv_def
method: informal
status: reviewed
dependencies:
- pl_syn_wff
- pl_sem_valuation
- pl_sem_clause_bicond
- pl_cls_tautology
is_canonical: true
date_added: '2026-07-10T20:18:36.242346Z'
schema_version: 1
---

זוהי הגדרה. יש להראות ששני הניסוחים אכן מגדירים את אותו יחס וששני הצדדים עקביים.

לפי pl_sem_clause_bicond, עבור השמה $v$ שרירותית מתקיים $v(\varphi \leftrightarrow \psi) = T$ אם ורק אם $v(\varphi) = v(\psi)$.

לפיכך: הביטוי $\varphi \leftrightarrow \psi$ הוא טאוטולוגיה (pl_cls_tautology) אם ורק אם $v(\varphi \leftrightarrow \psi) = T$ לכל השמה $v$, ומהצעד הקודם — אם ורק אם $v(\varphi) = v(\psi)$ לכל $v$, שהיא בדיוק ההגדרה הראשונית.

יחס $\equiv$ הוא יחס שקילות על קבוצת הנוסחאות: **רפלקסיביות** ($v(\varphi) = v(\varphi)$ טריוויאלית), **סימטריות** (מן השוויון $v(\varphi) = v(\psi)$ נובע $v(\psi) = v(\varphi)$), ו**טרנזיטיביות** (אם $v(\varphi) = v(\psi)$ וגם $v(\psi) = v(\chi)$ לכל $v$, אז $v(\varphi) = v(\chi)$ לכל $v$). ההגדרה חלה על כל שתי נוסחאות תקינות מ־pl_syn_wff.
