from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict_sentiment
from app.utils import clean_text


app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(req: TextRequest):
    cleaned = clean_text(req.text)
    sentiment = predict_sentiment(cleaned)

    return {"input": req.text, "sentiment": sentiment}
