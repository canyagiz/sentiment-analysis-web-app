from transformers import DistilBertForSequenceClassification, DistilBertTokenizerFast
import torch

# Model ve tokenizer'ı belleğe yükle
model = DistilBertForSequenceClassification.from_pretrained("models/sst2_model")
tokenizer = DistilBertTokenizerFast.from_pretrained("models/sst2_tokenizer")
                                                    

def predict_sentiment(text: str) -> str:
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True) # tokenizer output -> PyTorch tensor
    
    with torch.no_grad():   # Turns of gradient computing since there is only predition
        outputs = model(**inputs) # (**inputs) means the inputs dictionary gonna be converted to (key=value) for passing as argument
        prediction = torch.argmax(outputs.logits, dim=1).item() # Chooses the max score prediction, .item(): tensor -> py integer
    
    return "positive" if prediction ==1 else "negative"