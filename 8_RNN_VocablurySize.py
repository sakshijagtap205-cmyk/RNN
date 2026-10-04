import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

from tensorflow.keras.preprocessing.text import Tokenizer

Sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

tokenizer = Tokenizer()

tokenizer.fit_on_texts(Sentences)

word_index = tokenizer.word_index

vocab_size = len(word_index) + 1

print("Number of unique words :", len(word_index))
print("padding index : 0")

print("vocabulary size:", vocab_size)