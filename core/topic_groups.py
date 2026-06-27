"""Hierarchical grouping of fine-grained topics into a few high-level groups.

Used by the topic filter UI to offer "select-all-related" buttons. Editing
this file is the single point of truth — restart the server to apply.

Topics not listed here remain individually selectable but don't belong to
any group. If a topic in the data changes name, update the matching entry.
"""
from __future__ import annotations


def topic_to_group(groups: "dict[str, list[str]] | None" = None) -> dict[str, str]:
    """Reverse map: topic name → containing group name (the main topic).

    Used to label individual claims with their main topic in card metadata.
    """
    if groups is None:
        groups = TOPIC_GROUPS
    return {topic: group_name
            for group_name, topics in groups.items()
            for topic in topics}


def topic_groups_with_other(all_topics: list[str],
                             groups: "dict[str, list[str]] | None" = None) -> dict[str, list[str]]:
    """Augment the configured groups with an 'אחר' bucket for topics that
    didn't get assigned to any group. Lets the UI render every topic under a
    collapsible section without losing any.
    """
    if groups is None:
        groups = TOPIC_GROUPS
    grouped: set[str] = set()
    for vals in groups.values():
        grouped.update(vals)
    other = sorted(t for t in all_topics if t not in grouped)
    result = dict(groups)
    if other:
        result["אחר"] = other
    return result


TOPIC_GROUPS: dict[str, list[str]] = {
    "אלגברה ויסודות": [
        "אקסיומות שדה", "אקסיומות סדר", "אלגברה בסיסית",
        "יחידות", "פעולות יסודיות", "חזקות", "ערך מוחלט",
        "זהויות אלגבריות", "פולינומים", "פונקציה ריבועית",
        "משוואות לינאריות", "חזקות ושורשים",
    ],
    "אי-שוויונים": [
        "אי-שוויונים", "אי-שוויונים קלאסיים",
    ],
    "פונקציות": [
        "פונקציות", "תכונות פונקציות", "טרנספורמציות פונקציה",
    ],
    "חדו״א": [
        "גבולות", "הקדמה לחדו״א",
        "נגזרות", "כללי גזירה", "נגזרות פונקציות",
        "יישומי נגזרת", "נגזרת מתקדמת",
        "אינטגרלים", "אינטגרל מסוים", "אינטגרל מתקדם", "יישומי אינטגרל",
        "חדו״א בכמה משתנים", "טור טיילור",
    ],
    "סדרות וטורים": [
        "סדרות", "סדרות מתקדם", "טורים",
    ],
    "טריגונומטריה": [
        "טריגונומטריה", "טריגונומטריה מתקדמת",
    ],
    "מעריכיים ולוגריתמים": [
        "מעריכיים", "לוגריתמים",
    ],
    "גאומטריה": [
        "גאומטריה", "גאומטריית מעגל", "חפיפה ודמיון",
        "מרכזי משולש", "גאומטריה במרחב",
        "גאומטריה אנליטית", "גאומטריה אנליטית 3D",
        "חתכי חרוט",
    ],
    "וקטורים ואלגברה לינארית": [
        "וקטורים", "אלגברה לינארית",
    ],
    "מספרים מרוכבים": [
        "מספרים מרוכבים",
    ],
    "תורת המספרים": [
        "מערכות מספרים", "התחלקות", "שברים",
        "תורת המספרים", "תורת מספרים מתקדמת",
    ],
    "תורת הקבוצות": [
        "תורת הקבוצות",
    ],
    "הסתברות וסטטיסטיקה": [
        "הסתברות", "הסתברות מתקדמת",
        "סטטיסטיקה", "סטטיסטיקה מתקדמת",
    ],
    "קומבינטוריקה": [
        "קומבינטוריקה", "קומבינטוריקה מתקדמת",
    ],
    "יישומים": [
        "מודלים", "מתמטיקה פיננסית", "פיזיקה",
    ],
}
