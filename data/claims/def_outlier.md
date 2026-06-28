---
id: def_outlier
kind: definition
status: canonical
course: math_jhs
topic: סטטיסטיקה תיאורית (חטיבה)
date_added: '2026-06-28T20:34:16.517605Z'
schema_version: 1
---

**חריג סטטיסטי (outlier):** ערך בסדרת נתונים שרחוק במידה ניכרת משאר הערכים. ההגדרה המעשית הרווחת ביותר היא **קריטריון טוקי** (Tukey's fences): בהינתן סדרת נתונים, נחשב את הרבעונים $Q_1, Q_3$ ואת הטווח הבין-רבעוני $\text{IQR} = Q_3 - Q_1$. נגדיר:
$$L := Q_1 - 1.5 \cdot \text{IQR}, \qquad U := Q_3 + 1.5 \cdot \text{IQR}.$$
ערך $x$ נחשב **חריג** אם $x < L$ או $x > U$. ערך הוא **חריג קיצוני** אם $x < Q_1 - 3 \cdot \text{IQR}$ או $x > Q_3 + 3 \cdot \text{IQR}$.
