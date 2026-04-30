const state = {
  jurisdiction: "us",
  persona: "first-time",
  method: "in-person",
  completed: new Set()
};

const $ = (selector) => document.querySelector(selector);
const timeline = $("#timeline");
const completed = $("#completed");
const chatLog = $("#chat-log");

// --- State Persistence ---

function saveState() {
  const data = {
    ...state,
    completed: Array.from(state.completed)
  };
  localStorage.setItem("election_assistant_state", JSON.stringify(data));
}

function loadState() {
  const saved = localStorage.getItem("election_assistant_state");
  if (!saved) return;
  try {
    const data = JSON.parse(saved);
    state.jurisdiction = data.jurisdiction || "us";
    state.persona = data.persona || "first-time";
    state.method = data.method || "in-person";
    state.completed = new Set(data.completed || []);

    // Sync UI elements
    const fields = ["jurisdiction", "persona", "method"];
    fields.forEach(id => {
      const el = $(`#${id}`);
      if (el) el.value = state[id];
    });
  } catch (e) {
    console.error("Failed to load state", e);
  }
}

// --- API Interactions ---

async function postJson(path, body) {
  const response = await fetch(path, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body)
  });
  if (!response.ok) throw new Error("Request failed");
  return response.json();
}

function payload() {
  return {
    jurisdiction: state.jurisdiction,
    persona: state.persona,
    method: state.method,
    completed: Array.from(state.completed)
  };
}

async function renderPlan() {
  const plan = await postJson("/api/plan", payload());
  $("#plan-title").textContent = `${plan.jurisdiction.name} timeline`;
  $("#plan-summary").textContent = `${plan.persona} planning to vote by ${plan.method.toLowerCase()}.`;
  $("#source").innerHTML = `${plan.jurisdiction.note}<br><a href="${plan.jurisdiction.source}" target="_blank" rel="noreferrer">Open official source</a>`;

  timeline.innerHTML = "";
  completed.innerHTML = "";

  for (const step of plan.steps) {
    const row = document.createElement("article");
    row.className = `step ${step.status}`;
    row.innerHTML = `
      <div class="badge">${step.status === "done" ? "✓" : step.number}</div>
      <div>
        <div class="meta">
          <span class="pill">${step.phase}</span>
          <span class="pill">${step.when}</span>
        </div>
        <h3>${step.title}</h3>
        <p>${step.details}</p>
        <p><strong>Next action:</strong> ${step.action}</p>
      </div>
    `;
    timeline.appendChild(row);

    const label = document.createElement("label");
    label.className = "check";
    label.innerHTML = `<input type="checkbox" ${state.completed.has(step.title) ? "checked" : ""}> <span>${step.title}</span>`;
    label.querySelector("input").addEventListener("change", (event) => {
      if (event.target.checked) {
        state.completed.add(step.title);
      } else {
        state.completed.delete(step.title);
      }
      saveState();
      renderPlan();
    });
    completed.appendChild(label);
  }

  $("#tips").innerHTML = plan.tips.length
    ? plan.tips.map((tip) => `<li>${tip}</li>`).join("")
    : "<li>Confirm every deadline with the official election office before acting.</li>";
  
  saveState();
}

function addMessage(text, role, source) {
  const item = document.createElement("div");
  item.className = `message ${role}`;
  item.innerHTML = source ? `${text}<br><br><small>Source: <a href="${source}" target="_blank" rel="noreferrer">${source}</a></small>` : text;
  chatLog.appendChild(item);
  chatLog.scrollTop = chatLog.scrollHeight;
}

async function ask(question) {
  const clean = question.trim();
  if (!clean) return;
  addMessage(clean, "user");
  const response = await postJson("/api/ask", { ...payload(), question: clean });
  addMessage(`${response.answer}<br><br>${response.note || ""}`, "assistant", response.source);
}

// --- Event Listeners ---

for (const id of ["jurisdiction", "persona", "method"]) {
  const el = $(`#${id}`);
  if (el) {
    el.addEventListener("change", (event) => {
      state[id] = event.target.value;
      state.completed.clear();
      saveState();
      renderPlan();
    });
  }
}

const resetBtn = $("#reset");
if (resetBtn) {
  resetBtn.addEventListener("click", () => {
    state.completed.clear();
    saveState();
    renderPlan();
  });
}

const chatForm = $("#chat-form");
if (chatForm) {
  chatForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const input = $("#question");
    ask(input.value);
    input.value = "";
  });
}

document.querySelectorAll(".quick button").forEach((button) => {
  button.addEventListener("click", () => ask(button.dataset.question));
});

// --- Initialization ---

loadState();
renderPlan();
addMessage("Tell me where you are voting and what you need help with. I will explain the process step by step and point you to official sources for exact rules.", "assistant");
