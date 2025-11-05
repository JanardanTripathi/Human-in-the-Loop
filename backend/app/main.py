from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routes import requests, supervisor, calls, knowledge
from .routes.agent import router as agent_router

app = FastAPI(title="Human-in-the-Loop AI Backend")

# ✅ Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ allow browser access generated audio files
app.mount("/audio", StaticFiles(directory="app/data/audio"), name="audio")

# ✅ Include your routers
app.include_router(requests.router)
app.include_router(agent_router)    
app.include_router(supervisor.router)
app.include_router(calls.router)
app.include_router(knowledge.router)

@app.get("/")
def root():
    return {"message": "Backend is running!"}