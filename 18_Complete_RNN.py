import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import sequential
from tensorflow.keras.layers import Embedding , SimpleRNN , Dense

#step 1 : load the data

train_sentence = [
    "food was good",
    "food was bad",
    "food was excellent",
    "Food was terrible",
    "service was good",
    "service was bad"
    "service was excellent",
    "service was terrible",
    "ambiance was good",
    "ambiance was bad"
    "ambiance was excellent",
    "ambiance was terrible"
]

train_labels =[
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0
    
]

#step 2 : Tokenization

Tokenizer = Tokenizer(oov_token = "<oov>")

Tokenizer.fit_on_texts(train_sentence)

#step 3 : convert training data into sequence


train_sentence = Tokenizer.texts_to_sequences(train_sentence)

print("Training sequences :")

for sentence , sequence in zip(train_sentence, train_sequence):
    print(sentence, "->", sequence)
    
    