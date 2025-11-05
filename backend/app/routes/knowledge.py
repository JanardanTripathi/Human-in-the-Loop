# backend/app/routes/knowledge.py
from fastapi import APIRouter
import os, json

router = APIRouter(prefix="/knowledge", tags=["Knowledge Base"])

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "knowledge_base.json")

@router.get("/")
def get_knowledge_base():
    """Return the full knowledge base as JSON."""
    if not os.path.exists(DATA_PATH):
        return []
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = f.read().strip()
            return json.loads(data) if data else []
    except Exception as e:
        return {"error": f"Failed to load knowledge base: {e}"}

@router.post("/add")
def add_to_knowledge_base(entry: dict):
    """Add a new Q&A pair to the knowledge base."""
    try:
        data = []
        if os.path.exists(DATA_PATH):
            with open(DATA_PATH, "r", encoding="utf-8") as f:
                file_data = f.read().strip()
                if file_data:
                    data = json.loads(file_data)
        data.append(entry)
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return {"message": "Knowledge base updated successfully."}
    except Exception as e:
        return {"error": str(e)}        