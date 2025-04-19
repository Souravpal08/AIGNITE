import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from fpdf import FPDF
import base64
import os
from datetime import datetime

# Inject custom CSS to make the width 100%
def set_max_width():
    max_width_str = """
    <style>
    .main {
        max-width: 100%;
        padding-left: 5%;
        padding-right: 5%;
    }
    </style>
    """
    st.markdown(max_width_str, unsafe_allow_html=True)

# Load the model, scaler, and feature names
def load_model():
    model = joblib.load('model/model.pkl')
    scaler = joblib.load('model/scaler.pkl')
    feature_names = joblib.load('model/feature_names.pkl')
    return model, scaler, feature_names

# Input section
def get_user_input():
    st.header('Input Features')

    radius_mean = st.slider('Radius Mean', 0.0, 30.0, 14.0)
    texture_mean = st.slider('Texture Mean', 0.0, 40.0, 19.0)
    perimeter_mean = st.slider('Perimeter Mean', 0.0, 200.0, 90.0)
    area_mean = st.slider('Area Mean', 0.0, 2500.0, 700.0)
    smoothness_mean = st.slider('Smoothness Mean', 0.0, 0.2, 0.1)
    compactness_mean = st.slider('Compactness Mean', 0.0, 1.0, 0.2)
    concavity_mean = st.slider('Concavity Mean', 0.0, 1.0, 0.3)
    concave_points_mean = st.slider('Concave Points Mean', 0.0, 1.0, 0.2)
    symmetry_mean = st.slider('Symmetry Mean', 0.0, 1.0, 0.2)
    fractal_dimension_mean = st.slider('Fractal Dimension Mean', 0.0, 0.1, 0.05)
    radius_se = st.slider('Radius SE', 0.0, 5.0, 1.0)
    texture_se = st.slider('Texture SE', 0.0, 5.0, 1.0)

    user_data = {
        'radius_mean': radius_mean,
        'texture_mean': texture_mean,
        'perimeter_mean': perimeter_mean,
        'area_mean': area_mean,
        'smoothness_mean': smoothness_mean,
        'compactness_mean': compactness_mean,
        'concavity_mean': concavity_mean,
        'concave points_mean': concave_points_mean,
        'symmetry_mean': symmetry_mean,
        'fractal_dimension_mean': fractal_dimension_mean,
        'radius_se': radius_se,
        'texture_se': texture_se,
    }

    return pd.DataFrame(user_data, index=[0])

