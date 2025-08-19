from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Any
from app.deps.auth import get_current_user

router = APIRouter()

class PartnerCompatRequest(BaseModel):
    userOrgId: str

@router.post("/")
async def handle(_req: PartnerCompatRequest, user=Depends(get_current_user)):
    return {"compatibilityResults": []}
