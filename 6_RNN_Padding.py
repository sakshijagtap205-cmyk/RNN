import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

from tensorflow.keras.preprocessing.text import Tokenizer

sequences = [
    [1,2,3],
    [1,2,4],
    [1,2,5,3]
]

print("original sequences")
for sequence in sequences:
    print(sequence, "length:",len(sequence))
    
print("all sequences are different lengths")