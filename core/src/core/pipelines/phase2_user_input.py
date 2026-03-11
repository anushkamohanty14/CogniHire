from pathlib import Path
from typing import Any, Dict, List


def create_user_profile(
    user_id: str,
    manual_skills: List[str] | None = None,
    interest_tags: List[str] | None = None,
) -> Dict[str, Any]:
    """Create a normalized user profile payload for persistence."""
    if not user_id or not user_id.strip():
        raise ValueError("user_id is required")

    cleaned_skills = sorted({s.strip().lower() for s in (manual_skills or []) if s and s.strip()})
    cleaned_tags = sorted({t.strip().lower() for t in (interest_tags or []) if t and t.strip()})

    return {
        "user_id": user_id.strip(),
        "manual_skills": cleaned_skills,
        "interest_tags": cleaned_tags,
    }


def upload_resume(file_name: str, content: bytes, user_id: str) -> Dict[str, Any]:
    """Save uploaded resume to local storage and return metadata."""
    safe_name = Path(file_name).name
    output_dir = Path("data/interim/resumes") / user_id
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / safe_name
    output_path.write_bytes(content)
    return {
        "user_id": user_id,
        "file_name": safe_name,
        "saved_path": str(output_path),
        "size_bytes": len(content),
    }


def collect_manual_skills(raw_skills: str) -> List[str]:
    """Parse comma-separated skills from UI input."""
    return [item.strip() for item in raw_skills.split(",") if item.strip()]


def collect_interest_tags(raw_tags: str) -> List[str]:
    """Parse comma-separated career-interest tags from UI input."""
    return [item.strip() for item in raw_tags.split(",") if item.strip()]


def suggest_jobs_from_interest_tags(interest_tags: List[str], job_titles: List[str], top_k: int = 10) -> List[str]:
    """Simple lexical matching from user interest tags to Phase 1 job titles."""
    tags = [t.lower().strip() for t in interest_tags if t.strip()]
    if not tags:
        return []

    ranked: List[tuple[str, int]] = []
    for title in job_titles:
        lower = title.lower()
        score = sum(1 for tag in tags if tag in lower)
        if score > 0:
            ranked.append((title, score))

    ranked.sort(key=lambda item: (-item[1], item[0]))
    return [title for title, _ in ranked[:top_k]]
