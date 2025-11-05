import json
import os
from datetime import datetime
from uuid import uuid4

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "help_requests.json")

def load_requests():
    if not os.path.exists(DATA_PATH):
        with open(DATA_PATH, "w") as f:
            json.dump([], f)
    with open(DATA_PATH, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_request(request):
    requests = load_requests()
    data = request.dict()
    data["id"] = str(uuid4())
    data["created_at"] = str(datetime.now())
    data["status"] = "pending"
    requests.append(data)
    with open(DATA_PATH, "w") as f:
        json.dump(requests, f, indent=2)

def update_request(request_id, answer):
    requests = load_requests()
    for r in requests:
        if r["id"] == request_id:
            r["supervisor_answer"] = answer
            r["status"] = "resolved"
            r["resolved_at"] = str(datetime.now())
    with open(DATA_PATH, "w") as f:
        json.dump(requests, f, indent=2)

def get_all_requests():
    return load_requests()