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



MAX_NB_WORDS = 1000
MAX_SEQUENCE_LENGTH = 250
EMBEDDING_DIM = 50

def getdate():
    # Récupération de la date et de l'heure actuelles
    now = datetime.now()
    # Conversion en string avec le format souhaité
    formatted_date = now.strftime('%Y%m%d%H%M%S')
    return formatted_date

def process_data(text, MAX_NB_WORDS=1000, EMBEDDING_DIM=50, MAX_SEQUENCE_LENGTH=250):
    
    # Initialisation et ajustement du tokenizer
    tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
    tokenizer.fit_on_texts([text])
    
    # Transformation du texte
    X = tokenizer.texts_to_sequences([text])
    X = pad_sequences(X, maxlen=MAX_SEQUENCE_LENGTH)

    # Construction du modèle
    model = Sequential()
    model.add(Embedding(MAX_NB_WORDS, EMBEDDING_DIM, input_length=X.shape[1]))
    model.add(SpatialDropout1D(0.3))
    model.add(LSTM(50, dropout=0.1, recurrent_dropout=0.1, return_sequences=True))
    model.add(LSTM(50, dropout=0.1, recurrent_dropout=0.1, return_sequences=False))

    model.add(Dense(7, activation='sigmoid', kernel_regularizer=l2(0.01)))
    
    # Chargement des poids
    model.load_weights("blog/programs/capteurs.h5")

    # Prédiction
    predictions = model.predict(X)

    capteur_names = ["Caméra RGB", "Caméra Infrarouge", "Caméra Thermique", "Caméra de profondeur", "Capteurs Ultrasons", "LED", "Laster télémètre"]  # Remplissez ceci avec les noms réels des capteurs
    threshold = 0.2

    predicted_capteurs = [capteur_names[i]+" avec un pourcentage de sûreté de "+str(round(score*100,1)) +'%' for i, score in enumerate(predictions[0]) ]

    resultat = "Capteurs prédits : -"
    for ac in predicted_capteurs:
        resultat +=  ac + "-"
    return resultat




    

def process_data1(text, MAX_NB_WORDS=1000, EMBEDDING_DIM=50, MAX_SEQUENCE_LENGTH=250):
    
    # Initialisation et ajustement du tokenizer
    tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
    tokenizer.fit_on_texts([text])
    
    # Transformation du texte
    X = tokenizer.texts_to_sequences([text])
    X = pad_sequences(X, maxlen=MAX_SEQUENCE_LENGTH)

    # Construction du modèle
    model = Sequential()
    model.add(Embedding(MAX_NB_WORDS, EMBEDDING_DIM, input_length=X.shape[1]))
    model.add(SpatialDropout1D(0.3))
    model.add(LSTM(50, dropout=0.1, recurrent_dropout=0.1, return_sequences=True))
    model.add(LSTM(50, dropout=0.1, recurrent_dropout=0.1, return_sequences=False))

    model.add(Dense(7, activation='sigmoid', kernel_regularizer=l2(0.01)))
    # model.add(BatchNormalization())
    
    # Chargement des poids
    model.load_weights("blog/programs/actionneurs.h5")

    # Prédiction
    predictions = model.predict(X)

    actionneur_names = [
            "Pince",
            "Verin",
            "Haut_parleur",
            "Pompe",
            "Ecran",
            "Electroaimant",
            "Tapis_roulant"
        ]
    threshold = 0.3

    predicted_ac = [actionneur_names[i]+" avec un pourcentage de sûreté de "+str(round(score*100,1)) +'%' for i, score in enumerate(predictions[0]) ]

    resultat = "Actionneurs prédits : -"
    for ac in predicted_ac:
        resultat += ac+"-"

    return resultat



    
