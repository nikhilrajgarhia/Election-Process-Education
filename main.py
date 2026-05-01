import os
import json
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import google.generativeai as genai
from pydantic import BaseModel
from typing import List, Set, Optional

from data import JURISDICTIONS, PERSONAS, FAQ

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure Gemini
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
CIVIC_INFO_API_KEY = os.environ.get("CIVIC_INFO_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    model = None

templates = Jinja2Templates(directory="templates")

class PlanRequest(BaseModel):
    jurisdiction: str
    persona: str
    method: str
    completed: List[str]

class QuestionRequest(BaseModel):
    jurisdiction: str
    persona: str
    method: str
    completed: List[str]
    question: str

def build_plan_logic(payload: PlanRequest):
    jurisdiction_id = payload.jurisdiction
    persona_id = payload.persona
    voting_method = payload.method
    completed = set(payload.completed)
    jurisdiction = JURISDICTIONS.get(jurisdiction_id, JURISDICTIONS["us"])

    steps = []
    for index, step in enumerate(jurisdiction["steps"], start=1):
        status = "done" if step["title"] in completed else "todo"
        if status == "todo" and not any(item["status"] == "current" for item in steps):
            status = "current"
        steps.append({**step, "number": index, "status": status})

    extra = []
    if persona_id == "first-time":
        extra.append("Save a copy or screenshot of each confirmation page until the election is complete.")
    if persona_id == "student":
        extra.append("Check whether you should register at your campus address or home address; rules differ by location.")
    if persona_id in {"mail", "overseas"} or voting_method in {"mail", "postal", "absentee"}:
        extra.append("Build in mailing time. Request, complete, sign, and return ballots earlier than the final deadline.")
    if voting_method == "in-person":
        extra.append("Check polling place, hours, accessibility options, and ID rules shortly before voting.")

    return {
        "jurisdiction": jurisdiction,
        "persona": PERSONAS.get(persona_id, "Voter"),
        "method": voting_method.replace("-", " ").title(),
        "steps": steps,
        "tips": extra,
    }

def answer_question_logic(payload: QuestionRequest):
    question = payload.question.strip()
    jurisdiction = JURISDICTIONS.get(payload.jurisdiction, JURISDICTIONS["us"])
    
    if not question:
        return {
            "answer": "Ask about registration, deadlines, ID, voting methods, polling places, counting, or results.",
            "source": jurisdiction["source"],
        }

    # Use Gemini if API key is available
    if model:
        try:
            prompt = f"""
            You are a helpful Election Process Assistant. Your goal is to help users understand how to vote in {jurisdiction['name']}.
            
            Use the following context as your primary source of truth:
            - Jurisdiction: {jurisdiction['name']}
            - Official Source: {jurisdiction['source']}
            - Important Note: {jurisdiction['note']}
            - Core Steps: {json.dumps(jurisdiction['steps'], indent=2)}
            
            Guidelines:
            1. Only provide information related to the election process in {jurisdiction['name']}.
            2. If the user asks about deadlines or specific local rules not in the context, refer them to the official source: {jurisdiction['source']}.
            3. Be concise, encouraging, and clear.
            4. Use simple language for first-time voters.
            5. If you don't know the answer, say "I'm not sure about that specific detail. Please check the official source at {jurisdiction['source']} for the most accurate and up-to-date information."
            
            User Question: {question}
            """
            response = model.generate_content(prompt)
            return {
                "answer": response.text,
                "source": jurisdiction["source"],
                "sourceName": jurisdiction["name"],
                "note": jurisdiction["note"],
            }
        except Exception as e:
            print(f"Gemini Error: {e}")
            # Fall through to keyword logic on error

    # Fallback: Keyword matching logic (original)
    normalized = question.lower()
    matched = None
    for item in FAQ:
        if any(keyword in normalized for keyword in item["keywords"]):
            matched = item
            break

    if matched:
        answer = matched["answer"]
    else:
        answer = (
            "I can help break the process into steps: confirm eligibility, register or update details, verify your voter record, "
            "choose a voting method, prepare documents, cast your ballot, and follow official results. For exact rules, use the official source linked here."
        )

    return {
        "answer": answer,
        "source": jurisdiction["source"],
        "sourceName": jurisdiction["name"],
        "note": jurisdiction["note"],
    }

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.post("/api/plan")
async def get_plan(payload: PlanRequest):
    return build_plan_logic(payload)

class LookupRequest(BaseModel):
    address: str

@app.post("/api/lookup")
async def lookup_address(payload: LookupRequest):
    if not CIVIC_INFO_API_KEY:
        return {"error": "Civic Information API Key not configured."}
    
    url = "https://www.googleapis.com/civicinfo/v2/voterinfo"
    params = {
        "address": payload.address,
        "key": CIVIC_INFO_API_KEY
    }
    
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url, params=params)
            resp.raise_for_status()
            return resp.json()
        except httpx.HTTPStatusError as e:
            return {"error": f"API Error: {e.response.status_code}", "details": e.response.text}
        except Exception as e:
            return {"error": f"Connection Error: {str(e)}"}

@app.post("/api/ask")
async def ask_assistant(payload: QuestionRequest):
    return answer_question_logic(payload)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
