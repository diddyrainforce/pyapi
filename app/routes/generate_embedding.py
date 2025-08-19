from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List
from app.deps.auth import get_current_user

router = APIRouter()

class EmbeddingRequest(BaseModel):
    text: str

@router.post("/")
async def handle(_req: EmbeddingRequest, user=Depends(get_current_user)):
    # Return a dummy zero-vector for now
    return {"embedding": [0.0 for _ in range(10)]}
