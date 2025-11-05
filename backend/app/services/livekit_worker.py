# backend/app/services/livekit_worker.py
"""
LiveKit Worker Placeholder
--------------------------
This structure mirrors a real LiveKit worker but avoids exposing secrets.
When ready, install `livekit-agents` and move your credentials to .env.
"""

import os
from dotenv import load_dotenv
# from livekit.agents import WorkerOptions, JobContext, cli
# from livekit.agents.voice_assistant import VoiceAssistantAgent
from .ai_agent import ai_agent

load_dotenv()

LIVEKIT_URL = os.getenv("LIVEKIT_URL")
LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY")
LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET")

def run_local_test():
    """Simulate how LiveKit agent would use your AI logic."""
    print("🧠 Simulated LiveKit Worker running in text-only mode")
    while True:
        question = input("\n🎤 Ask something (or type 'exit'): ")
        if question.lower() == "exit":
            break
        response = ai_agent.get_answer(question)
        print(f"🤖 {response['answer']} (confidence: {response['confidence']})")

if __name__ == "__main__":
    run_local_test()
