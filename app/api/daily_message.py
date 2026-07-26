from fastapi import APIRouter
from app.services.ai_service import get_daily_message

router = APIRouter()

@router.get("/daily-message")
async def daily_message():

    return get_daily_message()