import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os

# Function to create a model
def create_model(data):
    # Use all features except the 'diagnosis' column
    X = data.drop(['diagnosis'], axis=1)
    y = data['diagnosis']
    
    # Save feature names to use for both training and prediction
    feature_names = X.columns

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split the data for training and testing
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Train the model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Evaluate the model on the test set
    y_pred = model.predict(X_test)
    print('Accuracy of the model: {:.2f}%'.format(accuracy_score(y_test, y_pred) * 100))
    print('Classification report of the model: \n', classification_report(y_test, y_pred))
    print('Confusion matrix of the model: \n', confusion_matrix(y_test, y_pred))

    return model, scaler, feature_names

# Load and clean the dataset
def get_clean_data():
    data = pd.read_csv('data/breastCancer.csv')

    # Remove unnecessary columns
    data = data.drop(['id'], axis=1)
    data = data.drop(['Unnamed: 32'], axis=1)

    # Map the categorical 'diagnosis' column to numerical (M -> 1, B -> 0)
    data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})

    return data

# Save the model, scaler, and feature names to files
def save_model(model, scaler, feature_names):
    if not os.path.exists('model'):
        os.makedirs('model')

    joblib.dump(model, 'model/model.pkl')
    joblib.dump(scaler, 'model/scaler.pkl')
    joblib.dump(feature_names, 'model/feature_names.pkl')  # Save feature names

def main():
    # Load and clean data, train model, and save artifacts
    data = get_clean_data()
    model, scaler, feature_names = create_model(data)
    save_model(model, scaler, feature_names)

main()
