sentence = "food was  not good"

#timestep  1    2   3   4
#token    1    2   5   3
#Embedding [0.7 0.1 0.2 0.3] [0.1 0.2 0.3 0.4] [0.5 0.6 0.7 0.8] [0.9 1.0 1.1 1.2]


words = sentence.split()

print("Actual Sentence is", sentence)

for index , words in enumerate(words):
    print("TimeStep :", index+1, ":", words)
    