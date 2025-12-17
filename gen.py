import streamlit as st
import google.generativeai as genai
st.title("google.generativeai with Streamlit")
st.write("my app")
user_input = st.text_input("Enter your prompt")
genai.configure(api_key="AIzaSyCOMfLO14-FfzkkTLzTAyc_qiG6OkWSWAQ")  
model = genai.GenerativeModel("models/gemini-2.5-flash")
if user_input:
response = model.generate_content(user_input)
st.write(response.text)