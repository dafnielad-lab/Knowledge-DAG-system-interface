---
id: thm_laplace_expansion
kind: theorem
status: canonical
course: math_uni_linear_algebra
topic: אלגברה לינארית
date_added: '2026-06-28T15:02:41.570051Z'
schema_version: 1
---

**משפט הפיתוח של לפלס:** תהי $A = (a_{ij})$ מטריצה ריבועית מסדר $n \times n$. לכל שורה $i \in \{1, \dots, n\}$ מתקיים $\det(A) = \sum_{j=1}^{n} (-1)^{i+j} a_{ij} M_{ij}$, וכן לכל עמודה $j$ מתקיים $\det(A) = \sum_{i=1}^{n} (-1)^{i+j} a_{ij} M_{ij}$, כאשר $M_{ij}$ (המינור) הוא הדטרמיננטה של תת-המטריצה מסדר $(n-1) \times (n-1)$ המתקבלת מ-$A$ על-ידי מחיקת השורה ה-$i$ והעמודה ה-$j$. הגודל $C_{ij} := (-1)^{i+j} M_{ij}$ נקרא הקופקטור של $a_{ij}$.
