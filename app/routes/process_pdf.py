from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from app.deps.auth import get_current_user

router = APIRouter()

class ProcessPdfRequest(BaseModel):
    url: Optional[str] = None
    file_id: Optional[str] = None

@router.post("/")
async def handle(_req: ProcessPdfRequest, user=Depends(get_current_user)):
    return {"text": "", "pages": 0}
