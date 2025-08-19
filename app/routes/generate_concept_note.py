from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Any, Optional
from app.deps.auth import get_current_user

router = APIRouter()

class ConceptNoteRequest(BaseModel):
    project: Any
    organization: Any
    format: Optional[str] = 'html'

@router.post("/")
async def handle(_req: ConceptNoteRequest, user=Depends(get_current_user)):
    return {"message": "generate-concept-note stub", "downloadUrl": "https://example.com/file.html", "conceptId": "stub-123"}
