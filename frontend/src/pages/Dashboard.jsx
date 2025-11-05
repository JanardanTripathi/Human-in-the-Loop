import React, { useEffect, useState } from "react";
import { fetchRequests, respondToRequest, fetchKnowledgeBase } from "../api/api";
import RequestList from "../components/RequestList";
import RequestForm from "../components/RequestForm";
import KnowledgeBase from "../components/KnowledgeBase";

const Dashboard = () => {
  const [requests, setRequests] = useState([]);
  const [selected, setSelected] = useState(null);
  const [knowledge, setKnowledge] = useState([]); 
  const [feedback, setFeedback] = useState(null);

  const loadData = async () => {
    try {
      const [reqData, kbData] = await Promise.all([fetchRequests(), fetchKnowledgeBase()]);
      setRequests(reqData || []);
      setKnowledge(kbData || []); 
    } catch (err) {
      console.error("Error loading data:", err);
      setFeedback("Failed to load data from backend.");
    }
  };

  useEffect(() => {
    loadData();
    const interval = setInterval(loadData, 8000);
    return () => clearInterval(interval);
  }, []);

  const handleRespond = async (request_id, answer) => {
    try {
      await respondToRequest(request_id, answer);
      setFeedback("Response submitted successfully!");
      setSelected(null);
      await loadData();
      setTimeout(() => setFeedback(null), 2500);
    } catch (err) {
      console.error(err);
      setFeedback("Failed to submit response.");
      setTimeout(() => setFeedback(null), 3000);
    }
  };

  return (
    <div className="app-container">
      <div className="app-header">
        <h1 className="app-title">Supervisor Dashboard</h1>
      </div>

      <div className="dashboard-grid">
        <RequestList requests={requests} onSelect={setSelected} />
        <RequestForm selected={selected} onRespond={handleRespond} />
        <KnowledgeBase knowledge={knowledge} />
      </div>

      {feedback && <div className="feedback">{feedback}</div>}
    </div>
  );
};

export default Dashboard;