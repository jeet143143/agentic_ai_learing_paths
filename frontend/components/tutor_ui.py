import streamlit as st
import requests

def show_tutor_ui():
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    st.header("🧐 Tutor Assistant")
    question = st.text_input("❓ Ask a study-related question")

    if st.button("Get Answer") and question:
        try:
            res = requests.post("https://agentic-backend-n9ha.onrender.com/tutor", json={"question": question})
            if res.status_code == 200:
                st.success("✅ Answer received")
                st.markdown(res.json()['response'])
            else:
                st.error("❌ Failed to get answer")
        except Exception as e:
            st.error(f"Error: {e}")

    st.markdown("</div>", unsafe_allow_html=True)
