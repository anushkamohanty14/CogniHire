from typing import Any, Dict, List


def create_user_profile(
    user_id: str,
    manual_skills: List[str] | None = None,
    interest_tags: List[str] | None = None,
) -> Dict[str, Any]:
    """Create a normalized user profile payload for persistence."""
    if not user_id:
        raise ValueError("user_id is required")

    cleaned_skills = sorted({s.strip().lower() for s in (manual_skills or []) if s and s.strip()})
    cleaned_tags = sorted({t.strip().lower() for t in (interest_tags or []) if t and t.strip()})

    return {
        "user_id": user_id.strip(),
        "manual_skills": cleaned_skills,
        "interest_tags": cleaned_tags,
    }


def collect_manual_skills(raw_skills: str) -> List[str]:
    """Parse comma-separated skills from UI input."""
    return [item.strip() for item in raw_skills.split(",") if item.strip()]


def collect_interest_tags(raw_tags: str) -> List[str]:
    """Parse comma-separated career-interest tags from UI input."""
    return [item.strip() for item in raw_tags.split(",") if item.strip()]
