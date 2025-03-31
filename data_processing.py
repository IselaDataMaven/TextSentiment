import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

# Asegúrate de descargar los recursos necesarios de NLTK
nltk.download('punkt')

# Cargar datos
train_data = pd.read_csv("data/train/train.csv")

# Procesamiento de texto
train_data['text'] = train_data['text'].apply(lambda x: word_tokenize(x.lower()))

