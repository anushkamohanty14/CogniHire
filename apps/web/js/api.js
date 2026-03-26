const API_BASE = '/api';

// Get/set user ID from localStorage
function getUserId() {
  return localStorage.getItem('cognihire_user_id') || '';
}
function setUserId(id) {
  localStorage.setItem('cognihire_user_id', id);
}

// Generic fetch wrapper
async function apiGet(path) {
  const res = await fetch(API_BASE + path);
  if (!res.ok) throw new Error(`API error: ${res.status}`);
  return res.json();
}

async function apiPost(path, body) {
  const res = await fetch(API_BASE + path, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(body)
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || `API error: ${res.status}`);
  }
  return res.json();
}

async function apiPostForm(path, formData) {
  const res = await fetch(API_BASE + path, {method: 'POST', body: formData});
  if (!res.ok) throw new Error(`API error: ${res.status}`);
  return res.json();
}
