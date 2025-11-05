from pydantic import BaseModel

class SupervisorResponse(BaseModel):
    request_id: str
    answer: str