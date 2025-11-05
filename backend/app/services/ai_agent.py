# backend/app/services/ai_agent.py
import os
import json
import random
from datetime import datetime
from dotenv import load_dotenv
from gtts import gTTS

# ---- IMPORT DB SERVICE FOR ESCALATION ----
from . import db_service

try:
    from openai import OpenAI
except Exception:
    OpenAI = None

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai_client = OpenAI(api_key=OPENAI_API_KEY) if (OpenAI and OPENAI_API_KEY) else None

KB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "knowledge_base.json")
AUDIO_FOLDER = os.path.join(os.path.dirname(__file__), "..", "data", "audio")

os.makedirs(AUDIO_FOLDER, exist_ok=True)


def synthesize_audio(text: str):
    ts = datetime.now().strftime("%Y%m%d%H%M%S%f")
    filename = f"tts_{ts}.mp3"
    filepath = os.path.join(AUDIO_FOLDER, filename)

    tts = gTTS(text)
    tts.save(filepath)

    return f"/audio/{filename}"


def load_kb():
    if not os.path.exists(KB_PATH):
        return []
    try:
        with open(KB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def find_answer(question: str):
    kb = load_kb()
    q = question.lower().strip().strip('"')
    for item in kb:
        if "question" in item and item["question"]:
            if item["question"].lower().strip().strip('"') in q or q in item["question"].lower():
                return item.get("answer")
    return None


def simulated_answer(question: str):
    templates = [
        "Thanks for asking — {}. If you need more details, I can check with a supervisor.",
        "Good question. {}. I can confirm with my supervisor if you'd like.",
        "From the available info: {}. Let me know if you'd like me to escalate."
    ]
    base = f"I think the answer is related to '{question}'."
    return random.choice(templates).format(base)


def get_answer(question: str):
    # 1) try KB
    kb_answer = find_answer(question)
    if kb_answer:
        audio_url = synthesize_audio(kb_answer)
        return {
            "agent": "mock_tts_agent",
            "answer": kb_answer,
            "confidence": 0.95,
            "escalated": False,
            "source": "knowledge_base",
            "audio": audio_url
        }

    # 2) try openai
    if openai_client:
        try:
            resp = openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a concise, polite hotel assistant."},
                    {"role": "user", "content": question}
                ],
                max_tokens=150,
            )
            text = resp.choices[0].message.content.strip()
            audio_url = synthesize_audio(text)
            return {
                "agent": "openai_text_agent",
                "answer": text,
                "confidence": 0.8,
                "escalated": False,
                "source": "openai",
                "audio": audio_url
            }
        except:
            pass

    # 3) fallback = escalate
    confidence = round(random.uniform(0.3, 0.65), 2)
    escalated = confidence < 0.7
    answer_text = simulated_answer(question)
    audio_url = synthesize_audio(answer_text)

    result = {
        "agent": "mock_tts_agent",
        "answer": answer_text,
        "confidence": confidence,
        "escalated": escalated,
        "source": "simulated",
        "audio": audio_url
    }

    if escalated:
        fake_request = {"question": question}
        class Obj: pass
        o = Obj()
        o.dict = lambda: fake_request
        db_service.save_request(o)

    return result