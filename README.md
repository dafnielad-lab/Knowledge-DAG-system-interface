# Knowledge DAG System

מערכת אישית לתיעוד חומר לימוד מתמטי כגרף מכוון של טענות, הוכחות ויחסים.

## הרצה

```cmd
Run.bat
```

ואז דפדפן ל-http://localhost:8000

## מבנה

- `data/` — מקור האמת. Markdown+YAML, ניתן לעריכה ידנית, ניתן ל-git
- `core/` — לוגיקה טהורה (מודלים, DAG, סטטוסים)
- `storage/` — קריאה/כתיבה של קבצים + אינדקס SQLite נגזר
- `verification/` — פלאגינים לשיטות אימות
- `api/` — FastAPI endpoints
- `web/` — Jinja2 templates + static assets
- `tests/` — pytest

## תכנון מלא

ראה את תוכנית העיצוב המקורית ב-`C:\Users\elad\Documents\knowledge_dag_system.html`.
