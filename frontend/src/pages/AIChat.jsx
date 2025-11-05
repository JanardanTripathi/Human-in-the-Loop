// frontend/src/pages/AIChat.jsx
import React, { useState, useRef, useEffect } from "react";
import "./AIChat.css";

const API_BASE = "http://127.0.0.1:8000";

const speakText = (text) => {
  if (!("speechSynthesis" in window)) return;
  const utter = new SpeechSynthesisUtterance(text);

  const voices = window.speechSynthesis.getVoices();
  if (voices && voices.length) {
    const v = voices.find((v) => v.lang && v.lang.includes("en")) || voices[0];
    if (v) utter.voice = v;
  }
  utter.rate = 1.0;
  utter.pitch = 1.0;
  window.speechSynthesis.cancel();
  window.speechSynthesis.speak(utter);
};

const AIChat = () => {
  const [messages, setMessages] = useState([
    { sender: "ai", text: "Hello — I'm your voice-enabled AI assistant. Ask me anything." },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const boxRef = useRef(null);

  useEffect(() => {
    const last = messages[messages.length - 1];
    if (last && last.sender === "ai") speakText(last.text);
    if (boxRef.current) boxRef.current.scrollTop = boxRef.current.scrollHeight;
  }, [messages]);

  const sendMessage = async (e) => {
    e && e.preventDefault();
    if (!input.trim()) return;
    const userMsg = { sender: "user", text: input };
    setMessages((m) => [...m, userMsg]);
    setLoading(true);
    const q = input;
    setInput("");

    try {
      // ✅ FIXED ENDPOINT -- from /ai/call -> /ai/ask
      const url = `${API_BASE}/ai/ask?question=${encodeURIComponent(q)}`;

      const res = await fetch(url);
      if (!res.ok) throw new Error("Failed to reach backend");
      const data = await res.json();

      const aiMsg = { sender: "ai", text: data.answer };
      setMessages((m) => [...m, aiMsg]);

      speakText(data.answer);

    } catch (err) {
      console.error(err);
      const aiMsg = { sender: "ai", text: "Sorry — could not reach the backend." };
      setMessages((m) => [...m, aiMsg]);
      speakText("Sorry, I could not reach the backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <h2 className="chat-title">AI Agent Interaction (Voice Simulated)</h2>
      <div className="chat-box" ref={boxRef}>
        {messages.map((msg, i) => (
          <div key={i} className={`chat-message ${msg.sender}`}>
            <div className="message-bubble">{msg.text}</div>
          </div>
        ))}
        {loading && (
          <div className="chat-message ai">
            <div className="message-bubble">Thinking...</div>
          </div>
        )}
      </div>

      <form className="chat-input-area" onSubmit={sendMessage}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
        />
        <button type="submit" disabled={loading}>Send</button>
      </form>
      <div style={{ marginTop: 8, fontSize: 12, color: "#666" }}>
        Tip: Allow your browser to use speech synthesis/voices if asked.
      </div>
    </div>
  );
};

export default AIChat;