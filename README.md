# CureCanAI

CureCancAI is a web application built with Streamlit that helps users detect breast cancer. The application uses Firebase for authentication and features a secure signup and login system.

**[Live Preview](https://curecanai.onrender.com/)** - Check out the live version of the application.

## Features

- **User Authentication**: Secure user signup and login with Firebase Authentication.
- **Breast Cancer Detection**: Leverage AI to detect cancer and present detailed results.
- **Dashboard**: Provides data visualization with beautiful charts (using libraries like Matplotlib, Plotly).
- **Responsive Design**: Streamlit provides a clean and responsive interface.

## Setup Instructions

To run the application locally, follow these steps:

### Prerequisites

- Python 3.8 or above
- Firebase account (with admin SDK setup)

### Installation

1. **Clone the repository:**
   ```bash
      git clone https://github.com/yourusername/curecancai.git
      cd CureCanAI
   ```

2. **Install Dependencies:**
   ```bash
       pip install -r requirements.txt
   ```

3. **Set up environment variables:**
- Create a .env file in the root directory.
- Use the provided .env.sample as a template to add your variables

4. **Firebase Admin SDK:**
- Add your Firebase Admin SDK JSON file and update the path in your code.

5. **Run the App:**
   ```bash
      streamlit run app.py
   ```

## Made By ByteForce for Google GenAI Excchange hackathon

### Members:
- [Tuhin Ghosh](https://github.com/TuhinCodeCraft)
- [Anushka Das](https://github.com/AnushkaTechSpace)
- [Pritam Mahata](https://github.com/PritamMahata)
- [Sourav Pal](https://github.com/Souravpal08)
