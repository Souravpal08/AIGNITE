import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

from dotenv import load_dotenv
load_dotenv()  # Loading all the environment variables

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Custom CSS for advanced styling
st.markdown("""
    <style>
    body {
        background: radial-gradient(circle, #1a2a3a, #000000); /* Darker theme with gradient */
        font-family: 'Arial', sans-serif;
        color: #ECF0F1;
    }

    .main {
        background-color: #181a20b3;
        max-width: 800px;
        max-height: 80%;
        margin: auto auto;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.4);
        transition: background-color 0.5s ease;
    }

    .main:hover {
        background-color: #414d5ac9;
    }

    .stHeader {
        color: #c9f4ff;
        font-size: 45px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 4px 3px 6px #0000005c;
    }

    .stTextInput > div > input {
        font-size: 18px;
        padding: 15px;
        width: 100%;
        border-radius: 8px;
        border: 1px solid #ccc;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
        background-color: #2C3E50;
        color: #ECF0F1;
    }

    .stTextInput input:focus {
        border-color: #1abc9c;
    }

    .stFileUploader {
        margin-bottom: 20px;
    }

    .stButton button {
        background-color: #1abc9c;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        box-shadow: 0px 4px 10px rgba(26, 188, 156, 0.3);
        transition: all 0.3s ease;
    }

    .stButton button:hover {
        background-color: #16a085;
        transform: translateY(-2px);
    }

    .stSubheader {
        color: #ECF0F1;
        font-size: 36px;
        font-weight: 700;
        margin-top: 30px;
        text-align: center;
    }

    .stMarkdown {
        text-align: center;
        font-size: 16px;
        margin-top: 10px;
        color: #ECF0F1;
    }

    .char-counter {
        text-align: right;
        font-size: 14px;
        color: #95a5a6;
    }

    footer {
        text-align: center;
        margin-top: 40px;
        font-size: 14px;
        color: #BDC3C7;
    }
    </style>
""", unsafe_allow_html=True)

# Page header
st.markdown('<h1 class="stHeader">CURECANAI CHATBOT</h1>', unsafe_allow_html=True)
st.write("Welcome to CureCancAI Chatbot, a helping hand for your queries.")

# User input section
input = st.text_input("Enter a prompt ", key="input", placeholder="Type your prompt here...")

# Image upload section
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.markdown('<p class="caption">Uploaded Image</p>', unsafe_allow_html=True)

# Submit button
submit = st.button("Generate the content")

# Response section
if submit:
    with st.spinner("Generating response..."):
        response = get_gemini_response(input, image)
    st.markdown('<h2 class="stSubheader">Gemini Response:</h2>', unsafe_allow_html=True)
    st.markdown(response, unsafe_allow_html=True)

# Footer
st.markdown('<footer>Powered by Gemini LLM</footer>', unsafe_allow_html=True)
