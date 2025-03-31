import json
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
import tensorflow as tf

# Cargar datos
X = np.load("path_to_features.npy")
y = np.load("path_to_labels.npy")

# Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Cargar el modelo entrenado
model = tf.keras.models.load_model("models/model.h5")

# Realizar predicciones
predictions = model.predict(X_test)

# Convertir las predicciones a etiquetas
predicted_labels = ['positive' if pred > 0.5 else 'negative' for pred in predictions]

# Calcular las métricas
accuracy = accuracy_score(y_test, predicted_labels)
precision = precision_score(y_test, predicted_labels, pos_label='positive')
recall = recall_score(y_test, predicted_labels, pos_label='positive')
f1 = f1_score(y_test, predicted_labels, pos_label='positive')

# Mostrar las métricas
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")

# Guardar las métricas si es necesario
metrics = {
    'accuracy': accuracy,
    'precision': precision,
    'recall': recall,
    'f1_score': f1
}

with open('metrics.json', 'w') as f:
    json.dump(metrics, f)
