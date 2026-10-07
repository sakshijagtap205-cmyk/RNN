# ht = tanh(Wx * xt + Wh * ht-1 + b)

# xt      Current input
# wx      Weight for input
# wh      Weight for previous hidden state
# b       Bias
# ht-1    Previous hidden state
# tanh    Activation function (-1 to 1)
# ht      new hidden state

import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def MarvellousRNNPredictions():
    print("Calculations of RNN")
    
    #Food was not good
    inputs = [1,2,5,3]
    
    
    hidden_State =0
    
    #RNN parameters
    
    wx = 0.5
    wh = 0.8
    bias = 0.1
    
    for  time_step , x in enumerate(inputs):
        prevoius_Hidden_State = hidden_State
        
        weighted_input = wx * x
        weighted_memory = wh * prevoius_Hidden_State
        
        total = weighted_input + weighted_memory + bias
        
        hidden_State = np.tanh(total)
        
        print("Time Step :", time_step+1)
        print("input : ", x)
        print("Hidden state ", hidden_State)
        print("-"*30)
    
    print("Final hidden state", hidden_State)



def main():
    MarvellousRNNPredictions()
    
if __name__ == "__main__":
    main()