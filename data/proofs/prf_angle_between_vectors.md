---
id: prf_angle_between_vectors
claim_id: def_angle_between_vectors
method: informal
status: reviewed
dependencies:
- def_dot_product
- def_vector_magnitude
- thm_law_of_cosines
is_canonical: true
date_added: '2026-06-28T15:49:27.941202Z'
schema_version: 1
---

הגדרת הזווית באמצעות המכפלה הסקלרית אינה הגדרה שרירותית — היא נובעת ישירות ממשפט הקוסינוסים שמיושם על המשולש שנפרש על-ידי שני הוקטורים. נראה זאת.

**שלב 1 — בניית משולש:** ניקח שני וקטורים $\vec{u}, \vec{v}$ הנפרשים מאותה ראשית $O$. סופי הוקטורים הם נקודות $A$ ו-$B$. המשולש $OAB$ בעל צלעות שאורכיהן $|OA| = |\vec{u}|$, $|OB| = |\vec{v}|$ (לפי def_vector_magnitude), ו-$|AB| = |\vec{v} - \vec{u}|$. נסמן ב-$\theta$ את הזווית הגיאומטרית ב-$O$ בין הוקטורים.

**שלב 2 — שימוש במשפט הקוסינוסים:** לפי thm_law_of_cosines במשולש $OAB$: $|AB|^2 = |OA|^2 + |OB|^2 - 2|OA|\,|OB| \cos \theta$, כלומר $|\vec{v} - \vec{u}|^2 = |\vec{u}|^2 + |\vec{v}|^2 - 2 |\vec{u}|\,|\vec{v}| \cos \theta$.

**שלב 3 — פתיחת האגף השמאלי:** לפי def_dot_product ו-def_vector_magnitude (שמקיימים $|\vec{w}|^2 = \vec{w} \cdot \vec{w}$): $|\vec{v} - \vec{u}|^2 = (\vec{v} - \vec{u}) \cdot (\vec{v} - \vec{u}) = \vec{v} \cdot \vec{v} - 2 \vec{u} \cdot \vec{v} + \vec{u} \cdot \vec{u} = |\vec{v}|^2 - 2 \vec{u} \cdot \vec{v} + |\vec{u}|^2$.

**שלב 4 — השוואה ובידוד:** משוואת הקוסינוסים והפיתוח מעל נותנים $|\vec{u}|^2 + |\vec{v}|^2 - 2 \vec{u} \cdot \vec{v} = |\vec{u}|^2 + |\vec{v}|^2 - 2|\vec{u}|\,|\vec{v}| \cos \theta$. צמצום והעברת אגף: $\vec{u} \cdot \vec{v} = |\vec{u}|\,|\vec{v}| \cos \theta$, ובחילוק (הוקטורים אינם אפס): $\cos \theta = \frac{\vec{u} \cdot \vec{v}}{|\vec{u}|\,|\vec{v}|}$.

**שלב 5 — מובן-טוב:** האגף הימני ב-$[-1, 1]$ לפי אי-שוויון קושי-שוורץ, ועל $[0, \pi]$ הפונקציה $\cos$ חד-חד-ערכית — לכן הזווית $\theta$ מוגדרת באופן יחיד. $\blacksquare$
