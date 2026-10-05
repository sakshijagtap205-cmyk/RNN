import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"


Sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

labels =[1,0,0]

for sentences , labels in zip(Sentences, labels):
   

    print("Sentence:" ,sentences) 
    
    print("label:", labels)
    
    if label ==1:
        print("Meaning: Positive sentiment")
        
    else:
        print("Meaning: Negative sentiment")
   
    print("Meaning :",sentiment)
    print("------------------------------------------------")
    
         