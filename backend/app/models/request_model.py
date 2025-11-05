from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class HelpRequest(BaseModel):
    id: str
    question: str
    customer_id: str
    status: str = "pending"  # pending | resolved | timeout
    supervisor_answer: Optional[str] = None
    created_at: datetime = datetime.utcnow()
    resolved_at: Optional[datetime] = None