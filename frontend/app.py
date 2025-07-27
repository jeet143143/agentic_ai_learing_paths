import streamlit as st
from components.plan_ui import show_plan_ui
from components.tutor_ui import show_tutor_ui
from streamlit_lottie import st_lottie
import json
import os

st.set_page_config(page_title="Agentic AI", layout="wide")

def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "styles", "custom.css")
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def load_local_lottie(path):
    with open(path, "r") as f:
        return json.load(f)

load_css()

# Load Lottie animations
logo_anim = load_local_lottie("lottie/logo.json")
tutor_anim = load_local_lottie("lottie/tutor.json")
plan_anim = load_local_lottie("lottie/plan.json")

st.sidebar.image("images/agentic_logo.png", width=150)

st.markdown("<h1>Agentic AI for Personalized Learning Paths</h1>", unsafe_allow_html=True)

query_params = st.query_params.to_dict()
page = query_params.get("page", "home")

if page == "home":
    st.markdown("<div class='container'>", unsafe_allow_html=True)

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st_lottie(tutor_anim, height=150)
            st.markdown("""
            <div class='card'>
                <h3>📘 Tutor</h3>
                <p>AI-powered tutoring to answer your questions and give real-time feedback.</p>
                <a href='?page=tutor'><button>Go to Tutor</button></a>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st_lottie(plan_anim, height=150)
            st.markdown("""
            <div class='card'>
                <h3>📚 Personalized Plan</h3>
                <p>Get a study plan tailored to your learning pace and goals.</p>
                <a href='?page=plan'><button>Go to Plan</button></a>
            </div>
            """, unsafe_allow_html=True)

    with st.container():
        st.markdown("""
        <div class='card'>
            <h3>🧪 Assessment Solver</h3>
            <p>Instant solutions and evaluation modules to assess your skills.</p>
            <div class='soon'>⚡ Coming Soon</div>
        </div>
        <div class='card'>
            <h3>🎯 Recommendation</h3>
            <p>Smart suggestions based on your learning journey.</p>
            <div class='soon'>⚡ Coming Soon</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

elif page == "plan":
    show_plan_ui()
    st.markdown("<a class='back-button' href='?page=home'>← Back to Home</a>", unsafe_allow_html=True)
elif page == "tutor":
    show_tutor_ui()
    st.markdown("<a class='back-button' href='?page=home'>← Back to Home</a>", unsafe_allow_html=True)
