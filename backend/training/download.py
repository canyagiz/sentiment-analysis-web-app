from transformers import pipeline
from transformers import DistilBertForSequenceClassification, DistilBertTokenizerFast

model_name = "distilbert-base-uncased-finetuned-sst-2-english"

DistilBertForSequenceClassification.from_pretrained(model_name).save_pretrained("../models/sst2_model")
DistilBertTokenizerFast.from_pretrained(model_name).save_pretrained("../models/sst2_tokenizer")
