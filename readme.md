# 🤖 Agentic AI – Personalized Learning Path Generator

Agentic AI is an intelligent education assistant built using FastAPI (backend) and Streamlit (frontend). It helps users generate **personalized study plans** and get **tutor-style answers** to academic questions using AI.

---

## 🌐 Live Demo

🔗 Frontend URL: [https://agentic-ai-learing-paths.onrender.com](https://agentic-ai-learing-paths.onrender.com)

---

## 📦 Project Structure

```
agentic_ai_learing_paths/
├── backend/         # FastAPI-based backend with plan & tutor agents
│   ├── agents/
│   ├── rl/
│   ├── data/
│   ├── utils/
│   ├── main.py      # Main API server
│   └── ...
├── frontend/        # Streamlit-based frontend UI
│   ├── components/
│   │   ├── plan_ui.py
│   │   └── tutor_ui.py
│   ├── app.py       # Streamlit entry point
│   └── ...
```

---

## 🧠 Features

- ✨ Generate custom study plans based on your goals (e.g., "Prepare for GATE Exam")
- 🤓 Get tutor-style answers to academic questions ("What is a black hole?")
- ⚡ Backend powered by OpenAI and FastAPI
- 🎨 Interactive frontend UI using Streamlit

---

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI, OpenAI API
- **Frontend:** Streamlit, CSS
- **Deployment:** Render.com (both frontend & backend)

---

## 🚀 Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/agentic_ai_learing_paths.git
cd agentic_ai_learing_paths
```

### 2. Set Up Python Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Add `.env` File

Inside the `backend/` folder, create a `.env` file:

```env
OPENAI_API_KEY=your_openai_key_here
```

### 4. Run Backend

```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Run Frontend

Open a new terminal:

```bash
cd frontend
streamlit run app.py
```

---

## 🌍 Deployment Instructions (Render)

### Backend (FastAPI)

1. Connect GitHub repo to [Render](https://render.com)
2. Create a new Web Service
3. Environment:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn backend.main:app --host 0.0.0.0 --port 10000`
4. Add `OPENAI_API_KEY` in environment variables
5. Deploy

### Frontend (Streamlit)

1. Deploy `app.py` from `frontend/` as another web service
2. Update all URLs in `plan_ui.py` and `tutor_ui.py` to use backend Render link

---

## 📌 Known Improvements

- Add login/auth system
- Track user progress over time
- Support file upload for assignments
- Improve UI with animations

---

## 👨‍💻 Author

**Jeet Senapati**  
Email: senapatijeet2004@gmail.com  
Project: Agentic AI Learning Paths

---

