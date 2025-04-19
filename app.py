import streamlit as st
import base64

# Define your pages
account_page = st.Page(
    page="pages/account.py",
    title="Account Page",
    icon=":material/account_circle:",
    default=True
)
home_page = st.Page(
    page="pages/home.py",
    title="Home Page",
    icon=":material/home:"
)
dashboard_page = st.Page(
    page="pages/dashboard.py",
    title="Dashboard",
    icon=":material/bar_chart:",
)
chatbot_page = st.Page(
    page="pages/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:"
)
blogs_page = st.Page(
    page="pages/blogs.py",
    title="Blogs",
    icon=":material/library_books:"
)
faqs_page = st.Page(
    page="pages/faqs.py",
    title="FAQs",
    icon=":material/help:"
)

# Function to check if the user is logged in
def is_user_logged_in():
    return st.session_state.get('logged_in', False)

# If user is not logged in, force them to the account page
if not is_user_logged_in():
    st.sidebar.warning("Please login or sign up to access the app.")
    pg = st.navigation({"User": [account_page]})
else:
    pg = st.navigation(
        {
            "User": [account_page],
            "Activities": [home_page, dashboard_page, chatbot_page, blogs_page, faqs_page]
        }
    )

# Shared across all pages
st.sidebar.title("CureCancAI")
st.sidebar.text("Made by ByteForce")

# Display the logo (optional)
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{encoded}"

image_base64 = get_base64_image("assets/logo.png")

st.sidebar.markdown(
    f"""
    <a href="/" target="_self">
        <img src="{image_base64}" width="80"  alt="logo">
    </a>
    """,
    unsafe_allow_html=True
)

# Run Navigation
pg.run()
