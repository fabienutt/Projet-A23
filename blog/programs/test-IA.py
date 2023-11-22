

import tensorflow as tf

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


print("TensorFlow version:", tf.__version__)
"""Chargement et prétraitement des données"""

data = pd.read_csv('data.csv')

# Supposons que la première colonne s'appelle 'description'
texts = data['colonne_texte'].values
labels = data.iloc[:, 1:].values  # Prendre toutes les colonnes après la description

"""Tokenisation des textes"""

MAX_NB_WORDS = 50000
MAX_SEQUENCE_LENGTH = 250
EMBEDDING_DIM = 100

tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
tokenizer.fit_on_texts(texts)
word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index))

X = tokenizer.texts_to_sequences(texts)
X = pad_sequences(X, maxlen=MAX_SEQUENCE_LENGTH)
print('Shape of data tensor:', X.shape)

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

x_train, x_test, y_train, y_test = train_test_split(X, labels, test_size=0.35, random_state=42)
# [`Sequential`](https://www.tensorflow.org/guide/keras/sequential_model) is useful for stacking layers where each layer has one input [tensor](https://www.tensorflow.org/guide/tensor) and one output tensor. Layers are functions with a known mathematical structure that can be reused and have trainable variables. Most TensorFlow models are composed of layers. This model uses the [`Flatten`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Flatten), [`Dense`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense), and [`Dropout`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dropout) layers.
# 
# For each example, the model returns a vector of [logits](https://developers.google.com/machine-learning/glossary#logits) or [log-odds](https://developers.google.com/machine-learning/glossary#log-odds) scores, one for each class.

# In[5]:


predictions = model(x_train[:1]).numpy()
predictions


# The `tf.nn.softmax` function converts these logits to *probabilities* for each class: 

# In[6]:


tf.nn.softmax(predictions).numpy()


# Note: It is possible to bake the `tf.nn.softmax` function into the activation function for the last layer of the network. While this can make the model output more directly interpretable, this approach is discouraged as it's impossible to provide an exact and numerically stable loss calculation for all models when using a softmax output. 

# Define a loss function for training using `losses.SparseCategoricalCrossentropy`:

# In[7]:


loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)


# The loss function takes a vector of ground truth values and a vector of logits and returns a scalar loss for each example. This loss is equal to the negative log probability of the true class: The loss is zero if the model is sure of the correct class.
# 
# This untrained model gives probabilities close to random (1/10 for each class), so the initial loss should be close to `-tf.math.log(1/10) ~= 2.3`.

# In[8]:


loss_fn(y_train[:1], predictions).numpy()


# Before you start training, configure and compile the model using Keras `Model.compile`. Set the [`optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers) class to `adam`, set the `loss` to the `loss_fn` function you defined earlier, and specify a metric to be evaluated for the model by setting the `metrics` parameter to `accuracy`.

# In[9]:


model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])


# ## Train and evaluate your model
# 
# Use the `Model.fit` method to adjust your model parameters and minimize the loss: 

# In[10]:


model.fit(x_train, y_train, epochs=5)


# The `Model.evaluate` method checks the model's performance, usually on a [validation set](https://developers.google.com/machine-learning/glossary#validation-set) or [test set](https://developers.google.com/machine-learning/glossary#test-set).

# In[11]:


model.evaluate(x_test,  y_test, verbose=2)


# The image classifier is now trained to ~98% accuracy on this dataset. To learn more, read the [TensorFlow tutorials](https://www.tensorflow.org/tutorials/).

# If you want your model to return a probability, you can wrap the trained model, and attach the softmax to it:

# In[12]:


probability_model = tf.keras.Sequential([
  model,
  tf.keras.layers.Softmax()
])


# In[13]:


probability_model(x_test[:5])


# ## Conclusion
# 
# Congratulations! You have trained a machine learning model using a prebuilt dataset using the [Keras](https://www.tensorflow.org/guide/keras/overview) API.
# 
# For more examples of using Keras, check out the [tutorials](https://www.tensorflow.org/tutorials/keras/). To learn more about building models with Keras, read the [guides](https://www.tensorflow.org/guide/keras). If you want learn more about loading and preparing data, see the tutorials on [image data loading](https://www.tensorflow.org/tutorials/load_data/images) or [CSV data loading](https://www.tensorflow.org/tutorials/load_data/csv).
# 
