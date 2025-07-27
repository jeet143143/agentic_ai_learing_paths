# Agentic AI for Personalized Education Paths

### 👤 Created by: Jeet Senapati

---

## 🚀 Project Overview
**Agentic AI** is an intelligent, agent-based education system that offers:
- AI-powered tutoring support
- Personalized learning path generation
- Future modules: assessments and content recommendations

It uses **Streamlit** as the frontend with **animated UI**, and Python FastAPI as backend (expected) for handling tutoring and planning logic.

The core principle is based on **Agentic AI**: where AI agents reason, plan, and act autonomously to personalize learning experiences for each user.

---

## 🧠 How It Works
1. **Home Interface**: Clean dashboard with 4 cards – Tutor, Plan, Assessment, Recommendation
2. **Tutor Section**: Ask questions and get AI-generated answers using a backend API
3. **Plan Section**: Enter your learning goals and get a tailored study roadmap
4. **Assessment & Recommendation**: Coming Soon modules

Back navigation and animations provide a smooth and interactive UX.

---

## 🛠️ Setup Instructions

### 🔧 Requirements:
- Python 3.9+
- pip

### 📦 Install Dependencies
```bash
pip install streamlit streamlit-lottie requests
```

### 📁 Folder Structure
```
agentic-edu-in/
├── frontend/
│   ├── app.py
│   ├── styles/
│   │   └── custom.css
│   ├── components/
│   │   ├── tutor_ui.py
│   │   └── plan_ui.py
│   ├── lottie/
│   │   ├── tutor.json
│   │   ├── plan.json
│   │   └── logo.json
│   └── images/
│       └── agentic_logo.png
```

### ▶️ Run the Project
```bash
cd frontend
streamlit run app.py
```

Make sure your backend is running at `http://localhost:8000` for `/plan` and `/tutor` routes.

---

## 🌟 Credits
Created by **Jeet Senapati** with a focus on AI-driven personalized learning and an animated, modern UI using Lottie and Streamlit.
