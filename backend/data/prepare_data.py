import pandas as pd
from datasets import load_dataset
import re # Regular Expression library for manipulating strings
import os

def clean_text(text):
    # Find strings which starts with http OR www. and replace these with blank
    '''
    "Check this out: https://example.com"
    → "Check this out: "
    '''
    text = re.sub(r"http\S+|www.\S+","",text)

    # Find strings which starts with @ OR # and replace these with blank
    '''
    "@user this is perfect! #perfection"
    → " this is perfect! "
    '''
    text = re.sub(r"@\w+|#\w+","",text)

    # Remove punctiations and special chars
    '''
    "Hello! Sup? :)"
    → "Hello Sup "
    '''
    text = re.sub(r"[^\w\s]", "", text)

    # Make text lowercase
    '''
    "HelLo wOrlD"
    → "hello world"
    '''
    text = text.lower()

    #return the text
    return text

def prepare_sentiment():
    # download dataset
    dataset = load_dataset("sentiment140")
    
    # convert the data to DataFrame
    df = dataset["train"].to_pandas()
    
    # print raw row count
    print("Pos, Neut & Neg:", len(df))
    
    # Remove Neutral comments
    df = df[df["sentiment"]!=2]

    # print row count
    print("Pos & Neg #record:", len(df))

    # rename the sentiments
    df["sentiment"] = df["sentiment"].replace({0: "negative", 4: "positive"})

    # apply clean_text
    df["clean_text"] = df["text"].apply(clean_text)
    
    # construct df with clean_text & sentiment columns
    df = df[["clean_text", "sentiment"]]

    # save the df as csv
    os.makedirs("../data", exist_ok=True) 
    df.to_csv("data/cleaned_sentiment.csv", index=False)

if __name__ == "__main__":
    prepare_sentiment()