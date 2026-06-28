---
id: prf_root_simplification
claim_id: thm_root_simplification
method: informal
status: reviewed
dependencies:
- def_nth_root
- thm_power_of_product
- def_natural_power
is_canonical: true
date_added: '2026-06-28T15:49:27.761705Z'
schema_version: 1
---

נשתמש באפיון של $\sqrt[n]{x}$ כמספר $y \geq 0$ היחיד המקיים $y^n = x$ [def_nth_root].

**שלב 1 — אי-שליליות של אגף ימין:** מאחר ש-$a, b \geq 0$, מתקיים על פי הגדרת השורש $\sqrt[n]{a} \geq 0$ ו-$\sqrt[n]{b} \geq 0$ [def_nth_root]. מכפלת שני מספרים אי-שליליים היא אי-שלילית, ולכן:
$$\sqrt[n]{a} \cdot \sqrt[n]{b} \geq 0.$$

**שלב 2 — חישוב החזקה ה-$n$-ית של אגף ימין:** נחשב את $(\sqrt[n]{a} \cdot \sqrt[n]{b})^n$. לפי משפט חזקה של מכפלה [thm_power_of_product] (המתקיים לכל $n \in \mathbb{N}$, ובפרט עבור $n \geq 2$):
$$\left( \sqrt[n]{a} \cdot \sqrt[n]{b} \right)^n = \left( \sqrt[n]{a} \right)^n \cdot \left( \sqrt[n]{b} \right)^n.$$
לפי הגדרת השורש מסדר $n$ [def_nth_root] מתקיים $\left( \sqrt[n]{a} \right)^n = a$ ו-$\left( \sqrt[n]{b} \right)^n = b$. (זוהי ההגדרה הרקורסיבית של חזקה טבעית [def_natural_power] בשילוב עם הגדרת השורש.) לפיכך:
$$\left( \sqrt[n]{a} \cdot \sqrt[n]{b} \right)^n = a \cdot b.$$

**שלב 3 — שימוש ביחידות השורש:** קיבלנו מספר $y := \sqrt[n]{a} \cdot \sqrt[n]{b}$ המקיים שני תנאים:
1. $y \geq 0$ (שלב 1).
2. $y^n = a \cdot b$ (שלב 2).

מאחר ש-$a, b \geq 0$ גם המכפלה $a \cdot b \geq 0$, ולכן $\sqrt[n]{a \cdot b}$ מוגדר היטב לפי [def_nth_root] והוא המספר היחיד $z \geq 0$ המקיים $z^n = a \cdot b$. מיחידות זו נובע $y = \sqrt[n]{a \cdot b}$, כלומר:
$$\sqrt[n]{a} \cdot \sqrt[n]{b} = \sqrt[n]{a \cdot b}. \quad \blacksquare$$
