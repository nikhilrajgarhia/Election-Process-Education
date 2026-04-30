# Election Process Assistant 🗳️

The **Election Process Assistant** is an interactive, AI-powered tool designed to simplify the voting process. It helps users understand election timelines, registration steps, and polling requirements based on their specific jurisdiction, voter profile, and preferred voting method.

## 🚀 Key Features

- **Dynamic Voter Plans**: Generates a step-by-step timeline tailored to your location (US, India, UK) and persona (First-time voter, Student, Overseas, etc.).
- **AI-Powered Assistant**: Integrated with **Google Gemini 1.5 Flash** to answer natural language questions about the election process with context-aware accuracy.
- **State Persistence**: Remembers your selected settings and checklist progress even after refreshing the page or closing the browser.
- **Modern Architecture**: Refactored into a clean, modular structure using **FastAPI** for the backend and a responsive Vanilla JS/CSS frontend.
- **Docker Ready**: Fully containerized and optimized for deployment on platforms like **Google Cloud Run**.

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
