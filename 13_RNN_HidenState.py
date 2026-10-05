words = ["food", "was", "not", "good"]

hidden_state = "Empty memory"

print("Input tokens :", words)

print("Initial  hidden state", hidden_state)

for index, word in enumerate(words):
    print("Timestep :", index+1)
    print("Current word:", word)
    print("Prevoius memory", hidden_state)
    
    hidden_state = "memory after reading"+" ".join(words[:index+1]) + ""     #list slicing
    print("Updated memory :", hidden_state)
    
    print("-"*30)
    
    