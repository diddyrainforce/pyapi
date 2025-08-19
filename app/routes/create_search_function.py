from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Any
from app.deps.auth import get_current_user

router = APIRouter()

class CreateSearchRequest(BaseModel):
    name: str | None = None

@router.post("/")
async def handle(_req: CreateSearchRequest, user=Depends(get_current_user)):
    return {"message": "create-search-function stub"}
