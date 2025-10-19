import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.utils import to_categorical
from emnist import extract_training_samples, extract_test_samples
import numpy as np

# Load EMNIST Letters + Digits dataset
x_train, y_train = extract_training_samples('letters')
x_test, y_test = extract_test_samples('letters')

# Normalize and reshape
x_train = x_train / 255.0
x_test = x_test / 255.0
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# Convert labels to 0-based indexing
y_train = y_train - 1
y_test = y_test - 1

# One-hot encode labels
y_train = to_categorical(y_train, 26)
y_test = to_categorical(y_test, 26)

# Build CNN
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(26, activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

print("🧠 Training EMNIST model...")
model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))
model.save('model/emnist_model.h5')
print("✅ EMNIST model saved!")
