# Knowledge DAG System

מערכת אישית לתיעוד חומר לימוד מתמטי כגרף מכוון של טענות, הוכחות ויחסים.

## הרצה מקומית (Windows)

```cmd
Run.bat
```

ואז דפדפן ל-http://localhost:8000 (ללא סיסמה — הגנה פעילה רק כשמשתני סביבה מוגדרים).

## הרצה מקומית (Linux/Mac, או clone חדש)

```bash
git clone https://github.com/dafnielad-lab/Knowledge-DAG-system-interface.git
cd Knowledge-DAG-system-interface
pip install -r requirements.txt
python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

## הרצה ב-Render (URL ציבורי עם סיסמה)

1. דחוף את הקוד ל-GitHub (כבר נעשה).
2. ב-Render.com: **New +** → **Blueprint** → חבר את הריפו.
3. אחרי deploy ראשון: לך ל-**Environment** של השירות והוסף:
   - `AUTH_USERNAME` = שם משתמש שתבחר
   - `AUTH_PASSWORD` = סיסמה חזקה
4. Render יעשה redeploy אוטומטי. ה-URL יראה משהו כמו `https://knowledge-dag.onrender.com`.

**מגבלות free tier:**
- האפליקציה "נרדמת" אחרי 15 דק׳ של ידלאיות, מתעוררת ב-~30 שניות בבקשה הראשונה.
- העריכות שתעשה דרך הממשק **לא נשמרות בין אתחולים** (filesystem ארעי). המאגר ב-GitHub נשאר source of truth.
- כדי להחזיק עריכות אונליין, שדרג ל-plan starter ($7/חודש) והפעל persistent disk ב-`render.yaml`.

## מבנה

- `data/` — מקור האמת. Markdown+YAML, ניתן לעריכה ידנית, ניתן ל-git.
- `core/` — לוגיקה טהורה (מודלים, DAG, סטטוסים, קבוצות נושאים).
- `storage/` — קריאה/כתיבה של קבצים + אינדקס SQLite נגזר.
- `verification/` — פלאגינים לשיטות אימות (informal, מוכן ל-Lean/AI עתידיים).
- `api/` — FastAPI endpoints (CRUD + Cowork ingest + DAG queries).
- `web/` — Jinja2 templates + CSS + auth middleware.
- `tests/` — pytest.
- `seed_*.py` + `seed_curriculum.py` — סקריפט יצירת/עדכון התוכן.

## אבטחה (Basic Auth)

- כשמשתני הסביבה `AUTH_USERNAME` ו-`AUTH_PASSWORD` מוגדרים, **כל בקשה** מצריכה אימות.
- מקומית בלי המשתנים → ללא הגנה (פשוט להפעיל).
- ב-Render הם **חובה** — אחרת המאגר חשוף לעולם.

## תוכן

12 קורסים, 687 טענות, 345 הוכחות (כיסוי 100% של משפטים), 12 קבוצות נושא היררכיות. מ-יסודות עד 5 יח״ל, פלוס 6 קורסי אוניברסיטה (אנליזה 1, אלגברה לינארית, תורת מספרים, הסתברות וסטטיסטיקה, גאומטריה אולימפית, אי-שוויונים מתקדמים).

## תכנון מלא

מסמך עיצוב מקורי: `~/Documents/knowledge_dag_system.html`.
