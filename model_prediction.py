import json
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import tensorflow as tf

# Cargar el conjunto de datos de prueba
X_test = np.load("path_to_test_features.npy")
y_test = np.load("path_to_test_labels.npy")

# Cargar el modelo entrenado
model = tf.keras.models.load_model("models/model.h5")

# Realizar las predicciones
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

# Guardar las métricas en un archivo JSON
metrics = {
    'accuracy': accuracy,
    'precision': precision,
    'recall': recall,
    'f1_score': f1
}

with open('predictions/metrics.json', 'w') as f:
    json.dump(metrics, f)

# También puedes guardar las predicciones si es necesario
with open("predictions/predictions.json", "w") as f:
    json.dump(predicted_labels, f)
