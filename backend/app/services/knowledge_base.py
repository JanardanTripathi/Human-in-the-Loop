import json
import os

KB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "knowledge_base.json")


def load_kb():
    """Load the knowledge base safely — always returns a list."""
    if not os.path.exists(KB_PATH):
        # Create the file if missing
        with open(KB_PATH, "w", encoding="utf-8") as f:
            json.dump([], f)

    try:
        with open(KB_PATH, "r", encoding="utf-8") as f:
            data = f.read().strip()
            if not data:
                return []

            parsed = json.loads(data)
            # ✅ ensure it’s a list
            if isinstance(parsed, list):
                return parsed
            else:
                print("⚠️ Knowledge base was not a list — fixing it.")
                return [parsed]
    except json.JSONDecodeError:
        print("⚠️ Corrupted JSON detected — resetting knowledge base.")
        return []
    except Exception as e:
        print(f"❌ Error loading knowledge base: {e}")
        return []


def save_kb(kb):
    """Save the knowledge base safely."""
    try:
        with open(KB_PATH, "w", encoding="utf-8") as f:
            json.dump(kb, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"❌ Error saving knowledge base: {e}")


def learn_answer(question, answer):
    """Add a new question-answer pair to the knowledge base."""
    kb = load_kb()
    if not isinstance(kb, list):
        kb = []
    kb.append({"question": question, "answer": answer})
    save_kb(kb)
    print(f"✅ Added to knowledge base: {question} → {answer}")