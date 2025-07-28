from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.agents.planner_agent import get_learning_plan
from backend.agents.tutor_agent import get_tutoring_response
from backend.utils import load_dotenv
import os

load_dotenv()
print("OpenAI Key Loaded:", os.getenv("OPENAI_API_KEY"))

app = FastAPI()

# Add this middleware for CORS support
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace * with frontend domain for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
