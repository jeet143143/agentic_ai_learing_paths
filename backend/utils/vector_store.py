from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv
import json, os

load_dotenv()

def get_vector_store():
    with open('backend/data/learning_content.json') as f:
        content = json.load(f)
    texts = [c['text'] for c in content]
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    db = FAISS.from_texts(texts, embeddings)
    return db