import streamlit as st
import requests

def show_plan_ui():
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    st.header("📘 Personalized Plan")
    goal = st.text_input("🎯 What's your learning goal?")

    if st.button("Generate Plan") and goal:
        try:
            res = requests.post("http://localhost:8000/plan", json={"goal": goal})
            if res.status_code == 200:
                st.success("✅ Plan Generated Successfully")
                st.code(res.json()['plan'], language='markdown')
            else:
                st.error("❌ Failed to get plan")
        except Exception as e:
            st.error(f"Error: {e}")

    st.markdown("</div>", unsafe_allow_html=True)