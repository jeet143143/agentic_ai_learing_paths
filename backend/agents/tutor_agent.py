from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(temperature=0.3, openai_api_key=os.getenv("OPENAI_API_KEY"))

def get_tutoring_response(question):
    prompt = PromptTemplate.from_template(
        "You are a helpful tutor. Answer this student query: {question}"
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    return {"response": chain.run(question=question)}