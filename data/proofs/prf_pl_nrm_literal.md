---
id: prf_pl_nrm_literal
claim_id: pl_nrm_literal
method: informal
status: reviewed
dependencies:
- pl_syn_prop_var
- pl_syn_connectives
- pl_syn_wff
- pl_syn_atomic
is_canonical: true
date_added: '2026-07-10T20:18:36.351346Z'
schema_version: 1
---

הליטרל הוא היחידה הבסיסית שממנה נבנות הצורות הנורמליות. לפי `pl_syn_prop_var`, משתנה פסוקי $p$ הוא סמל אטומי; לפי `pl_syn_atomic`, $p$ עצמו הוא נוסחה. לפי `pl_syn_connectives`, השלילה $\neg$ היא קשר יוני, ולכן $\neg p$ גם היא נוסחה תקינה לפי כללי הבנייה (`pl_syn_wff`). קבוצת הליטרלים היא בדיוק $\{p_1, p_2, \ldots\} \cup \{\neg p_1, \neg p_2, \ldots\}$. כל ליטרל נופל בדיוק לאחת משתי הקטגוריות — חיובי אם אין לפניו סמל $\neg$, ושלילי אם יש. שים לב שנוסחאות מורכבות יותר כמו $\neg \neg p$ או $p \wedge q$ אינן ליטרלים; הליטרל הוא הצורה המינימלית של "טענה עם או בלי שלילה", והוא זה שמופיע בתפקיד הראשי בבניית DNF ו־CNF.
