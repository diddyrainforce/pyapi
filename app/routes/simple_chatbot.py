from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.deps.auth import get_current_user

router = APIRouter()

class ChatbotRequest(BaseModel):
    message: str

@router.post("/")
async def handle(req: ChatbotRequest, user=Depends(get_current_user)):
    return {"reply": f"You said: {req.message}"}
