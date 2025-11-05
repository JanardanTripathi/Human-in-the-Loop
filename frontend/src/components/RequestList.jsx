import React from "react";

const RequestList = ({ requests, onSelect }) => {
  return (
    <div className="card">
      <h2>Help Requests</h2>
      {(!requests || requests.length === 0) ? (
        <p className="empty-state">No requests found.</p>
      ) : (
        <ul className="request-list">
          {requests.map((req) => (
            <li
              key={req.id}
              className={`request-item ${req.status === "resolved" ? "resolved" : ""}`}
              onClick={() => onSelect(req)}
            >
              <p className="q">{req.question}</p>
              <p className="meta">Status: {req.status} • Customer: {req.customer_id}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default RequestList;