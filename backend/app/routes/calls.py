# backend/app/routes/calls.py
from fastapi import APIRouter, Query
from app.services.ai_agent import get_answer

router = APIRouter(prefix="/ai", tags=["AI"])

@router.get("/call")
def call_ai(question: str = Query(..., description="Customer question to the AI agent")):
    """
    Call the AI agent (text). Returns JSON with answer + metadata.
    Frontend will use browser TTS to speak the 'answer'.
    """
    res = get_answer(question)
    return res