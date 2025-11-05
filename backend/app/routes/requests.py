from fastapi import APIRouter
from app.services import db_service
from app.models.request_model import HelpRequest

router = APIRouter(prefix="/requests", tags=["Requests"])

@router.get("/")
def get_all_requests():
    return db_service.get_all_requests()

@router.post("/")
def create_request(request: HelpRequest):
    db_service.save_request(request)
    return {"message": "Request saved successfully"}