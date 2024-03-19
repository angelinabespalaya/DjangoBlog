from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

class DiabetesPredictor:
    def __init__(self):
        self.model = None
        self.features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']  # Replace with actual feature names

    def train(self):
        data = pd.read_csv('diabetes.csv')  # Replace with your dataset file

        X = data[self.features]
        y = data['Outcome']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model = RandomForestClassifier()
        self.model.fit(X_train, y_train)

    def predict(self, input_data):
        input_df = pd.DataFrame([input_data], columns=self.features)
        prediction = self.model.predict(input_df)
        if prediction[0] == 0:
            return 'У вас нет диабета'
        else:
            return 'У вас может быть диабет'