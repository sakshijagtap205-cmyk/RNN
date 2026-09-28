Sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

Vocabulary =[]

for sentence in Sentences:
    words = sentence.split()
    
    for word in words:
        if word not in Vocabulary:
            Vocabulary.append(word)
            
for index, X in enumerate(Vocabulary):
    print("position", index+1 , ":", X)
    
    