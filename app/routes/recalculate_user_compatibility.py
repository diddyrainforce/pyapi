from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Any, List
from app.deps.auth import get_current_user

router = APIRouter()

class RecalcRequest(BaseModel):
    user_id: str
    projects: List[Any]
    user_profile: Any
    preferences_hash: str

@router.post("/")
async def handle(_req: RecalcRequest, user=Depends(get_current_user)):
    return {"message": "recalculate-user-compatibility stub"}
