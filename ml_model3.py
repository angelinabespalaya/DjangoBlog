import numpy as np
import pandas as pd
from keras import Sequential
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense


class Iris_neiron:
    def __init__(self):
        self.model = None
        self.features = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']  # Replace with actual feature names
        self.scaler = StandardScaler()

    def train(self):
        # Загрузка датасета Iris
        iris = load_iris()
        X = iris.data
        y = iris.target

        # Нормализация данных
        X_scaled = self.scaler.fit_transform(X)

        # Разделение данных на обучающий и тестовый наборы
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

        # Подготовка данных для RNN (добавление временного измерения)
        X_train_rnn = X_train.reshape(-1, 1, 4)
        X_test_rnn = X_test.reshape(-1, 1, 4)

        # Создание и компиляция модели RNN
        self.model = Sequential([
            SimpleRNN(32),
            Dense(3, activation='softmax')
        ])

        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

        # Обучение модели
        self.model.fit(X_train_rnn, y_train, epochs=50, batch_size=16, validation_split=0.1)

    def predict(self, input_data):
        input_df = pd.DataFrame([input_data], columns=self.features)
        new_data_scaled = self.scaler.transform(input_df)
        new_data_reshaped = new_data_scaled.reshape(-1, 1, 4)
        predictions = self.model.predict(new_data_reshaped)
        prediction = np.argmax(predictions, axis=1)


        if prediction[0] == 0:
            return 'Вид ириса - setosa'
        elif prediction[0] == 1:
            return 'Вид ириса - versicolor'
        else:
            return 'Вид ириса - virginica'