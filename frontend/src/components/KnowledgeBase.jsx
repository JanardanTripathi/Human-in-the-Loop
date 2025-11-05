import React from "react";

const KnowledgeBase = ({ knowledge }) => {
  return (
    <div className="card">
      <h2>Knowledge Base</h2>
      {knowledge.length === 0 ? (
        <p className="empty-state">No knowledge entries yet.</p>
      ) : (
        <ul className="knowledge-list">
          {knowledge.map((item, idx) => (
            <li className="knowledge-item" key={idx}>
              <p className="q-text">Q: {item.question}</p>
              <p className="a-text">A: {item.answer}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default KnowledgeBase;