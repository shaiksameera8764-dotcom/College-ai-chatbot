import streamlit as st

st.title("College AI Chatbot")
st.write("AIML 2nd Year Project")

q = st.text_input("Question adugu:")

if q:
    st.success("Nee question: " + q)
