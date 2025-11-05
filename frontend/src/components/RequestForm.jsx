import React, { useState } from "react";

const RequestForm = ({ selected, onRespond }) => {
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  if (!selected) {
    return (
      <div className="card">
        <h2>Respond to Request</h2>
        <p className="empty-state">Select a request to respond.</p>
      </div>
    );
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!answer.trim()) return;
    setLoading(true);
    try {
      await onRespond(selected.id, answer);
      setAnswer("");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>Respond to Request</h2>
      <p className="form-subtitle">{selected.question}</p>
      <form onSubmit={handleSubmit}>
        <textarea
          className="response-box"
          placeholder="Enter your response..."
          value={answer}
          onChange={(e) => setAnswer(e.target.value)}
          required
        />
        <div style={{ marginTop: 10 }}>
          <button className="btn" type="submit" disabled={loading}>
            {loading ? "Submitting..." : "Submit Response"}
          </button>
        </div>
      </form>
    </div>
  );
};

export default RequestForm;