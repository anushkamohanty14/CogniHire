from pydantic import BaseModel, Field


class UserProfileCreate(BaseModel):
    user_id: str = Field(min_length=1)
    manual_skills: list[str] = Field(default_factory=list)
    interest_tags: list[str] = Field(default_factory=list)


class UserProfileResponse(UserProfileCreate):
    pass
