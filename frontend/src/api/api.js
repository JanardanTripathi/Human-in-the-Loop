const API_BASE = "http://127.0.0.1:8000";

export async function fetchRequests() {
  const res = await fetch(`${API_BASE}/requests/`);
  if (!res.ok) throw new Error("Failed to fetch requests");
  return res.json();
}

export async function respondToRequest(request_id, answer) {
  const res = await fetch(`${API_BASE}/supervisor/respond`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ request_id, answer }),
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`Failed to send response: ${text}`);
  }
  return res.json();
}

export async function fetchKnowledgeBase() {
  const res = await fetch(`${API_BASE}/knowledge/`);
  if (!res.ok) throw new Error("Failed to fetch knowledge base");
  return res.json();
}