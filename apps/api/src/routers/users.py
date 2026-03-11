from fastapi import APIRouter

from ..schemas.users import UserProfileCreate, UserProfileResponse
from core.src.core.pipelines.phase2_user_input import create_user_profile

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/profile", response_model=UserProfileResponse)
def create_profile(payload: UserProfileCreate) -> UserProfileResponse:
    normalized = create_user_profile(
        user_id=payload.user_id,
        manual_skills=payload.manual_skills,
        interest_tags=payload.interest_tags,
    )
    return UserProfileResponse(**normalized)
