import streamlit as st
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

st.sidebar.markdown(
    f"""
    <style>
    .sidebar-bottom {{
        position: fixed;
        bottom: 20px;
        width: 100%;
        text-align: center;
    }}
    </style>

    <div class="sidebar-bottom">
        <h1 style="margin-bottom: 2px;">CureCancAI</h1>
        <p style="font-size: 15px; margin: 0;">Made by ByteForce</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Run Navigation
pg.run()
