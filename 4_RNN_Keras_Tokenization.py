from tensorflow.keras.preprocessing.text import Tokenizer

Sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

tokenizer = Tokenizer()

tokenizer.fit_on_texts(Sentences)

word_index = tokenizer.word_index

for word , index in word_index.items():
    print("position" , index, ":", word)