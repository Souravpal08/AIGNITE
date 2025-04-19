import streamlit as st

st.title("Frequently Asked Questions (FAQs)")

faqs = {
    "What is this cancer detection system?": "This is an AI-powered system designed to detect cancer from input data like images or other test results.",

    "How does the AI model work?": "Our AI model uses advanced machine learning techniques to analyze medical data and make predictions about cancer detection. It has been trained on a large dataset of cancer cases.",

    "Is the cancer detection accurate?": "While our system strives to be as accurate as possible, it should not be used as a replacement for professional medical diagnosis. Always consult a doctor for a comprehensive diagnosis.",

    "What kind of data is used for cancer detection?": "Our system uses data such as images (e.g., X-rays or CT scans) and other test results for analysis.",

    "Is my data secure completely?": "Yes, we prioritize data security. All user data is encrypted and stored securely in compliance with privacy regulations.",

    "Can this system detect all types of cancer?": "Currently, the system focuses on specific types of cancer, but we are continually working to expand its capabilities.",

    "How often should I use this system?": "Consult with your healthcare provider for personalized recommendations on the frequency of use.",

    "What are the limitations of this system?": "This system is not a definitive diagnostic tool. It may not detect all cases of cancer, and false positives or negatives are possible.",

    "Can I use this system for self-diagnosis?": "No, this system is not intended for self-diagnosis. Always consult a doctor for any health concerns.",

    "How can I contribute to improving this system?": "You can help by providing feedback on your experience and sharing any relevant medical data with our research team."
}

for question, answer in faqs.items():
    with st.expander(question):
        st.write(answer)