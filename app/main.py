from fastapi import FastAPI
from app.api import quran
from app.api import insight
from app.api import daily_message



app = FastAPI(
    title="KnowledgeBook AI Server"
)


app.include_router(
    quran.router,
    prefix="/api/quran"
)
app.include_router(insight.router)
app.include_router(daily_message.router)

@app.get("/")
def home():
    return {
        "message": "KnowledgeBook AI Server is running"
    }