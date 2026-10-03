import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"


from tensorflow.keras.preprocessing.text import Tokenizer

from tensorflow.keras.preprocessing.text import Tokenizer

Sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

tokenizer = Tokenizer()

tokenizer.fit_on_texts(Sentences)

sequences = tokenizer.texts_to_sequences(Sentences)

for sentence, sequence in zip(Sentences, sequences):
    print("sentence:", sentence)
    print("sequence:", sequence)
    print("-------------------------")