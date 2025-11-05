Human-in-the-Loop AI Voice Assistant

An AI system that answers customer queries in realtime, learns from a supervisor, and improves its knowledge base over time.

This project contains:

AI Agent (backend) — answers questions using knowledge base, LLM or fallback.

Human Supervisor Dashboard (frontend) — allows supervisor to review & respond to escalated questions.

Knowledge Base — automatically updated from supervisor responses.

Voice AI interaction — frontend page where user chats with AI (with browser TTS voice output).

Tech Stack
Component	Technology
Backend	Python + FastAPI
Frontend	React + Vite
Storage	JSON files (no database needed)
Optional LLM	OpenAI API (if key provided)
Project Structure
backend/
  app/
    routes/
      agent.py
      knowledge.py
      supervisor.py
      requests.py
    services/
      ai_agent.py
      db_service.py
      knowledge_base.py
    data/
      help_requests.json
      knowledge_base.json
frontend/
  src/
    pages/
      AIChat.jsx
    components/
    api/
README.md

Setup Instructions
1) Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate   # windows
pip install -r requirements.txt


Optionally add your OpenAI API or LiveKit Agent key:

create .env in backend:

OPENAI_API_KEY=sk-xxxx
LIVEKIT_URL=XXXXXXXXXXXXXXXXXXXXXX
LIVEKIT_API_KEY=XXXXXXXXXXXXXXXXX
LIVEKIT_API_SECRET=XXXXXXXXXXXXX
OPENAI_API_KEY=sk-XXXXXxxxx



Start backend:

uvicorn app.main:app --reload


Backend runs at → http://127.0.0.1:8000

2) Frontend Setup
cd frontend
npm install
npm run dev


Frontend runs at → http://127.0.0.1:5173

How The System Works
Step	Description
1. User asks a question	front-end /ai page
2. Backend tries to answer	from knowledge_base.json
3. If confidence is low	it escalates → stored in help_requests.json
4. Supervisor sees pending requests	Dashboard page
5. Supervisor answers	their answer is saved + added to KB
6. Next time, AI answers automatically	because KB is now richer

The system gets smarter automatically.

Screens
Page	URL
AI Chat (voice)	/ai
Supervisor Dashboard	/dashboard
JSON Storage

help_requests.json = pending / resolved escalations

knowledge_base.json = known Q&A pairs

Example knowledge_base.json:

[
  { "question": "do you offer facials?", "answer": "Yes, we offer spa and facial services from 10 AM to 8 PM." }
]

Optional Features
Feature	Status
OpenAI integration	supported (if key added)
Browser Text-To-Speech	enabled
Auto refresh dashboard	enabled
Run Order

Start backend

Start frontend

Open dashboard → resolve escalations

Open AI chat → test learned responses

Conclusion

This project implements a full human-in-the-loop AI system which teaches itself from supervisor feedback and stores that learning permanently.
