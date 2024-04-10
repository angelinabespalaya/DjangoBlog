import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

class DiabetesPredictor:
    def __init__(self):
        self.model = None
        self.features = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']  # Replace with actual feature names

    def train(self):
        data = fetch_california_housing()  # Replace with your dataset file

        X = data.data
        y = data.target

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model = Pipeline([
            ("poly_features", PolynomialFeatures(degree=2, include_bias=False)),
            ("std_scaler", StandardScaler()),
            ("lin_reg", LinearRegression())
        ])

        # Обучение модели полиномиальной регрессии
        self.model.fit(X_train, y_train)

    def predict(self, input_data):
        input_df = pd.DataFrame([input_data], columns=self.features)
        prediction = self.model.predict(input_df)
        return f'{prediction[0]} долларов'