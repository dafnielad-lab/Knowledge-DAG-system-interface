---
id: prf_pl_nrm_cnf_existence
claim_id: pl_nrm_cnf_existence
method: informal
status: reviewed
dependencies:
- pl_nrm_dnf_existence
- pl_nrm_dnf_def
- pl_nrm_cnf_def
- pl_nrm_literal
- pl_eqv_double_neg
- pl_eqv_demorgan_disj
- pl_eqv_demorgan_conj
- pl_eqv_substitution
- pl_eqv_def
is_canonical: true
date_added: '2026-07-10T20:18:36.362846Z'
schema_version: 1
---

נשתמש בקיום DNF (`pl_nrm_dnf_existence`) עבור השלילה $\neg \varphi$: קיימת נוסחה $\psi$ ב־DNF (`pl_nrm_dnf_def`) כך ש־$\neg \varphi \equiv \psi$, כלומר
$$\psi = \bigvee_{i=1}^{m} \bigwedge_{j=1}^{k_i} \ell_{i,j},$$
כאשר כל $\ell_{i,j}$ ליטרל (`pl_nrm_literal`).

מפעילים שלילה על שני הצדדים ומשתמשים בכפילות השלילה (`pl_eqv_double_neg`) ובכלל החלפת השקילויות (`pl_eqv_substitution`):
$$\varphi \equiv \neg \neg \varphi \equiv \neg \psi.$$

כעת נדחוס את השלילה פנימה. בשלב הראשון מפעילים דה מורגן על הדיסיונקציה החיצונית (`pl_eqv_demorgan_disj`):
$$\neg \psi \equiv \neg \bigvee_{i=1}^{m} \bigwedge_{j=1}^{k_i} \ell_{i,j} \equiv \bigwedge_{i=1}^{m} \neg \bigwedge_{j=1}^{k_i} \ell_{i,j}.$$

בשלב השני מפעילים דה מורגן על כל קוניונקציה פנימית (`pl_eqv_demorgan_conj`):
$$\neg \bigwedge_{j=1}^{k_i} \ell_{i,j} \equiv \bigvee_{j=1}^{k_i} \neg \ell_{i,j}.$$

לבסוף, $\neg \ell_{i,j}$ שקול לליטרל: אם $\ell_{i,j} = p$ אזי $\neg \ell_{i,j} = \neg p$ שכבר ליטרל; אם $\ell_{i,j} = \neg p$ אזי $\neg \ell_{i,j} = \neg \neg p \equiv p$ לפי `pl_eqv_double_neg` — גם זה ליטרל. נסמן ב־$\ell'_{i,j}$ את הליטרל המתאים. באמצעות `pl_eqv_substitution` נקבל
$$\varphi \equiv \bigwedge_{i=1}^{m} \bigvee_{j=1}^{k_i} \ell'_{i,j},$$
וזו נוסחה ב־CNF (`pl_nrm_cnf_def`). לפי טרנזיטיביות של שקילות (`pl_eqv_def`) $\varphi \equiv \varphi'$ עבור $\varphi'$ זו. $\blacksquare$
