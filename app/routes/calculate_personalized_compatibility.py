from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Any
from app.deps.auth import get_current_user

router = APIRouter()

class PersonalizedCompatRequest(BaseModel):
    user_id: str
    project_id: str
    project_data: Any
    user_profile: Any

@router.post("/")
async def handle(_req: PersonalizedCompatRequest, user=Depends(get_current_user)):
    return {"message": "calculate-personalized-compatibility stub"}
