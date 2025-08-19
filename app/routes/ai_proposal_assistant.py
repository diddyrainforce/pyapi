from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Any, List, Optional
from app.config import config
from app.deps.auth import get_current_user

router = APIRouter()

class AssistantRequest(BaseModel):
    action: Optional[str] = None
    proposalData: Optional[Any] = None
    proposalId: Optional[str] = None
    prompt: Optional[str] = None
    context: Optional[str] = None
    conversation_history: Optional[List[Any]] = None

@router.post("/")
async def handle(req: AssistantRequest, user=Depends(get_current_user)):
    # Partnership assistant path
    if req.prompt and req.context == 'partnership_assistant':
        if not config.OPENAI_API_KEY:
            return {"error": "OPENAI_API_KEY not configured"}
        return {"message": "partnership assistant stub", "tokens_used": 0}

    if not req.action:
        return {"error": "Missing action"}

    if req.action in {"generate_proposal", "analyze_proposal", "get_suggestions", "find_matches", "get_rag_context"}:
        return {"message": f"{req.action} stub"}

    return {"error": "Invalid action"}
