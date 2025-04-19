import streamlit.components.v1 as components

components.html(
    """
    <div style="border: 2px solid #fff; border-radius: 10px; padding: 10px; border-radius: 10px; background-color: #fff; height: 100%;">
        <iframe 
            src="https://www.chatbase.co/chatbot-iframe/kphq_g1RlH3TcsGvwEJvD"
            width="100%" 
            height="600" 
            style="border:none;">
        </iframe>
    </div>
    """,
    height=650
)