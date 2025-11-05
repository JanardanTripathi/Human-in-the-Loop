import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import AIChat from "./pages/AIChat";

const App = () => {
  return (
    <Router>
      <nav style={styles.navbar}>
        <h2 style={styles.title}>Human-in-the-Loop AI</h2>
        <div>
          <Link to="/" style={styles.link}>Dashboard</Link>
          <Link to="/chat" style={styles.link}>AI Interaction</Link>
        </div>
      </nav>

      <div style={styles.container}>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/chat" element={<AIChat />} />
        </Routes>
      </div>
    </Router>
  );
};

const styles = {
  navbar: {
    backgroundColor: "#2b6cb0",
    padding: "10px 20px",
    color: "#fff",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
  },
  title: {
    margin: 0,
    fontSize: "20px",
  },
  link: {
    color: "#fff",
    marginLeft: "20px",
    textDecoration: "none",
    fontWeight: "bold",
  },
  container: {
    padding: "20px",
  },
};

export default App;