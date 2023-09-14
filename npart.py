import tensorflow as tf
from tensorflow import keras

# Создаем простую последовательную модель
model = keras.Sequential()

# Добавляем входной слой с 64 нейронами
model.add(keras.layers.Dense(64, activation='relu', input_shape=(input_shape,)))

# Добавляем выходной слой с 1 нейроном (простая бинарная классификация)
model.add(keras.layers.Dense(1, activation='sigmoid'))

# Компилируем модель
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Выводим информацию о модели
model.summary()
