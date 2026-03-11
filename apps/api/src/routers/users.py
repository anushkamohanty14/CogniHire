from fastapi import APIRouter, File, HTTPException, UploadFile

from ..schemas.users import ResumeUploadResponse, UserProfileCreate, UserProfileResponse
from ..services.profile_service import ProfileService
from core.src.core.pipelines.phase2_user_input import upload_resume

router = APIRouter(prefix="/users", tags=["users"])
service = ProfileService()


@router.post("/profile", response_model=UserProfileResponse)
def create_profile(payload: UserProfileCreate) -> UserProfileResponse:
    normalized = service.create_profile(
        user_id=payload.user_id,
        manual_skills=payload.manual_skills,
        interest_tags=payload.interest_tags,
    )
    return UserProfileResponse(**normalized)


@router.get("/profile/{user_id}", response_model=UserProfileResponse)
def get_profile(user_id: str) -> UserProfileResponse:
    profile = service.get_profile(user_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="profile not found")
    return UserProfileResponse(**profile)


@router.post("/resume", response_model=ResumeUploadResponse)
async def upload_user_resume(user_id: str, file: UploadFile = File(...)) -> ResumeUploadResponse:
    content = await file.read()
    metadata = upload_resume(file.filename, content, user_id)
    return ResumeUploadResponse(**metadata)
