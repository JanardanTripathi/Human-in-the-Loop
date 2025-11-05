# backend/app/routes/supervisor.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..services import db_service, knowledge_base

router = APIRouter(prefix="/supervisor", tags=["Supervisor"])

# Define the model for the POST request body
class SupervisorResponse(BaseModel):
    request_id: str
    answer: str

@router.post("/respond")
def respond(data: SupervisorResponse):
    """Record supervisor’s response and update the knowledge base."""
    try:
        request_id = data.request_id
        answer = data.answer

        # Update the request in the database
        db_service.update_request(request_id, answer)
        print(f"✅ Supervisor answered request {request_id}: {answer}")

        # Update the knowledge base
        all_requests = db_service.get_all_requests()
        for r in all_requests:
            if str(r["id"]) == str(request_id):
                question = r["question"]
                knowledge_base.learn_answer(question, answer)
                break

        return {"message": "Response recorded and knowledge base updated."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))