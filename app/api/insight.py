from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_service import get_ai_insight

router = APIRouter()

class VerseRequest(BaseModel):
    verse: str

@router.post("/ai-insight")
async def ai_insight(request: VerseRequest):

    return get_ai_insight(request.verse)