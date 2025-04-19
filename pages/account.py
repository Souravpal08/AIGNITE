import streamlit as st
import pyrebase
import firebase_admin
from firebase_admin import credentials
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def add_custom_css():
    st.markdown("""
        <style>
        /* Background color */
        body {
            background-color: #1e1e1e;
            color: #dcdcdc;
        }
        /* Text input styles */
        input {
            background-color: #333333;
            color: #ffffff;
            border: 1px solid #444444;
            padding: 8px;
        }
        /* Header styles */
        h1, h2, h3, h4, h5, h6 {
            color: #d4af37; /* Gold-like color for headers */
        }
        /* Subheader style */
        .stMarkdown h2 {
            font-size: 1.8em;
            color: #ffcc00; /* Yellowish color */
        }
        /* Button style */
        div.stButton button {
            background-color: #008CBA;
            color: white;
            border-radius: 8px;
            border: none;
            padding: 10px 20px;
            font-size: 1em;
            transition: background-color 0.3s ease;
        }
        div.stButton button:hover {
            background-color: #005f7a;
        }
        /* Balloons style */
        .balloon-container {
            background-color: #1e1e1e;
        }
        /* Selectbox style */
        select {
            background-color: #333333;
            color: #ffffff;
            border: 1px solid #444444;
        }
        </style>
    """, unsafe_allow_html=True)

add_custom_css()

# Firebase admin setup for other Firebase services (not used for auth in this case)
# if not firebase_admin._apps:
#     cred = credentials.Certificate("curecanai-bbfffde990d3.json")
#     firebase_admin.initialize_app(cred)

# Pyrebase configuration for authentication
firebaseConfig = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
    "measurementId": os.getenv("FIREBASE_MEASUREMENT_ID")
}

# Initialize Pyrebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

st.title("CureCancAI - Account Page")
add_custom_css()

# Initialize session state variables if they don't exist
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = ""
if 'useremail' not in st.session_state:
    st.session_state['useremail'] = ""

# Function to handle login
def login(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        st.session_state['useremail'] = user['email']
        st.session_state['logged_in'] = True
        st.success(f"Welcome, {user['email']}!")
    except Exception as e:
        st.error(f"Login failed: {e}")

# Function to handle signup
def signup(username, email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        st.session_state['username'] = username
        st.session_state['useremail'] = user['email']
        st.session_state['logged_in'] = True
        st.balloons()
        st.success("Signup successful")
    except Exception as e:
        st.error(f"Signup failed: {e}")

# Function to handle logout
def logout():
    st.session_state.clear()
    st.session_state['logged_in'] = False

# Display user info after login/signup
if st.session_state['logged_in']:
    st.markdown("<h2 style='color: #d4af37;'>Welcome to your account</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #dcdcdc; font-size: 1.2em;'>Username: <strong style='color: #ffcc00;'>{st.session_state['username']}</strong></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #dcdcdc; font-size: 1.2em;'>Email: <strong style='color: #ffcc00;'>{st.session_state['useremail']}</strong></p>", unsafe_allow_html=True)
    st.markdown("<p style='color: #dcdcdc; font-size: 1.2em;'>You have successfully logged in or signed up.</p>", unsafe_allow_html=True)
    
    if st.button("Sign Out"):
        logout()

# Login/Signup form for users who are not signed in
else:
    login_signup_choice = st.selectbox("Choose an option", ["Login", "Sign Up"])

    if login_signup_choice == "Login":
        st.subheader("Login to your account")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            login(email, password)

    elif login_signup_choice == "Sign Up":
        st.subheader("Create a new account")
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Sign Up"):
            signup(username, email, password)
