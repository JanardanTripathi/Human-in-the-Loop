# backend/app/routes/agent.py
from fastapi import APIRouter, Query
from ..services.ai_agent import get_answer

router = APIRouter(prefix="/ai", tags=["AI Agent"])

@router.get("/ask")
def ask(question: str = Query(...)):
    result = get_answer(question)
    return result
