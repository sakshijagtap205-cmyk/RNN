import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"


from tensorflow.keras.preprocessing.text import Tokenizer

from tensorflow.keras.preprocessing.sequence import pad_sequences

Sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

tokenizer = Tokenizer()

tokenizer.fit_on_texts(Sentences)

sequences = tokenizer.texts_to_sequences(Sentences)

print("original sequences")
for sequence in sequences:
    print(sequence, "length:",len(sequence))
    
print("all sequences are different lengths")

max_length = 4

padded_sequences = pad_sequences(
    sequences,
    maxlen=max_length,
    padding="pre"
)

for sentence, sequence , padded in zip(Sentences, sequences, padded_sequences):
    print("sentence:", sentence)
    print("Original 
          sequence:", sequence)
    print("padded sequence:", padded)
    print("-------------------------")
