from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY"))

def get_learning_plan(goal):
    prompt = PromptTemplate.from_template(
        "Create a personalized learning plan for a student who wants to {goal} in 2 months."
    )
    response = llm.predict(prompt.format(goal=goal))
    return {"plan": response}