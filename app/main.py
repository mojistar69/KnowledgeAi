from fastapi import FastAPI
from app.api import quran


app = FastAPI(
    title="KnowledgeBook AI Server"
)


app.include_router(
    quran.router,
    prefix="/api/quran"
)


@app.get("/")
def home():
    return {
        "message": "KnowledgeBook AI Server is running"
    }