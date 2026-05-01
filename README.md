# Election Process Assistant 🗳️

The **Election Process Assistant** is an interactive, AI-powered tool designed to simplify the voting process. It helps users understand election timelines, registration steps, and polling requirements based on their specific jurisdiction, voter profile, and preferred voting method.

## 🎯 Chosen Vertical
**Civic Engagement & Election Education**: This solution addresses the "information gap" in democratic processes by translating complex, jurisdiction-specific election rules into actionable, personalized tasks.

## 🧠 Approach & Logic
The application follows a **"Guide-First, AI-Enhanced"** philosophy:
1.  **Guided Logic**: Uses a deterministic rule engine (`data.py`) to generate reliable timelines based on the user's location, persona, and voting method. This ensures that core legal requirements are always accurate.
2.  **AI Fallback**: Integrates **Gemini 1.5 Flash** as a dynamic layer. If a user asks a question outside the predefined steps, the AI provides context-aware answers, citing official sources and the specific jurisdiction context.
3.  **Real-Time Data**: Integrates the **Google Civic Information API** to supplement general guides with exact polling locations and ballot details for US addresses.

## ⚙️ How it Works
1.  **Onboarding**: The user selects their jurisdiction and voter profile (e.g., "Student" or "Overseas").
2.  **Dynamic Timeline**: The system generates a custom checklist. For example, a student voting in the US sees specific steps for campus registration.
3.  **Persistence**: Using `localStorage`, the app remembers the user's progress. A voter can mark steps as "Done" and return later to see the next task.
4.  **AI Chat**: Users can ask natural language questions (e.g., "Do I need a passport to vote in India?"). The AI analyzes the `JURISDICTIONS` data and the user's current plan to provide a tailored response.

## 📝 Assumptions Made
- **Official Priority**: The app assumes that the "Official Source" links provided are the final authority for any legal or deadline-related disputes.
- **Connectivity**: Assumes a stable internet connection for AI interactions and Civic API lookups.
- **US Coverage**: Real-time polling place lookup via the Civic Information API is primarily optimized for US-based addresses.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.11, FastAPI, Uvicorn, Jinja2
- **Frontend**: Vanilla JavaScript, CSS3 (Modern HSL-based design)
- **AI**: Google Generative AI (Gemini API)
- **DevOps**: Docker, Google Cloud Run

---

## 🏃 Getting Started

### Prerequisites

- Python 3.11+
- A Google Gemini API Key (Get one at [AI Studio](https://aistudio.google.com/))

### Running Locally

1. **Clone the repository:**
   ```bash
   git clone git@github.com:nikhilrajgarhia/Election-Process-Education.git
   cd Election-Process-Education
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your API Key:**
   ```bash
   export GEMINI_API_KEY="your_api_key_here"
   ```

4. **Start the application:**
   ```bash
   python main.py
   ```
   The app will be live at `http://localhost:8000`.

### Running with Docker

1. **Build the image:**
   ```bash
   docker build -t election-assistant .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8000:8080 -e GEMINI_API_KEY="your_api_key_here" election-assistant
   ```
   Access the app at `http://localhost:8000`.

---

## 📁 Project Structure

```text
.
├── main.py             # FastAPI application and routes
├── data.py             # Static election data and FAQ logic
├── static/
│   ├── style.css       # Premium CSS design
│   └── app.js          # Frontend logic and state management
├── templates/
│   └── index.html      # Main application structure
├── Dockerfile          # Container configuration
└── requirements.txt    # Project dependencies
```

## 🤝 Contributing

Contributions are welcome! Whether it's adding new jurisdictions, improving the AI prompts, or enhancing the UI, feel free to open a PR.

---

## ⚖️ Disclaimer

*This tool provides information based on official sources but is not an official government application. Always verify deadlines and rules with your local election office.*
