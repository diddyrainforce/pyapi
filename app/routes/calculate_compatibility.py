from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Any
from app.deps.auth import get_current_user

router = APIRouter()

class CompatRequest(BaseModel):
    type: str
    data: Any

@router.post("/")
async def handle(req: CompatRequest, user=Depends(get_current_user)):
    return {"message": "calculate-compatibility stub"}
