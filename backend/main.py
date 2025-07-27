from fastapi import FastAPI, Request
from backend.agents.planner_agent import get_learning_plan
from backend.agents.tutor_agent import get_tutoring_response
from dotenv import load_dotenv
import os

load_dotenv()
print("OpenAI Key Loaded:", os.getenv("OPENAI_API_KEY"))

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "Agentic AI API is running"}

@app.post("/plan")
async def plan_route(request: Request):
    body = await request.json()
    return get_learning_plan(body["goal"])

@app.post("/tutor")
async def tutor_route(request: Request):
    body = await request.json()
    return get_tutoring_response(body["question"])