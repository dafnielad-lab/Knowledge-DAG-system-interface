"""University-level courses (above 5-unit matriculation).

Defines the 6 new courses and the topic→course mapping that re-classifies
existing claims whose topics fall above the 5-unit curriculum.

Run as part of seed_curriculum.py. Migration is idempotent — claims already
in the right university course aren't touched.
"""
from __future__ import annotations

from core.models import Course
from storage import files


COURSES: list[Course] = [
    Course(id="math_uni_analysis",
           name="אנליזה 1 (חדו״א, ODE, רב-משתני)",
           prerequisites=["math_hs_5"]),
    Course(id="math_uni_linear_algebra",
           name="אלגברה לינארית 1",
           prerequisites=["math_hs_5"]),
    Course(id="math_uni_number_theory",
           name="תורת המספרים האלמנטרית",
           prerequisites=["math_hs_5"]),
    Course(id="math_uni_prob_stats",
           name="הסתברות וסטטיסטיקה",
           prerequisites=["math_hs_5"]),
    Course(id="math_uni_advanced_geometry",
           name="גאומטריה אולימפית",
           prerequisites=["math_hs_5"]),
    Course(id="math_uni_advanced_algebra",
           name="אי-שוויונים וקומבינטוריקה אולימפית",
           prerequisites=["math_hs_5"]),
]


# Topic → target university course. Claims with these topics get re-classified.
TOPIC_TO_UNI_COURSE: dict[str, str] = {
    # אנליזה אוניברסיטה
    "חדו״א בכמה משתנים":   "math_uni_analysis",
    "טור טיילור":           "math_uni_analysis",
    "אנליזה":               "math_uni_analysis",
    "נגזרת מתקדמת":         "math_uni_analysis",
    "שיטות נומריות":        "math_uni_analysis",
    "פונקציות מיוחדות":     "math_uni_analysis",
    "אינטגרל מתקדם":        "math_uni_analysis",
    "טורים":                "math_uni_analysis",
    "משוואות דיפרנציאליות": "math_uni_analysis",

    # אלגברה לינארית
    "אלגברה לינארית":       "math_uni_linear_algebra",

    # תורת מספרים אוניברסיטה
    "תורת מספרים מתקדמת":   "math_uni_number_theory",

    # הסתברות וסטטיסטיקה אוניברסיטה
    "הסתברות מתקדמת":       "math_uni_prob_stats",
    "סטטיסטיקה מתקדמת":     "math_uni_prob_stats",

    # גאומטריה אולימפית
    "מרכזי משולש":          "math_uni_advanced_geometry",
    "גאומטריה מתקדמת":      "math_uni_advanced_geometry",

    # אלגברה / אי-שוויונים מתקדמים
    "אי-שוויונים קלאסיים":  "math_uni_advanced_algebra",
    "קומבינטוריקה מתקדמת":  "math_uni_advanced_algebra",
}


def migrate_claims_to_uni_courses(data_dir):
    """Re-classify claims whose topic falls above 5-unit scope.

    Idempotent: only re-saves a claim if its course differs from the target.
    Returns (moved_count, by_target).
    """
    moved = 0
    by_target: dict[str, int] = {}
    claims, _, _ = files.scan_data_dir(data_dir)
    for c in claims:
        if not c.topic:
            continue
        target = TOPIC_TO_UNI_COURSE.get(c.topic)
        if target is None or c.course == target:
            continue
        c.course = target
        files.save_claim(c, data_dir)
        moved += 1
        by_target[target] = by_target.get(target, 0) + 1
    return moved, by_target
