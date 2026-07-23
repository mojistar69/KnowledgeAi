from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ai_service import get_word_meanings

router = APIRouter()


class VerseRequest(BaseModel):
    verse: str


@router.post("/word-meaning")
def word_meaning(request: VerseRequest):

    result = get_word_meanings(request.verse)

    return {
        "verse": request.verse,
        "words": result["words"]
    }