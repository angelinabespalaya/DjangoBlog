import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

# Загрузка датасета Iris
iris = load_iris()
X = iris.data
y = iris.target

# Нормализация данных
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Подготовка данных для RNN (добавление временного измерения)
X_train_rnn = X_train.reshape(-1, 1, 4)
X_test_rnn = X_test.reshape(-1, 1, 4)

# Создание и компиляция модели RNN
model = Sequential([
    SimpleRNN(32),
    Dense(3, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Обучение модели
model.fit(X_train_rnn, y_train, epochs=50, batch_size=16, validation_split=0.1)

# Оценка производительности модели на тестовых данных
loss, accuracy = model.evaluate(X_test_rnn, y_test)
print("Test Loss:", loss)
print("Test Accuracy:", accuracy)
