import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from keras.regularizers import l1, l2
from keras.callbacks import EarlyStopping
from keras.layers import BatchNormalization
from datetime import datetime



MAX_NB_WORDS = 50000
MAX_SEQUENCE_LENGTH = 250
EMBEDDING_DIM = 100

def getdate():
    # Récupération de la date et de l'heure actuelles
    now = datetime.now()
    # Conversion en string avec le format souhaité
    formatted_date = now.strftime('%Y%m%d%H%M%S')
    return formatted_date

def process_data(text, MAX_NB_WORDS=50000, EMBEDDING_DIM=100, MAX_SEQUENCE_LENGTH=250):
    
    # Initialisation et ajustement du tokenizer
    tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
    tokenizer.fit_on_texts([text])
    
    # Transformation du texte
    X = tokenizer.texts_to_sequences([text])
    X = pad_sequences(X, maxlen=MAX_SEQUENCE_LENGTH)

    # Construction du modèle
    new_model = Sequential()
    new_model.add(Embedding(MAX_NB_WORDS, EMBEDDING_DIM, input_length=X.shape[1]))
    new_model.add(SpatialDropout1D(0.3))
    new_model.add(LSTM(50, dropout=0.3, recurrent_dropout=0.3))
    new_model.add(Dense(7, activation='sigmoid', kernel_regularizer=l2(0.01)))
    new_model.add(BatchNormalization())
    
    # Chargement des poids
    new_model.load_weights("blog/programs/model_weights.h5")

    # Prédiction
    predictions = new_model.predict(X)

    capteur_names = ["Caméra RGB", "Caméra Infrarouge", "Caméra Thermique", "Caméra de profondeur", "Capteurs Ultrasons", "LED", "Laster télémètre"]  # Remplissez ceci avec les noms réels des capteurs
    threshold = 0.2

    predicted_capteurs = [capteur_names[i] for i, score in enumerate(predictions[0]) if score > threshold]

    resultat ="Capteurs prédits :", ", ".join(predicted_capteurs)
    return resultat




    
