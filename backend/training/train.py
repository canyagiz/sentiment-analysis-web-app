# Imports
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset
import torch
import os

# load_data method
def load_data():
    df = pd.read_csv("data/cleaned_sentiment.csv")
    label_map = {"negative":0, "positive":1}
    df["label"] = df["sentiment"].map(label_map)
    return df

# tokenize_data method
def tokenize_data(df, tokenizer):
    dataset = Dataset.from_pandas(df[["clean_text","label"]])
    dataset = dataset.map(lambda x: tokenizer(x["clean_text"], padding="max_length", truncation=True), batched=True)
    dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "label"])
    return dataset

# train_model method
def train_model():
    df = load_data()
    tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")
    
    train_df, val_df = train_test_split(df,test_size=0.2, random_state=42)
    
    train_dataset = tokenize_data(train_df, tokenizer)
    val_dataset = tokenize_data(val_df, tokenizer)

    model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)

    training_args = TrainingArguments(
        output_dir="../models/checkpoints",
        eval_strategy="epoch",
        save_strategy="epoch",
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        num_train_epochs=2,
        weight_decay=0.01,
        logging_dir="../models/logs",
        logging_steps=10,
        load_best_model_at_end=True        
        )
    
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset
    )

    trainer.train()
    trainer.save_model("../models/distilbert_model")
    tokenizer.save_pretrained("../models/distilbert-tokenizer")

    # Performance
    preds = trainer.predict(val_dataset)
    y_true = val_df["label"]
    y_pred = preds.predictions.argmax(axis=1)
    print(classification_report(y_true,y_pred))

if __name__ == "__main__":
    train_model()