# Pie chart for prediction probability
def display_chart(probabilities):
    labels = ['Benign', 'Malignant']
    fig, ax = plt.subplots()
    ax.pie(probabilities, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#8fbc8f', '#f08080'])
    ax.axis('equal')
    st.pyplot(fig)

# PDF report generation
def generate_pdf(user_input, prediction, prediction_prob):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 20)
    pdf.cell(0, 15, "Breast Cancer Diagnostic Report", ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Date: {datetime.today().strftime('%B %d, %Y')}", ln=True)
    pdf.cell(0, 10, "Patient Name: _______________________________", ln=True)
    pdf.cell(0, 10, "Patient ID: _________________________________", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", "", 11)
    intro = (
        "This report presents the results of a machine learning-based diagnostic evaluation. "
        "The input data provided was analyzed using a trained classifier to assist in determining "
        "the likelihood of a tumor being malignant or benign. This tool is intended to support, not replace, "
        "clinical judgement."
    )
    pdf.multi_cell(0, 7, intro)

    pdf.ln(5)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 10, "Prediction Summary", ln=True)

    pdf.set_font("Arial", "", 12)
    pred_text = "Malignant" if prediction == 1 else "Benign"
    status_text = "High Risk - Malignant" if prediction == 1 else "Low Risk - Benign"
    pdf.cell(0, 10, f"Prediction Result: {status_text}", ln=True)
    pdf.cell(0, 10, f"Benign Probability: {prediction_prob[0]*100:.2f}%", ln=True)
    pdf.cell(0, 10, f"Malignant Probability: {prediction_prob[1]*100:.2f}%", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 10, "Medical Recommendation", ln=True)
    pdf.set_font("Arial", "", 11)
    recommendation = (
        "The model predicts that the tumor is likely malignant. It is strongly recommended that the patient "
        "consult an oncologist or a medical professional immediately for confirmatory testing such as a biopsy, "
        "MRI, or further clinical evaluation."
    ) if prediction == 1 else (
        "The model predicts that the tumor is likely benign. However, it is still recommended to follow up with "
        "a healthcare provider for further assessment and routine check-ups to rule out any anomalies."
    )
    pdf.multi_cell(0, 7, recommendation)

    pdf.ln(5)
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 10, "Input Feature Summary", ln=True)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(90, 8, "Feature", 1)
    pdf.cell(50, 8, "Value", 1, ln=True)

    pdf.set_font("Arial", "", 11)
    for col in user_input.columns:
        value = round(user_input[col].values[0], 4)
        feature = col.replace('_', ' ').capitalize()
        pdf.cell(90, 8, feature, 1)
        pdf.cell(50, 8, str(value), 1, ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", "I", 10)
    disclaimer = (
        "Disclaimer: This report is generated by an AI system and is not a substitute for professional medical advice, "
        "diagnosis, or treatment. Always seek the advice of a qualified healthcare provider."
    )
    pdf.multi_cell(0, 5, disclaimer)

    pdf_output_path = "report.pdf"
    pdf.output(pdf_output_path)
    return pdf_output_path

# Stylish download button
def get_download_button(base64_pdf):
    return f'''
    <div style="text-align: center; margin-top: 20px;">
        <a href="data:application/octet-stream;base64,{base64_pdf}" download="breast_cancer_report.pdf" 
           style="
               display: inline-block;
               padding: 12px 24px;
               font-size: 16px;
               font-weight: bold;
               color: #fff;
               background-color: #4CAF50;
               border-radius: 8px;
               text-decoration: none;
               transition: background-color 0.3s ease;
               box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
           "
           onmouseover="this.style.backgroundColor='#45a049';"
           onmouseout="this.style.backgroundColor='#4CAF50';">
           📄 Download Diagnostic Report
        </a>
    </div>
    '''

# Main app
def main():
    set_max_width()
    st.title("🩺 Breast Cancer Detection Dashboard")

    col1, col2 = st.columns([1, 1.5])
    model, scaler, feature_names = load_model()

    with col1:
        user_input = get_user_input()

    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)

        for feature in feature_names:
            if feature not in user_input.columns:
                user_input[feature] = 0

        user_input = user_input[feature_names]
        user_input_scaled = scaler.transform(user_input)

        if st.button('Predict'):
            prediction = model.predict(user_input_scaled)[0]
            prediction_prob = model.predict_proba(user_input_scaled)[0]

            if prediction == 1:
                st.markdown("<h2 style='color: red;'>The prediction is: Malignant</h2>", unsafe_allow_html=True)
                st.markdown("""
                <div style='background-color: #f8d7da; padding: 10px; border-radius: 5px; color: black;'>
                    <p><strong>Description:</strong> The model predicts that the tumor is <strong>malignant</strong>. Malignant tumors are cancerous and can spread.</p>
                    <p>Consult with a healthcare professional immediately.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("<h2 style='color: green;'>The prediction is: Benign</h2>", unsafe_allow_html=True)
                st.markdown("""
                <div style='background-color: #d4edda; padding: 10px; border-radius: 5px; color: black;'>
                    <p><strong>Description:</strong> The model predicts that the tumor is <strong>benign</strong>. Benign tumors are usually non-cancerous.</p>
                    <p>Still, regular monitoring and check-ups are advised.</p>
                </div>
                """, unsafe_allow_html=True)

            # Show pie chart
            display_chart(prediction_prob)

            # Generate PDF and show stylish download button
            report_path = generate_pdf(user_input, prediction, prediction_prob)
            with open(report_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                st.markdown(get_download_button(base64_pdf), unsafe_allow_html=True)

main()
